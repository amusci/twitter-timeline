import datetime
import random
import matplotlib.pyplot as plt
import numpy as np

import tweepy

from keys import keys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']
AT = keys['handle']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


class Error(Exception):
    pass


class Unverified(Error):
    pass

try:
    api.verify_credentials()
    print("on")
except Unverified:
    print("Error during authentication")


def gathering():
    plt.style.use('seaborn')
    list_of_date_times = []
    final = []
    tweet_ids = []

    for status in api.user_timeline(AT):
        # print(status.id)
        tweet_ids.append(str(status.id))
    for status in api.user_timeline(AT):
        list_of_date_times.append(str(status.created_at))  # time is in UTC

    for dates in list_of_date_times:
        times = dates.split()[-1]
        final.append(times)

    print(final)
    print(tweet_ids)
    plotting(final, tweet_ids)


def plotting(times, id):
    levels = np.tile([-5, -5, -5, -5, -5, -5], int(np.ceil(len(times) / 6)))[1]

    # Create figure and plot a stem plot with the times
    fig, ax = plt.subplots(figsize=(8.8, 5), constrained_layout=True)
    ax.set(title="Menace Activity")

    ax.vlines(times, 0, levels, color="tab:red")  # Stems
    ax.plot(times, np.zeros_like(times))  # Baseline

    plt.setp(ax.get_xticklabels(), rotation=30, ha="center")

    plt.show()


if __name__ == "__main__":
    gathering()
