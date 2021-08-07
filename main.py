import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

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

try:
    api.verify_credentials()
    print("on")
except:
    print("Error during authentication")


def gathering():
    plt.style.use('seaborn')
    list_of_date_times = []
    times = None
    for status in api.user_timeline(AT):
        list_of_date_times.append(str(status.created_at))  # time is in UTC
        for dates in list_of_date_times:
            times = dates.split()[-1]
        plotting(times)


def plotting(times):
    # x =
    # y =

    # plot
    plt.plot([], [])
    plt.scatter(x, y)

    # beautify the x-labels
    plt.gcf().autofmt_xdate()
    myFmt = mdates.DateFormatter('%H:%M')
    plt.gca().xaxis.set_major_formatter(myFmt)

    plt.show()
    plt.close()



if __name__ == "__main__":
    gathering()
