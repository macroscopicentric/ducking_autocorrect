import credentials as cred
import tweepy
import sys

auth = tweepy.OAuthHandler(cred.consumer_key, cred.consumer_secret)
auth.set_access_token(cred.access_token_key, cred.access_token_secret)
api = tweepy.API(auth)

#Step one: replace "fuck" with "duck."
def word_replace(word):
    if 'Fuck' in word:
        word_remainder = word.split('Fuck')
        word = 'Duck' + word_remainder[1]
        return word
    elif 'fuck' in word:
        word_remainder = word.split('fuck')
        word = 'duck' + word_remainder[1]
        return word
    elif 'FUCK' in word:
        word_remainder = word.split('fuck')
        word = 'duck' + word_remainder[1]
        return word
    else:
        return word

def tweet_formatting(tweet):
    return ' '.join(map(word_replace, tweet.split(' ')))

#Step two: search Twitter for relevant tweets.

# make a method to check if the body of the tweet contains query string
# make a method to check if the body of the tweet can be printed

matching_tweets = api.search("fuck")

for tweet in matching_tweets:
    try:
       print "original tweet: " + tweet.text
       print "censored tweet: " +  tweet_formatting(tweet.text)
    except:
        print "strange characters in tweet preventing the text from printing"
    print "-------------------------------------\n\n\n"




#Step three: RT.
