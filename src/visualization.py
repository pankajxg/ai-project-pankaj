import matplotlib.pyplot as plt
import pandas as pd

def plot_top_keywords(df_trends, n=10, save_path=None):
    top = df_trends.sort_values('count', ascending=False).head(n)
    plt.figure(figsize=(10,6))
    plt.bar(top['keyword'], top['count'])
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()

def plot_sentiment_distribution(df, save_path=None):
    counts = df['sentiment_label'].value_counts()
    plt.figure(figsize=(6,6))
    plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=140)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()

def top_keyword_bar(df, text_column='processed', top_n=20, save_path=None):
    words = ' '.join(df[text_column].dropna().astype(str).tolist()).split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    items = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:top_n]
    if not items:
        return None
    words, counts = zip(*items)
    plt.figure(figsize=(10,6))
    plt.bar(words, counts)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()
    return items