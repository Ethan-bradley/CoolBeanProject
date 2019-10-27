import datetime as dt


def get_start_day(time, day):
    if time.time() < dt.time(12):
        time = time - dt.timedelta(days=1)
    while time.weekday() != day:
        time = time - dt.timedelta(days=1)
    return dt.datetime(time.year, time.month, time.day, 12)


def evaluate(weeks, guessfunc, num_weeks=-1):
    hours = {i: [0, 0] for i in range(7)}
    for week_index in range(len(weeks.weeks)):
        if week_index > num_weeks:
            for tweet_index in range(len(weeks.weeks[week_index].tweets)):
                tweet = weeks.get_week(week_index).get_tweet(tweet_index)
                guess = guessfunc(week_index, (weeks.get_week(week_index).end - tweet.time).total_seconds()/86400, tweet_index)
                correct = len(weeks.get_week(week_index).tweets)
                error = abs(guess - correct)
                print(error)
                hours[(weeks.get_week(week_index).end - tweet.time).days][0] += error
                hours[(weeks.get_week(week_index).end - tweet.time).days][1] += 1
    for i in range(7):
        hours[i][0] /= hours[i][1]
    print(hours)
