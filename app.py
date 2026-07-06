import streamlit as st
import pickle 
import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# 1. Page Config (Must be the very first Streamlit command)
st.set_page_config(page_title="Movie Recommender", page_icon="🍿", layout="wide")

def fetch_poster(movie_id):
    # Fetching securely from Streamlit's secrets environment
    try:
        api_key = st.secrets["TMDB_API_KEY"]
    except KeyError:
        st.error("API Key missing. Please set TMDB_API_KEY in your deployment environment.")
        return "https://via.placeholder.com/500x750?text=Config+Error"

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    
    # Session retry logic for network stability
    session = requests.Session()
    retry_strategy = Retry(
        total=3,
        backoff_factor=0.5,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    
    try:
        response = session.get(url, timeout=10)
        response.raise_for_status() 
        data = response.json()
        
        if data.get('poster_path'):
            return "https://image.tmdb.org/t/p/w500" + data['poster_path']
        else:
            return "https://via.placeholder.com/500x750?text=No+Poster"
            
    except requests.exceptions.RequestException:
        return "https://via.placeholder.com/500x750?text=Image+Error"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_poster = []
    
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
        
    return recommended_movies, recommended_movies_poster

# Load data safely
@st.cache_data # Caches data so the app doesn't reload the pickles on every single click
def load_data():
    movie_dict = pickle.load(open('movies_dict.pkl', 'rb'))
    movies_df = pd.DataFrame(movie_dict)
    similarity_matrix = pickle.load(open('similarity.pkl', 'rb'))
    return movies_df, similarity_matrix

movies, similarity = load_data()

# User Interface
st.title('🍿 Movie Recommender System')
st.markdown("Discover your next favorite film based on what you already love.")
st.divider()

selected_movie_name = st.selectbox(
    "Search or select a movie:",
    movies['title'].values
)

if st.button("Show Recommendations", type="primary"):
    with st.spinner(f'Analyzing recommendations for {selected_movie_name}...'):
        names, posters = recommend(selected_movie_name)
    
    st.subheader("Top Picks for You")
    col1, col2, col3, col4, col5 = st.columns(5, gap="medium")

    columns = [col1, col2, col3, col4, col5]
    for idx, col in enumerate(columns):
        with col:
            st.image(posters[idx], use_container_width=True)
            st.markdown(f"**{names[idx]}**")