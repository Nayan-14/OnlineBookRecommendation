import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the pivot table model
with open('models\pt.pkl', 'rb') as file:
    pivot_table_model = pickle.load(file)

# Load the precomputed cosine similarity model
with open('models/similarity_scores.pkl', 'rb') as file:
    similarity_scores_model = pickle.load(file)

# Function to recommend top N books based on a given book name
def recommend_books_based_on_book(book_name, top_n=4):
    try:
        # Get the index of the book name in the pivot table
        book_index = pivot_table_model.index.get_loc(book_name)
    except KeyError:
        st.error('Book not found. Please try another book name.')
        return None
    
    # Retrieve the cosine similarity scores for the corresponding row or column
    similarity_scores = similarity_scores_model[book_index]
    similar_books_indices = np.argsort(similarity_scores)[::-1][1:top_n+1]
    recommended_books = pivot_table_model.index[similar_books_indices].tolist()
    return recommended_books

def search():
    st.title('Search')

    st.write('Enter the name of a book to get recommendations.')

    book_name = st.text_input('Book Name:')
    if book_name:
        recommended_books = recommend_books_based_on_book(book_name)
        if recommended_books is None:
            return
        st.subheader('Recommended Books:')
        for i, book in enumerate(recommended_books):
            st.write(f"{i+1}. {book}")

if __name__ == "__main__":
    search()
