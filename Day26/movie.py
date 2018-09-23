#import csv
from urllib.request import urlretrieve
import urllib.error

# where our data is stored
data_url = 'https://aw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv'

# what will we name our file?
file_name = 'movies.csv'

try:

    # download the data
    urlretrieve(data_url, file_name)


except urllib.error.URLError:
    print("URLerror")

except Exception as e:
    print(e)
