# Basic Sentiment Analysis

import nltk
from nltk import sentiment
nltk.download(['vader_lexicon']) # VADER best for short pieces of text with slang
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()
text_to_analyse = str("I love cats")
sentiment = sia.polarity_scores(text_to_analyse)
print(text_to_analyse)
print(sentiment)