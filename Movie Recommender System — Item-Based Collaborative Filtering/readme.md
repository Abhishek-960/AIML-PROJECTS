# 🎞️ Movie Recommender System — Item-Based Collaborative Filtering 

This project builds a lightweight movie recommender engine using item-to-item collaborative filtering. It finds movies that are similar based on user rating behaviors by measuring cosine similarity between movies—no external ML libraries needed!

---

## 📌 Project Highlights

-  Recommends movies similar to a user-selected title
-  Uses cosine similarity between item-user vectors
-  Pulls actual movie titles from MovieLens metadata
-  Clean, modular Python code with intuitive logic

---

## 🧠 How It Works

1. Loads `ratings.csv` and `movies.csv` from the MovieLens dataset.
2. Creates an **Item-User Matrix**, where each row is a movie and each column is a user rating.
3. Computes **cosine similarity** between movies.
4. Accepts a user-input movie title.
5. Returns top 5 similar movies with their names and similarity scores.

This is pure collaborative filtering—but item-based instead of user-based.

---

## Results
![abhi 4](https://github.com/user-attachments/assets/ff37def6-1b9e-4f99-9be4-3767d95d679c)




## 📦 Installation

```bash
pip install pandas scikit-learn
