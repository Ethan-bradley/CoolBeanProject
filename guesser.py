def guess1(weeks, timedelta, tweets, num_weeks=-1, week=-1, bound=10):
    return weeks.get_av_len_matching(timedelta, tweets, bound, num_weeks, week)


def guess2(weeks, timedelta, tweets, num_weeks=-1, week=-1):
    return tweets + weeks.get_av_num_after(timedelta, num_weeks, week)

