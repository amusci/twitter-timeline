import matplotlib
import matplotlib.pyplot as plt

import tweepy

from keys import keys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']
AT = keys['handle']
y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

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
    list_of_datetimes = []
    for status in api.user_timeline(AT):

        list_of_datetimes.append(str(status.created_at))  # time is in UTC

    for dates in list_of_datetimes:
        x = dates.split()[-1]
        print(x)



    # x = matplotlib.dates.date2num(list_of_datetimes)
    # plt.plot_date(x, y)
    # plt.tight_layout()
    # plt.show()


if __name__ == "__main__":


        gathering()
