import requests
import collections
from typing import List

Movie = collections.namedtuple('Movie', 'imdb_code, title, director, keywords, '
                                        'duration, genres, rating, year, imdb_score')
# find_movie_by_title(keyword): works just fine
# by adding keyword: str and -> List[Movies] explicitly stating
# what we are doing, text editors give us additional help
# similar to functions...we get smart suggestions so we don't have to
# look it up or potential mistype an element!
def find_movie_by_title(keyword: str) -> List[Movie]:
    url = f'http://movie_service.talkpython.fm/api/search/{keyword}'

    resp = requests.get(url)
    resp.raise_for_status()

    results = resp.json()
    movies = []
    for r in results.get('hits'):
        movies.append(Movie(**r))

    return movies
