from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

def get_top_keywords(df, text_column='processed', top_n=20):
    texts = df[text_column].dropna().astype(str).tolist()
    if len(texts) == 0:
        return []
    vectorizer = CountVectorizer(max_df=0.85, min_df=1, stop_words='english')
    X = vectorizer.fit_transform(texts)
    sums = X.sum(axis=0)
    terms = vectorizer.get_feature_names_out()
    counts = [(terms[i], int(sums[0,i])) for i in range(len(terms))]
    counts.sort(key=lambda x: x[1], reverse=True)
    return counts[:top_n]

def keyword_growth_score(df, time_column, keyword, text_column='processed'):
    if time_column not in df.columns:
        return 0
    df = df.copy()
    df[time_column] = pd.to_datetime(df[time_column], errors='coerce')
    df = df.dropna(subset=[time_column])
    df = df.sort_values(time_column)
    df['has_kw'] = df[text_column].apply(lambda t: 1 if keyword in str(t).split() else 0)
    if len(df) < 2:
        return 0
    half = len(df) // 2
    first = df['has_kw'].iloc[:half].sum()
    second = df['has_kw'].iloc[half:].sum()
    if first == 0 and second == 0:
        return 0
    growth = (second - first) / (first + 1e-6)
    return growth

def build_trend_table(df, text_column='processed', time_column=None, top_n=20):
    top = get_top_keywords(df, text_column=text_column, top_n=top_n)
    rows = []
    for term, count in top:
        growth = keyword_growth_score(df, time_column, term, text_column=text_column) if time_column else 0
        rows.append({'keyword': term, 'count': count, 'growth_score': round(float(growth), 3)})
    return pd.DataFrame(rows).sort_values(['growth_score','count'], ascending=False)