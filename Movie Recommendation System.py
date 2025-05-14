import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Step 1: Load the dataset
df = pd.read_csv("movies.csv")

# Step 2: Fill missing genres
df['genres'] = df['genres'].fillna('')

# Step 3: Convert genres to TF-IDF matrix
vectorizer = TfidfVectorizer(token_pattern=r"(?u)\b\w+\b")
tfidf_matrix = vectorizer.fit_transform(df['genres'])

# Step 4: Function to recommend movies
def recommend(title, df=df, tfidf_matrix=tfidf_matrix):
    # Try case-insensitive partial match
    matches = df[df['title'].str.contains(title, case=False, na=False)]
    
    if matches.empty:
        return f"No match found for '{title}'."
    
    idx = matches.index[0]
    
    # Compute similarity only for this movie
    sim_scores = linear_kernel(tfidf_matrix[idx], tfidf_matrix).flatten()
    sim_indices = sim_scores.argsort()[::-1][1:6]  # top 5 (excluding itself)
    
    return df['title'].iloc[sim_indices].tolist()

# Step 5: Test the recommender
user_input = input("Enter a movie: ")  # You can change this
recommendations = recommend(user_input)

print(f"\n Recommendations for '{user_input}':")
for movie in recommendations:
    print("•", movie)

