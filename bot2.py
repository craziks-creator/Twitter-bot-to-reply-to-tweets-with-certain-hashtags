#!/usr/bin/env python
import tweepy, random, time
#from our keys module (keys.py), import the keys dictionary
from keys import keys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

file_name =("E:\\hopebot\\asc\last_seen_id.txt", "r")



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

 


def reply():
 twt = api.search("python",result_type="mixed",count=25) 
  for s in twt:
     print(s.id)
     sn = s.user.screen_name
     m = "@%s chup bsdk " % (sn)
     api.update_status(status=m, in_reply_to_status_id = s.id)
     store_last_seen_id(file_name, s.id)
      print("Done!!!")

while True:
    reply()
    time.sleep(20)




