import streamlit as st
from main import df_reviews, df_top100_books
import pandas as pd

books = df_top100_books['book title'].unique()
book = st.sidebar.selectbox(
    'Books',
    books
)

df_book = df_top100_books[df_top100_books['book title'] == book]
df_book # para exibir na pagina
