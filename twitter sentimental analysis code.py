import pandas as pd
import tweepy
import matplotlib.pyplot as plt
from textblob import TextBlob



# obtain these codes by register to the Twitter Developer platform
consumer_key= 'CONSUMER KEY'
consumer_secret= 'CONSUMER SECRET'

access_token= 'ACCESS TOKEN'
access_token_secret= 'ACCESS TOKEN SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets= api.search('Donald Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis= TextBlob(tweet.text)
    print(analysis.sentiment)
    if analysis.sentiment[0]>0:
        print('Positive')
    elif analysis.sentiment[0]<0:
        print('Negative')
    else:
        print('Neutral')





