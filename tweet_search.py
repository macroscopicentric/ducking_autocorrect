import json
import sys
import urllib2
import os

usage = """
Usage: ./tweet_search.py 'keyword'
e.g ./tweet_search.py pythonforbeginners

Use "+" to replace whitespace"
e.g ./tweet_search.py "python+for+beginners"
"""

# Check that the user puts in an argument, else print the usage variable, then quit.
if len(sys.argv)!=2:
    print (usage)
    sys.exit(0)

# The screen name in Twitter, is the screen name of the user for whom to return results for. 

# Set the screen name to the second argument
screen = sys.argv[1]
print screen

# Open the twitter search URL the result will be shown in json format
url_query = "https://api.twitter.com/1.1/search/tweets.json?q="+screen
print url_query

'''
url = urllib2.urlopen("https://api.twitter.com/1.1/search/tweets.json?q="+screen)

data = json.load(url)

print len(data), "tweets"

for tweet in data["results"]:
    print tweet["text"]

for status in data['results']:
    print "(%s) %s" % (status["created_at"], status["text"])
'''
