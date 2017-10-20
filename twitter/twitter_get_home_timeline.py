import json
from tweepy import Cursor
from twitter_client import get_twitter_client

if __name__ == '__main__':
    client = get_twitter_client()

# retrieve up to 200 statuses per page for 4 pages of recent timeline
with open('home_timeline.jsonl', 'w') as f:
    for page in Cursor(client.home_timeline, count=200).pages(4):
        for status in page:
            f.write(json.dumps(status._json)+"\n")
