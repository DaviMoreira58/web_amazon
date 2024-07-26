import streamlit as st
from main import df_reviews, df_top100_books
import pandas as pd

st.set_page_config(layout='wide')

books = df_top100_books['book title'].unique()
book = st.sidebar.selectbox(
    'Books',
    books
)

df_book = df_top100_books[df_top100_books['book title'] == book]
df_reviews_f = df_reviews[df_reviews['book name'] == book]

book_title = df_book['book title'].iloc[0]
