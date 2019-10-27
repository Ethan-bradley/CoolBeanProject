import tensorflow as tf
import pandas as pd
import numpy as np
from rip3000 import get_tweets
import datetime as dt
from datetime import timedelta
from main.py import *

model = tf.keras.models.load_model('model3.h5')
#Weeks is week in dataset. Time is days until end of week, tweets is number of tweets in that week
def guess(weeks, time, tweets):
    weeks = (weeks - 57.795247) / 26.644229
    time = (time - 3.531709) / 2.064484
    tweets = (tweets - 62.426499) / 51.817219
    df = pd.DataFrame.from_dict({'Days': [weeks], 'Time': [time], 'tweets': [tweets]})
    return model.predict(np.array(df))[0][0]

def guess2(user):
    tweets = get_tweets(user)
    dt2 = dt.datetime.now()
    start = dt2 - timedelta(days=dt2.weekday())
    end = start + timedelta(days=6)
    numberInWeek = tweets

def trumpGuess():
    dt2 = dt.datetime.now()
    start = dt2 - timedelta(days=dt2.weekday())
    end = start + timedelta(days=6)
    diff = end-dt2
    get_tweets("realDonaldTrump")
    everything = csv_to_weeks('realDonaldTrump.csv')
    NumberThisWeek = everything.get_week(-1).get_num_tweets()
    return guess(40,diff,NumberThisWeek)