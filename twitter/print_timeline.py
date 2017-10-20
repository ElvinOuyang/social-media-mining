from tweepy import Cursor
from sys import argv
from twitter_client import get_twitter_client

script, count = argv
count = int(count)

if __name__ == '__main__':
    client = get_twitter_client()

# tweepy.Cursor is an auto pagination object
# Cursor has methods .items() and .pages(), which lists each status or page
# as element
    for i, status in enumerate(Cursor(client.home_timeline).items(count)):
        # Process a single status
        print("%d $$$ %s" % (i + 1, status.text))
