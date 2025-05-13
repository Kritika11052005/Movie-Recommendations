# Movie-Recommendations
# 🎬 Movie Recommendation System

A content-based movie recommendation system built using Python and scikit-learn that suggests similar movies based on genre metadata. This project demonstrates a beginner-friendly application of machine learning and NLP techniques for real-world recommendation problems.

---

## 📌 Project Overview

With the overwhelming number of movies available today, viewers often struggle to find content tailored to their preferences. This project addresses that issue by recommending similar movies based on genre information using **TF-IDF vectorization** and **cosine similarity**.

---

## 🧠 Features

- Content-based recommendations using **genre metadata**
- Uses **TF-IDF Vectorizer** and **cosine similarity**
- Accepts partial or case-insensitive input (e.g., "toy story", "Matrix")
- Optimized for large datasets (over 60,000+ movies)
- Lightweight and easy to extend

---

## 🚀 Technologies Used

- **Python 3.12+**
- **pandas**
- **scikit-learn**
- **TfidfVectorizer**
- **cosine_similarity**
- Dataset: `movies.csv` (from [MovieLens](https://grouplens.org/datasets/movielens/))

---

## ⚙️ How It Works

1. Load `movies.csv` containing `movieId`, `title`, and `genres`.
2. Clean and vectorize genres using TF-IDF.
3. Compute cosine similarity between all movie vectors.
4. Accept user input, match it against the title list.
5. Return the top 5 most similar movies.

---
Example Input/Output

🎬 Recommendations for 'toy story':
• Toy Story 2
• A Bug's Life
• Monsters, Inc.
• Shrek
• Finding Nemo

🔮 Future Improvements
Add collaborative filtering based on user ratings

Combine genres, keywords, cast, and overview for hybrid recommendations

Deploy as a Streamlit or Flask web app

Integrate with TMDB or IMDb APIs


👩‍💻 Author
Kritika Benjwal
Manipal University Jaipur
Email: ananya.benjwal@gmail.com

📚 References:
scikit-learn documentation:https://scikit-learn.org/stable/

Movie dataset:https://www.kaggle.com/datasets/parasharmanas/movie-recommendation-system?resource=download&select=movies.csv

TF-IDF Explanation:https://en.wikipedia.org/wiki/Tf%E2%80%93idf


## ⚙️ How It Works

1. Load `movies.csv` containing `movieId`, `title`, and `genres`.
2. Clean and vectorize genres using TF-IDF.
3. Compute cosine similarity between all movie vectors.
4. Accept user input, match it against the title list.
5. Return the top 5 most similar movies.

---

## 📥 Installation

```bash
git clone https://github.com/yourusername/movie-recommendation-system.git
cd movie-recommendation-system
pip install -r requirements.txt




