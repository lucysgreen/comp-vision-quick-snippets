# NLTK sentiment analysis, Lucy Green, 25/11/2021

import nltk
from nltk import sentiment
nltk.download(['vader_lexicon']) # VADER best for short pieces of text with slang
from nltk.sentiment import SentimentIntensityAnalyzer

# Analyse sentiment
def analyse_sentiment(text_to_analyse):
    # Analyse
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text_to_analyse)
    return sentiment

# # Text
# text_to_analyse = str("I love cats")

# sentiment = analyse_sentiment(text_to_analyse)

# print(text_to_analyse)
# print(sentiment)