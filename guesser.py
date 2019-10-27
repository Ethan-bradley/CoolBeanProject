import tensorflow as tf
import pandas as pd
import numpy as np
import sys
print(sys.path)
sys.stdout.flush()

model = tf.keras.models.load_model('.model3.h5')


# Weeks is week in dataset. Time is days until end of week, tweets is number of tweets in that week
def guess(weeks, time, tweets):
    weeks = (weeks - 57.795247) / 26.644229
    time = (time - 3.531709) / 2.064484
    tweets = (tweets - 62.426499) / 51.817219
    df = pd.DataFrame.from_dict({'Days': [weeks], 'Time': [time], 'tweets': [tweets]})
    return model.predict(np.array(df))[0][0]
