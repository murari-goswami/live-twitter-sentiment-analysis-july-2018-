import tweepy
import csv
import pandas as pd
####input your credentials here


consumer_key='RxNvFrxQTnBA7f5QiU6g7aV21'
consumer_secret='U8TabCRoKzHJqc8to8YurQ3JbRGnfSJVGpgMsFdfbqvutFkoOh'
access_token='825205434910908416-StkStLrSZWFuQYtrVxtRkgrUdDzl4hp'
access_token_secret='YnhIIwFBdm1btdT8W4Y9imjY8Y4peHjGMWlWGBkOWlSPq'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('ua.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#unitedAIRLINES",count=100,
                           lang="en",
                           since="2017-04-03").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
