import re
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

def load_data(path):
    return pd.read_csv(path)

def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def preprocess_dataframe(df, text_column='text'):
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    df = df.copy()
    df['clean_text'] = df[text_column].apply(clean_text)
    df['tokens'] = df['clean_text'].apply(lambda t: [lemmatizer.lemmatize(w) for w in nltk.word_tokenize(t) if w not in stop_words and w.isalpha()])
    df['processed'] = df['tokens'].apply(lambda tokens: ' '.join(tokens))
    return df