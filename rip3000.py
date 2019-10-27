import tweepy
import auths
import csv
import datetime as dt

auth = tweepy.OAuthHandler(auths.consumer_key, auths.consumer_secret)
auth.set_access_token(auths.access_token, auths.access_token_secret)

api = tweepy.API(auth)

months = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10,
          'Nov': 11, 'Dec': 12}


def get_tweets(user):  # only gets 3000 tweets
    with open(user + '.csv', mode='w') as csv_file:
        tweet_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        tweet_writer.writerow(['date', 'id'])

        for tweet in tweepy.Cursor(api.user_timeline, id=user).items():
            json = tweet._json
            unconverted = json['created_at'].split(' ')
            hour = unconverted[3].split(':')
            time = dt.datetime(int(unconverted[-1]), int(months[unconverted[1]]),
                               int(unconverted[2]),
                               int(hour[0]), int(hour[1]), int(hour[2]))
            tweet_writer.writerow([time, json['id']])
    return user
