# Day 14 - Python and APIs
# Open Library API: search for books by title, author or topic

import requests

SEARCH_URL = "https://openlibrary.org/search.json"

# Open Library asks apps to say who they are
HEADERS = {"User-Agent": "Book Finder (Student Project)"}


# Step 1: Fetch data from the API

def fetch_books(search_text, limit):
    params = {
        "q": search_text,
        "limit": limit,
        "fields": "key,title,author_name,first_publish_year,edition_count",
    }

    try:
        response = requests.get(SEARCH_URL, params=params, headers=HEADERS, timeout=30)

        print("Request URL:", response.url)
        print("Status code:", response.status_code)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 429:
            print("Too many requests. Please wait a moment and try again.")
        else:
            print("The API returned an error. Try again later.")

    except requests.exceptions.RequestException as error:
        print("Network problem:", error)

    return None


# Step 2: Explore the JSON structure

def show_structure(data):
    print("\nData type:", type(data).__name__)
    print("Keys in the response:", list(data.keys()))
    print("Type of data['docs']:", type(data["docs"]).__name__)
    if len(data["docs"]) > 0:
        print("Keys in the first book:", list(data["docs"][0].keys()))


# Step 3: Extract and display useful information

def show_books(data):
    books = data["docs"]

    print("\n==============================")
    print("Total books found:", data["numFound"])
    print("Books shown below:", len(books))
    print("==============================")

    number = 1
    for book in books:
        title = book.get("title", "Unknown title")
        authors = book.get("author_name", ["Unknown author"])
        year = book.get("first_publish_year", "Unknown")
        editions = book.get("edition_count", "Unknown")

        print("\nBook", number)
        print("  Title:", title)
        print("  Author(s):", ", ".join(authors[:3]))
        print("  First published:", year)
        print("  Editions:", editions)
        print("  Link: https://openlibrary.org" + book["key"])
        number = number + 1


# Main

def main():
    print("Book Finder (type 'quit' to stop)")

    while True:
        search_text = input("\nSearch for a book title, author or topic: ").strip()

        if search_text.lower() == "quit":
            print("Goodbye!")
            break
        if search_text == "":
            print("Please type something to search for.")
            continue

        try:
            limit = int(input("How many results do you want? (1-10): "))
        except ValueError:
            print("That was not a number, so I will show 5 results.")
            limit = 5
        if limit < 1 or limit > 10:
            print("Number out of range, so I will show 5 results.")
            limit = 5

        data = fetch_books(search_text, limit)

        if data is None:
            continue
        if data["numFound"] == 0:
            print("No books found for '" + search_text + "'. Try different words.")
            continue

        show_structure(data)
        show_books(data)


main()