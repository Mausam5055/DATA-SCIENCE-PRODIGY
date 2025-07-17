import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import nltk
from nltk.corpus import stopwords
import re

def analyze_sentiment(filepath):
    """
    Analyzes and visualizes sentiment from a CSV file.

    Args:
        filepath (str): The path to the CSV file.
    """
    try:
        stopwords.words('english')
    except LookupError:
        nltk.download('stopwords')

    try:
        # The CSV doesn't have a header, so we assign column names.
        col_names = ['TweetID', 'Entity', 'Sentiment', 'Tweet_Content']
        df = pd.read_csv(filepath, header=None, names=col_names)
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return

    df.dropna(subset=['Tweet_Content'], inplace=True)


    # --- 1. Sentiment Distribution ---
    plt.figure(figsize=(8, 6))
    sns.countplot(x='Sentiment', data=df, order=df['Sentiment'].value_counts().index, palette='viridis')
    plt.title('Distribution of Sentiments')
    plt.xlabel('Sentiment')
    plt.ylabel('Number of Tweets')
    plt.tight_layout()
    plt.savefig('sentiment_distribution.png')
    print("Generated sentiment_distribution.png")


    # --- 2. Keyword Analysis ---

    def preprocess_text(text):
        """Basic text preprocessing."""
        if not isinstance(text, str):
            return []
        text = text.lower()
        text = re.sub(r'http\S+', '', text)  # Remove URLs
        text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove non-alphabetic characters
        tokens = text.split()
        try:
            stop_words = set(stopwords.words('english'))
            filtered_tokens = [word for word in tokens if word not in stop_words]
        except Exception:
            # If stopwords are not available, return original tokens
            filtered_tokens = tokens
        return filtered_tokens

    df['processed_text'] = df['Tweet_Content'].apply(preprocess_text)

    sentiments = df['Sentiment'].unique()
    top_words = {}

    for sentiment in sentiments:
        all_words = [word for tokens in df[df['Sentiment'] == sentiment]['processed_text'] for word in tokens]
        word_counts = Counter(all_words)
        top_words[sentiment] = word_counts.most_common(15)

    for sentiment, words in top_words.items():
        if not words:
            continue
        plt.figure(figsize=(10, 8))
        word_df = pd.DataFrame(words, columns=['Word', 'Frequency'])
        sns.barplot(x='Frequency', y='Word', data=word_df, palette='plasma')
        plt.title(f'Top 15 Keywords for {str(sentiment).capitalize()} Sentiment')
        plt.xlabel('Frequency')
        plt.ylabel('Word')
        plt.tight_layout()
        plt.savefig(f'top_keywords_{sentiment}.png')
        print(f"Generated top_keywords_{sentiment}.png")


if __name__ == '__main__':
    # Replace 'twitter_training.csv' with the path to your file
    analyze_sentiment('twitter_training.csv')