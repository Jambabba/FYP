# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tweepy
import pandas as pd

consumer_key = "x1kSWSU0duVWpmeX3V6v7JXw9"
consumer_secret = "pAxLEOqIPyop68hptwRjUaWzqLLQmnhL5S0KSFezTpwytoO7PC"
access_key = "947517242891149318-4kxhY6WRXX6cFZpidqrmIbsdDBGs9Jn"
access_secret = "mZaKpzxWqHYODZ0dk2Wkn1Sea7zLcWJXJeTFICMyzS7wI"

def twitter_setup():
    
    #Autentication and access using keys
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)    
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth, wait_on_rate_limit = True)
                     
    try:
        api.verify_credentials()
        print('Authentication OK')
    except:
        print('Error During Authentication')
        
    return api

# Create extractor object (hold api data) by calling in our twitter_setup() function
extractor = twitter_setup()

def get_user_tweets(api, username):
    tweets = []
    for status in tweepy.Cursor(api.user_timeline, screen_name=username).items():
        tweets.append(status)
        
    return tweets

def keyword_tweets(api, keyword, number_of_tweets):
    new_keyword = keyword + " -filter:retweets"
    
    tweets = []
    for status in tweepy.Cursor(api.search_tweets, q=new_keyword, lang='en').items(number_of_tweets):
        tweets.append(status)
        
    return tweets


keyword_alltweets = keyword_tweets(extractor, 'ccp', 5000)

print('5 recent tweet: \n')
for tweet in keyword_alltweets[:5]:
    print(tweet.text)
    
# Create a pandas DataFrame by looping through each element and add into the DataFrame
data = pd.DataFrame(data=[tweet.text for tweet in keyword_alltweets], columns=['Tweets'])

data['Date'] = [tweet.created_at for tweet in keyword_alltweets]
data['Likes'] = [tweet.favorite_count for tweet in keyword_alltweets]
data['RTs'] = [tweet.retweet_count for tweet in keyword_alltweets]
data['Likes'] = [tweet.favorite for tweet in keyword_alltweets]
tt=[]
for tweet in keyword_alltweets[:5]:
    tt.append(tweet.favorite)

data.to_csv('C:/Users/user/Downloads/ccp.csv')