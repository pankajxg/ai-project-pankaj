import streamlit as st
import os
import pandas as pd
from src.data_preprocessing import preprocess_dataframe, load_data
from src.sentiment_analysis import add_sentiment_columns
from src.trend_detection import build_trend_table
from src.visualization import generate_wordcloud
import matplotlib.pyplot as plt

st.set_page_config(page_title="Market Trend Analyzer", layout="wide")

dataset_path = os.path.join('dataset', 'sample_marketing_data.csv')

if not os.path.exists(dataset_path):
    from src.main import ensure_sample_dataset
    ensure_sample_dataset(dataset_path)

st.title("AI-Powered Market Trend Analyzer")

uploaded = st.file_uploader("Upload CSV with a 'text' column (optional)", type=['csv'])
if uploaded:
    df = pd.read_csv(uploaded)
else:
    df = load_data(dataset_path)

st.sidebar.header("Settings")
top_n = st.sidebar.slider("Top keywords", 5, 50, 15)
topic = st.sidebar.text_input("Search keyword (optional)")

df = preprocess_dataframe(df, text_column='text')
df = add_sentiment_columns(df, text_column='processed')

st.header("Sentiment Summary")
st.write(df['sentiment_label'].value_counts())

st.header("Top Keywords")
trends = build_trend_table(df, text_column='processed', time_column='date', top_n=top_n)
st.table(trends.head(top_n))

if topic:
    st.subheader(f"Entries containing '{topic}'")
    filtered = df[df['processed'].str.contains(topic, na=False)]
    st.write(filtered[['date','text','sentiment_label']].head(50))

st.header("Word Cloud")
wc = generate_wordcloud(df['processed'])
if wc:
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)