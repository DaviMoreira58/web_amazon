import streamlit as st
from main import df_reviews, df_top100_books
import pandas as pd

books = df_top100_books['book title'].unique()
book = st.sidebar.selectbox(
    'Books',
    books
)