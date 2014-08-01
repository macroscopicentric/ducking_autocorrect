import filters
import tweepy
import os
import sys
import re
import time
import random

auth = tweepy.OAuthHandler(os.environ['consumer_key'], os.environ['consumer_secret'])
auth.set_access_token(os.environ['access_token_key'], os.environ['access_token_secret'])
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


def main():
    try:
        matching_tweets = api.search("fuck")
        tweet = matching_tweets[random.randrange(0,len(matching_tweets))]
        string_to_retweet = ('RT @' + tweet.author.screen_name + ' ' +
            tweet_formatting(tweet.text))
        #SFW filter: avoids some keywords, tweets with links, and tweets with media (ie, photos or videos) attached.
        #First condition ensures that 'fuck' isn't just in a username.
        while ('fuck' not in tweet.text.lower() or
            re.search(filters.swears, string_to_retweet,
                flags=re.I) or
            re.search(filters.politics, string_to_retweet,
                flags=re.I) or
            'media' in tweet.__dict__):
            main()
        print_tweet(string_to_retweet)
        api.update_status(string_to_retweet)
        time.sleep(3600)
    except tweepy.error.TweepError:
        pass

if __name__ == '__main__':
    while True:
        main()

