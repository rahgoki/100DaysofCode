from blog_client import BlogClient

def main():
    val = 'RUN'


    while val:
        print("What would you like to do next?")
        val = input('[w]rite a post, [r]ead a post or [q]uit? ')

        if val == 'w':
            write_post()
        elif val == 'r':
            read_post() 
        elif val == 'q':
            break


def write_post():
    pass

def read_post():
    svc = BlogClient()
    response = svc.all_entries()
    response.raise_for_status()

    posts = response.json()
    for idx, p in enumerate(posts, 1):
        print(f" {idx}. [{p.get('view_count')} views] {p.get('title')}")

    print(type(response), response) 
    selected = int(input("Which number do you want to view? "))

    selected_id = posts[selected-1].get('id')

    response = svc.entry_by_id(selected_id)
    response.raise_for_status()

    selected_post = response.json()
    print(f"Details for selected_post: {selected_post.get('id')}")
    print(f"Title: {selected_post.get('title')}")
    print(f"Written: {selected_post.get('published')}")
    print(f"Content: {selected_post.get('content')}")
    print()
    print()

if __name__ == "__main__":
    main()
