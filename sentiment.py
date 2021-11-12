# Basic Sentiment Analysis
import nltk
from nltk import sentiment
from nltk.sentiment import SentimentIntensityAnalyzer

# TODO: Find a way of installing this offline.

nltk.download(['vader_lexicon']) # VADER best for short pieces of text with slang

# Initialise Sentiment Intensity Analyser as a global variable.
SIA = SentimentIntensityAnalyzer()

def analyse_sentiment_intensity(text_to_analyse="I love cats"):
    '''This function analyses the sentiment intensity of a given string and returns a polarity score.'''
    return SIA.polarity_scores(text_to_analyse)