import twitterapi as ta

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

#Step one: search Twitter for relevant tweets.
test_string1 = 'I fucking hate autocorrect.'
test_string2 = 'Fuck that.'

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
    else:
        return word

def tweet_formatting(tweet):
    return ' '.join(map(word_replace, tweet.split(' ')))

print tweet_formatting(test_string1)
print tweet_formatting(test_string2)

#Step three: RT.