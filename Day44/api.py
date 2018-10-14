
def open_map_by_keyword(keyword):

    searchList = keyword.split()

    urlKeyword = create_search_string(searchList)
    # it's lazy, but the spaces are implied as + rather than explicitly stated
    url = f'https://www.google.com/maps/search/?api=1&query={urlKeyword}'


    print(url)
    return url

def create_search_string(searchList):
    searchString = ""

    # leaves trailing + 
    for term in searchList:
        searchString += term
        searchString += '+'

    # lazy way to remove last '+'
    searchString = searchString[:-1]

    return searchString
