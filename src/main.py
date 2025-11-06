import os
import pandas as pd
from src.data_preprocessing import load_data, preprocess_dataframe
from src.sentiment_analysis import add_sentiment_columns
from src.trend_detection import build_trend_table
from src.visualization import plot_top_keywords, plot_sentiment_distribution, top_keyword_bar

def ensure_sample_dataset(path):
    if os.path.exists(path):
        return
    os.makedirs(os.path.dirname(path), exist_ok=True)
    sample = [
        {"date":"2025-10-20","text":"New AI camera on the latest smartphone is amazing"},
        {"date":"2025-10-21","text":"People love the battery life of the new phone"},
        {"date":"2025-10-22","text":"Foldable phones are getting popular and stylish"},
        {"date":"2025-10-23","text":"Users complain about phone overheating after update"},
        {"date":"2025-10-24","text":"Organic skincare product trend rising in social media"},
        {"date":"2025-10-25","text":"Electric cars discussion trending because of new model launch"},
        {"date":"2025-10-25","text":"AI cameras and battery performance praised by influencers"},
        {"date":"2025-10-26","text":"Many tweets about sustainable packaging and organic products"},
        {"date":"2025-10-27","text":"Foldable phone sales increased in last quarter"},
        {"date":"2025-10-28","text":"Electric cars have better range this year everyone excited"}
    ]
    df = pd.DataFrame(sample)
    df.to_csv(path, index=False)

def run_demo(dataset_path):
    ensure_sample_dataset(dataset_path)
    df = load_data(dataset_path)
    df = preprocess_dataframe(df, text_column='text')
    df = add_sentiment_columns(df, text_column='processed')
    trends = build_trend_table(df, text_column='processed', time_column='date', top_n=15)
    print("Top trends (keyword, count, growth_score):")
    print(trends.head(15).to_string(index=False))
    plot_top_keywords(trends, n=10)
    plot_sentiment_distribution(df)
    top_keyword_bar(df, text_column='processed', top_n=20)

if __name__ == "__main__":
    dataset_path = os.path.join(os.path.dirname(__file__), '..', 'dataset', 'sample_marketing_data.csv')
    run_demo(dataset_path)