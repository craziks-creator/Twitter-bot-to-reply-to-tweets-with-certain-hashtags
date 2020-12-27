#!/usr/bin/env python
import tweepy, random, time, logging
#from our keys module (keys.py), import the keys dictionary
from secrets import key

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

CONSUMER_KEY = key[0]
CONSUMER_SECRET = key[1]
ACCESS_TOKEN = key[2]
ACCESS_TOKEN_SECRET = key[3]

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

 
def reply():
    twt = api.search("python",result_type="mixed",count=5) 
    for s in twt:
        logging.info(f"Found tweet by {s.user.screen_name} mentioning searched keyword")
        if s.in_reply_to_status_id is not None or \
            s.user.id == api.me().id:
            logging.info("Not original tweet, but reply to a tweet...")    
            continue
        else:
            try:
                logging.info("Replying to tweet...")
                m = "@%s chup bsdk " % (s.user.screen_name)
                api.update_status(status=m, in_reply_to_status_id = s.id)
            except Exception as e:
                logging.error("Error on reply", exc_info=True)

while True:
    reply()
    time.sleep(20)




