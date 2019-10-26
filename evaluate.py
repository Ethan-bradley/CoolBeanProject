import datetime as dt


def get_start_day(time, day):
    if time.time() < dt.time(12):
        time = time - dt.timedelta(days=1)
    while time.weekday() != day:
        time = time - dt.timedelta(days=1)
    return dt.datetime(time.year, time.month, time.day, 12)


def evaluate(weeks, guessfunc, num_weeks):
    hours = []
    for week_index in range(len(weeks.weeks)):
        if week_index > num_weeks:
            for tweet_index in range(len(weeks.weeks[week_index].tweets)):
                tweet = weeks.weeks[week_index].get_tweet(tweet_index)
                guess = guessfunc(weeks, tweet.time - get_start_day(tweet.time, 2), tweet_index, num_weeks, week_index)
                correct = len(weeks.weeks[week_index].tweets)
                error = abs(guess - correct)
                print('-')
                print(week_index)
                print(guess, correct)
                print(round(error, 4))
