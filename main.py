import streamlit as st
import pandas as pd
import os

source = os.path.abspath('.')
dir = os.path.join(source, 'datasets')
path_reviews = os.path.join(dir, 'customer reviews.csv')
path_book = os.path.join(dir, 'Top-100 Trending Books.csv')

df_reviews = pd.read_csv(path_reviews)
df_top100_books = pd.read_csv(path_book)

