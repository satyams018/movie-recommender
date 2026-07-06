# 🍿 Movie Recommender System

A content-based machine learning movie recommendation web application built with Python and Streamlit. This system analyzes movie metadata to suggest five films similar to your favorites and dynamically fetches their official posters using the TMDB API.

## 🌟 Features
* **Machine Learning Powered:** Utilizes natural language processing and vector embeddings to calculate cosine similarity between thousands of films.
* **Dynamic API Integration:** Connects to the TMDB (The Movie Database) API to fetch high-quality movie posters in real-time.
* **Modern UI:** Built with Streamlit for a clean, responsive, and wide-layout web interface.
* **Robust Architecture:** Includes network retry strategies to handle API timeouts and Git LFS for safely versioning massive similarity matrix models.

## 🧠 How It Works (The Data Pipeline)
1. **Data Source:** The model is trained on the [TMDB 5000 Movie Dataset from Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).
2. **Preprocessing:** Data cleaning, merging, and feature extraction were performed in a Google Colab environment. 
3. **Vectorization:** Text data (tags, genres, cast, crew) was converted into vector embeddings using `scikit-learn`.
4. **Recommendation Engine:** The system calculates the **Cosine Similarity** between these vectors to find the mathematically closest movie matches.

## 🛠️ Tech Stack
* **Language:** Python
* **Data Science & ML:** Pandas, Scikit-learn, Google Colab
* **Frontend/Web Framework:** Streamlit
* **Network Requests:** Requests, urllib3
* **Version Control:** Git, Git LFS (Large File Storage)
* **API:** The Movie Database (TMDB) API

## 🚀 How to Run Locally

**1. Clone the repository and pull large files**
Since this project uses Git LFS for the similarity matrix, make sure you have Git LFS installed before cloning.
```bash
git clone [https://github.com/satyams018/movie-recommender.git](https://github.com/satyams018/movie-recommender.git)
cd movie-recommender
git lfs pull


```

**2. Install dependencies**

```bash
pip install -r requirements.txt

```

**3. Set up the TMDB API Key**
Create a `.streamlit` folder in the root directory. Inside it, create a `secrets.toml` file and add your API key:

```toml
TMDB_API_KEY = "your_api_key_here"

```

**4. Run the Streamlit app**

```bash
streamlit run app.py

```

## 🌐 Deployment

This application is fully configured for deployment on **Streamlit Community Cloud**. The massive `similarity.pkl` model (176+ MB) is safely managed via Git LFS, allowing for seamless cloud deployment.

---

**Author:** Satyam Sharma

```

```
