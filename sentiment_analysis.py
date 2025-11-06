from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

analyzer = SentimentIntensityAnalyzer()

def get_sentiment_score(text):
    if not isinstance(text, str) or text.strip() == "":
        return {'neg':0.0, 'neu':1.0, 'pos':0.0, 'compound':0.0}
    return analyzer.polarity_scores(text)

def add_sentiment_columns(df, text_column='processed'):
    df = df.copy()
    scores = df[text_column].apply(get_sentiment_score)
    df['neg'] = scores.apply(lambda s: s['neg'])
    df['neu'] = scores.apply(lambda s: s['neu'])
    df['pos'] = scores.apply(lambda s: s['pos'])
    df['compound'] = scores.apply(lambda s: s['compound'])
    df['sentiment_label'] = df['compound'].apply(lambda c: 'positive' if c>=0.05 else ('negative' if c<=-0.05 else 'neutral'))
    return df