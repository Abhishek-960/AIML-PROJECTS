import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load datasets
ratings_df = pd.read_csv("dataset/ratings.csv")
movies_df = pd.read_csv("dataset/movies.csv")


ratings_df.drop(columns=["timestamp"], inplace=True)

# item-user matrix
item_user_matrix = ratings_df.pivot_table(index='movieId', columns='userId', values='rating')
item_user_matrix.fillna(0, inplace=True)


movie_sim = cosine_similarity(item_user_matrix)
movie_sim_df = pd.DataFrame(movie_sim, index=item_user_matrix.index, columns=item_user_matrix.index)

# input from the user
movie_title_input = input(" Enter a movie title to get recommendations: ").strip().lower()
matched = movies_df[movies_df['title'].str.lower().str.contains(movie_title_input)]

if matched.empty:
    print("⚠️ Movie not found in dataset.")
else:
    movie_id = matched.iloc[0]['movieId']
    movie_title = matched.iloc[0]['title']
    print(f"\n Movies similar to '{movie_title}':\n")

    # Get top 5 similar movies
    similar_scores = movie_sim_df[movie_id].sort_values(ascending=False)[1:6]
    similar_df = pd.DataFrame({'movieId': similar_scores.index, 'score': similar_scores.values})
    similar_named = pd.merge(similar_df, movies_df, on='movieId')

    for _, row in similar_named.iterrows():
        print(f"- {row['title']} → similarity score: {row['score']:.2f}")
