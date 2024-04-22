import streamlit as st
import pandas as pd
import pickle

# Load the popularity model
with open('models\popular.pkl', 'rb') as file:
    popularity_model = pickle.load(file)

def home():
    st.title('Home')

    st.write('Welcome to Book Recommendation System!')

    st.subheader('Top 50 Books:')
    
    # Display books in a grid layout
    books_per_row = 4
    num_books = len(popularity_model)
    num_rows = (num_books - 1) // books_per_row + 1
    col_width = int(12 / books_per_row)  # Divide page width into equal parts for each column

    for i in range(num_rows):
        cols = st.columns(books_per_row)

        for j in range(books_per_row):
            idx = i * books_per_row + j
            if idx < num_books:
                book_info = popularity_model.iloc[idx]
                with cols[j]:
                    st.image(book_info['Image-URL-M'], use_column_width='always')
                    st.write(f"**{book_info['Book-Title']}**")
                    st.write(f"by {book_info['Book-Author']}")
                    st.write(f"Rating: {book_info['avg_rating']:.2f}")

    st.subheader('Search for Books:')
    st.write('Go to the search page to find book recommendations based on a book name.')

