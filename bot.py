import credentials as cred
import tweepy
import sys
import re
import time
import random

auth = tweepy.OAuthHandler(cred.consumer_key, cred.consumer_secret)
auth.set_access_token(cred.access_token_key, cred.access_token_secret)
api = tweepy.API(auth)


def letter_replace(word):
    word = word.groups()[0]
    if word[0].isupper():
        word = 'D' + word[1:]
    else:
        word = 'd' + word[1:]
    return word

def tweet_formatting(tweet):
    return re.sub(r'(\bfuck\w*\b)', letter_replace, tweet, flags=re.I)

#Prints to console for debugging purposes. Formats to avoid emojis.
def print_tweet(text):
    return_string = ""
    for i in text:
        try:
            i.decode('ascii')
            return_string += i
        except:
            return_string += "_"
    print return_string 
            
def retweet(tweet):
    retweet_string = 'RT @' + tweet.author.screen_name + ' ' + tweet_formatting(tweet.text)
    api.update_status(retweet_string)
    print_tweet(retweet_string)

def main():
    try:
        matching_tweets = api.search("fuck")
        i = random.randrange(0,len(matching_tweets))
        retweet(matching_tweets[i])
        time.sleep(600)
    except tweepy.error.TweepError:
        pass

if __name__ == '__main__':
    while True:
        main()

