import tweepy
import time
consumer_key = ""
consumer_secret = ""
key = ""
secret = ""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)
search = "message"   # <== this can be in a tuple
for rt in tweepy.Cursor(api.search, search).items(10):
    try:
        rt.retweet()
        print("retweet successful")
        time.sleep(2)
    except tweepy.TweepError as e:
        print(e.reason)
        time.sleep(2)
    except StopIteration:
        break   # breaking loop in order to run the rest of the code
