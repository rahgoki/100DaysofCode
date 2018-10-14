import api
import webbrowser

'''
This is only 1 way to use the API.  Aside from search strings
we could search by place_id, lat/long, category or request directions.
'''

def main():
    print('******** Simple Google Map Search *********')
    keyword = input("Enter a search term: ")
    results = api.open_map_by_keyword(keyword)

    webbrowser.open_new(results)



if __name__ == '__main__':
    main()
