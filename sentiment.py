import streamlit as st
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')
st.title('Sentiment Analysis App')

st.write('Developed by Crucifier')

st.write('Created with the help of NLTK Library')
st.write('***')
text=st.text_input('Enter a text')
result=SentimentIntensityAnalyzer().polarity_scores(text)
st.title('Output')
st.write(result)
if result['neg'] != 0:
	st.write('Negative')
else:
	st.write('Positive')
