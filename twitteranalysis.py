from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

import json


ckey='RxNvFrxQTnBA7f5QiU6g7aV21'
csecret='U8TabCRoKzHJqc8to8YurQ3JbRGnfSJVGpgMsFdfbqvutFkoOh'
atoken='825205434910908416-StkStLrSZWFuQYtrVxtRkgrUdDzl4hp'
asecret='YnhIIwFBdm1btdT8W4Y9imjY8Y4peHjGMWlWGBkOWlSPq'



class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data["text"]
        output = open("C://Users/Soumyadip Nandi/OneDrive/Documents/pickled_algos/twitter-out.txt","w")
        output.write(data)
        output.close()
        print(data)
        return True
    
    def on_error(self, status):
         print(status)

auth=OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream= Stream(auth,listener())

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["happy"])

