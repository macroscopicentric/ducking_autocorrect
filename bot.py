import credentials as cred
import tweepy
import re

auth = tweepy.OAuthHandler(cred.consumer_key, cred.consumer_secret)
auth.set_access_token(cred.access_token_key, cred.access_token_secret)
api = tweepy.API(auth)

#Step one: search Twitter for relevant tweets.

matching_tweets = api.search("fuck")
print "number of returned tweets", len(matching_tweets)

print matching_tweets[0].user

for tweet in matching_tweets:
    try:
       print "original tweet: " + tweet.text
       print "censored tweet: " +  tweet_formatting(tweet.text)
    except:
        print "strange characters in tweet preventing the text from printing"
    print "-------------------------------------\n\n\n"

#Step two: replace "fuck" with "duck."

test1 = 'I fucking hate autocorrect.'
test2 = 'Fuck you.'
test3 = 'FUcK YOU'

def letter_replace(word):
    word = word.groups()[0]
    if word[0].isupper():
        word = 'D' + word[1:]
    else:
        word = 'd' + word[1:]
    return word

def tweet_formatting(tweet):
    # new_word_list += re.sub(r'fuck', letter_replace, word, flags=re.I)
    tweet = re.sub(r'(\bfuck\w*\b)', letter_replace, tweet, flags=re.I)
    return tweet

print tweet_formatting(test1)
print tweet_formatting(test2)
print tweet_formatting(test3)

#Step three: RT.
def retweet(tweet):
    #Change from return to actual tweepy retweet method when we're done.
    return 'rt @' + tweet.screen_name + tweet_formatting(tweet.text)

