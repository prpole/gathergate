import tweepy
import cPickle as pickle

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'BvkxtoSU9qNK4s3nncattaRZM'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'uZLIQ6C0PmMGwLHuO5mIhlFUMKeoTUHBmsfnqLKEviKwazsKVw'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '615528592-FuZIIFycOEmyNaEUtSMXpJ5iyPZSEqK5Oz4I7GoN'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'Ospy8ZPsgNPkUWhbuG8DsjNVfLwZZXYG1RjKSYD7Ob9Eh'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True)
'''
with open('oct_tweets.p','r') as f:
    tweet_list = pickle.load(f)
'''
with open('latest_tweet.txt','r') as f:
    status_start = pickle.load(f) 

tweet_list = []

start = status_start[0]
start_id = status_start[1]

#load pickled csv file
with open('tweet_ids.p','r') as f:
    tweet_ids = pickle.load(f)

while start < 316569:
    
    new_ids = tweet_ids[start+1:start+101]

    result = api.statuses_lookup(new_ids)
    
    for row in result:
        print start
        tweet_list.append(result)
        pickle.dump(tweet_list,open('oct_tweets.p','w')) 
        pickle.dump([start,row],open('latest_tweet.txt','w'))
        start += 1
