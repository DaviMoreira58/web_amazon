import streamlit as st
import pandas as pd
import os

st.set_page_config(layout='wide')
source = os.path.abspath('.')
dir = os.path.join(source, 'datasets')
path_reviews = os.path.join(dir, 'customer reviews.csv')
path_book = os.path.join(dir, 'Top-100 Trending Books.csv')

df_reviews = pd.read_csv(path_reviews)
df_top100_books = pd.read_csv(path_book)

price_max = df_top100_books['book price'].max()
price_min = df_top100_books['book price'].min()
st.slider('Price Range', price_min, price_max, price_max)