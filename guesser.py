import tensorflow as tf
import pandas as pd
import numpy as np

model = tf.keras.models.load_model('model2.h5')

def guess(days, time, tweets):
    days = (days - 407.633877) / 186.525372
    time = (time - 3.531709) / 2.064484
    tweets = (tweets - 62.426499) / 51.817219
    df = pd.DataFrame.from_dict({'Days': [days], 'Time': [time], 'tweets': [tweets]})
    print(model.predict(np.array(df)))
    