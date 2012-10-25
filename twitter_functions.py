import twitter
import util
import pdb

BOSTON_WOEID = 2367105

def search(searchTerm):
    """
    Print recent tweets containing `searchTerm`.

    To test this function, at the command line run:
        python twitter_api.py --search=<search term>
    For example,
        python twitter_api.py --search=python
    """
    api = twitter.Api()
    tweets = api.GetSearch(searchTerm)
    for tweet in tweets:
        util.safe_print(tweet.GetText())

def trendingTopics():
    """
    Print the currently trending topics.

    To test this function, at the command line run:
        python twitter_api.py -t
    """
    api = twitter.Api()

    trending_topics = api.GetTrendsWoeid(BOSTON_WOEID)
    for topic in trending_topics:
        util.safe_print(topic.name)

def userTweets(username):
    """
    Print recent tweets by `username`.

    You may find the twitter.Api() function GetUserTimeline() helpful.

    To test this function, at the command line run:
        python twitter_api.py -u <username>
    For example,
        python twitter_api.py -u bostonpython
    """
    api = twitter.Api()

    user_tweets = api.GetUserTimeline(username)
    for tweet in user_tweets:
        util.safe_print(tweet.GetText())

def trendingTweets():
    """
    Print tweets for all the trending topics.

    To test this function, at the command line run:
        python twitter_api.py -w
    """
    api = twitter.Api()

    trending_topics = api.GetTrendsWoeid(BOSTON_WOEID)
    for topic in trending_topics:
        topic_name = topic.name.encode('ascii', 'ignore')
        get_tweets = api.GetSearch(topic.name)
        util.safe_print(topic.name)
        for tweet in get_tweets:
            util.safe_print(tweet.GetText())



