import tweepy
import time

CONSUMER_KEY = '#A'
CONSUMER_SECRET = '#'
ACCESS_KEY = '#'
ACCESS_SECRET = '#'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)



def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return



hashtag = "#christmas"
tweetnumber = 15

def reply_to_tweets():
    print('retrieving and replying to tweets...', flush=True)
    # DEV NOTE: use 1060651988453654528 for testing.
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    
    if len(tweet['entities']['hashtags']) > 0:
						hashtags = tweet['entities']['hashtags'][0]['text']
						TwitterAPI.bot_tweet(twitter_object_lookup,'#'+hashtags + ' '+ message)
						print "tweeted with message -> " , '#'+hashtags + ' '+ message

						TwitterAPI.bot_retweet(twitter_object_lookup,tweet['id'])
						print "retweeted the tweet_id -> " , tweet['id']


while True:
    reply_to_tweets()
    time.sleep(15)
            

