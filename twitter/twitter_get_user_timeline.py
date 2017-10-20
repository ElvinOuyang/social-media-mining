import json
from sys import argv
from tweepy import Cursor
from twitter_client import get_twitter_client

if __name__ == '__main__':
    client = get_twitter_client()
    script, user = argv
    fname = "user_timeline_{}.jsonl".format(user)

    # retrieve up to 200 statuses per page for 16 pages of specified timeline
    with open(fname, 'w') as f:
        for page in Cursor(client.home_timeline, count=200).pages(16):
            for status in page:
                f.write(json.dumps(status._json)+"\n")
