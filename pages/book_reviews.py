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
df_book # para exibir na pagina

df_reviews_f = df_reviews[df_reviews['book name'] == book]
df_reviews_f # para exibir na pagina