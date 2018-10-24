import requests
import feedparser

url = 'http://feeds.arstechnica.com/arstechnica/technology-lab'

# in the tutorial 'wb' was specified for the mode to use with open
# 'b' specifies binary mode and does nothing on a unix machine
r = requests.get(url)
with open('feed.xml', 'w') as f:
    f.write(r.content)

feed_file = 'feed.xml'

feed = feedparser.parse(feed_file)

# what elements are available?
for element in feed.entries[0]:
    print(element)

if 'title' in feed.entries[0]:
    for entry in feed.entries:
        print(f'{entry.title}: {entry.summary}')


