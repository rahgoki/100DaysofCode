import api

def main():
    keyword = input("Enter a search term: ")
    results = api.find_movie_by_title(keyword)

    print(f'\nThere are {len(results)} movies found.\n')

    for r in results:
        print(f"Title: {r.title} has score {r.imdb_score} and imdb code {r.imdb_code}")


if __name__ == '__main__':
    main()
