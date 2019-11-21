import tweepy
import csv
import time
from settings import twitter_auth

auth = tweepy.OAuthHandler(twitter_auth['consumer_key'],
                           twitter_auth['consumer_secret'])
auth.set_access_token(twitter_auth['access_token'],
                      twitter_auth['access_token_secret'])

api = tweepy.API(auth,
                 retry_count=2,
                 retry_delay=30,
                 wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)

with open('tweets2.csv', mode='a') as tweet_file:
    writer = csv.writer(tweet_file)
    writer.writerow([
        'Tweet ID', 'Tweet Created at', 'Retweeted ID', 'User ID', 'Username',
        'User Location', 'User Created at', 'Default Profile',
        'Default Profile Image', '#Tweets'
    ])

    started_at = time.time()
    for tweet in tweepy.Cursor(api.search, q='#PautaLogoAlcolumbre').items(5):
        user = tweet.user
        try:
            retweet_id = tweet.retweeted_status.id_str
        except (AttributeError):
            retweet_id = None
        data = [
            tweet.id_str, tweet.created_at, retweet_id, user.id_str,
            user.screen_name, user.location, user.created_at,
            user.default_profile, user.default_profile_image,
            user.statuses_count
        ]
        writer.writerow(data)

ended_at = time.time()
print("Execution finished successfully! I took {:.2f}s to execute.".format(
    ended_at - started_at))
