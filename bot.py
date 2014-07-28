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

matching_tweets = api.search("fuck")

def print_tweet(text):
    return_string = ""
    for i in text:
        try:
            i.decode('ascii')
            return_string += i
        except:
            return_string += "_"
    print return_string 
            
for tweet in matching_tweets:
    print_tweet("original tweet: " + tweet.text)
    print_tweet( "censored tweet: " +  tweet_formatting(tweet.text))
    print_tweet( 'RT @' + tweet.author.screen_name + tweet_formatting(tweet.text))
    print "\n\n"
     
#Step three: RT.
def retweet(tweet):
    #Change from return to actual tweepy retweet method when we're done.
    return 'rt @' + tweet.author.screen_name + tweet_formatting(tweet.text)

print retweet(matching_tweets[0])



