import credentials as cred
import tweepy

auth = tweepy.OAuthHandler(cred.consumer_key, cred.consumer_secret)
auth.set_access_token(cred.access_token_key, cred.access_token_secret)
api = tweepy.API(auth)

#Step one: search Twitter for relevant tweets.

#Step two: replace "fuck" with "duck."
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

#Step three: RT.

matching_tweets = api.search("fuck")
print "number of returned tweets", len(matching_tweets)


for tweet in matching_tweets:
    print tweet
    print "-------------------------------------\n\n\n"
