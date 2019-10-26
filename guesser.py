def guess(weeks, timedelta, tweets, num_weeks=-1, week=-1):
    return tweets + weeks.get_av_num_after(timedelta, num_weeks, week)
