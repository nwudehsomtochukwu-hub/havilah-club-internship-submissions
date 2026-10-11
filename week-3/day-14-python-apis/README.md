# Day 14 - Python and APIs: Book Finder

A small Python program that searches for books using the **Open Library API** and prints the results in a clear, readable format.

## The API I chose

- **Name:** Open Library API (Search API), run by the Internet Archive
- **Documentation:** https://openlibrary.org/dev/docs/api/search
- **Found on:** PublicAPIs.io: https://publicapis.io/open-library-api-api
- **Why I chose it:** It is free, needs no API key, and returns JSON from a simple GET request. It also accepts several query parameters, and its response has a list of dictionaries, which is good practice for loops and dictionary access. A book search is also useful for a student.

## API details

| Item | Details |
|---|---|
| Method | GET |
| Endpoint | `https://openlibrary.org/search.json` |
| Authentication | None required, so no `.env` file is needed for this project |
| Response format | JSON |

### Parameters used

| Parameter | Meaning | Example |
|---|---|---|
| `q` | The search text (a title, author, or topic) | `q=the hobbit` |
| `limit` | How many books to return | `limit=5` |
| `fields` | Which details to return for each book | `fields=key,title,author_name,first_publish_year,edition_count` |

Example request URL:
`https://openlibrary.org/search.json?q=the+hobbit&limit=5&fields=key,title,author_name,first_publish_year,edition_count`

The program also sends a `User-Agent` header, because Open Library asks applications to identify themselves.

## Structure of the JSON response

The response is a **dictionary** with these keys:

- `numFound`: the total number of books that match the search
- `start`: the position of the first result
- `docs`: a **list** of dictionaries, one for each book. Each book can have:
  - `key`: the book's page on Open Library, such as `/works/...`
  - `title`: the book title
  - `author_name`: a list of author names
  - `first_publish_year`: the year it was first published
  - `edition_count`: how many editions exist

Some books are missing some of these keys, so the program uses `.get()` with a default value instead of reading the key directly.

## What the program does

1. Asks the user for a book title, author, or topic (type `quit` to stop).
2. Asks how many results to show (1 to 10). If the input is not a valid number, it uses 5.
3. Sends a GET request with `requests.get()`, using the `params` argument for `q`, `limit`, and `fields`.
4. Prints the request URL (`response.url`) and the status code (`response.status_code`).
5. Converts the response with `.json()` and prints its structure (type, keys, and the type of `docs`).
6. Loops through the list of books and prints the useful information in a labelled format.
7. Lets the user search again until they type `quit`.

## Information the program extracts

- Total number of matching books (`numFound`)
- Title of each book
- Author name(s), showing up to three
- Year first published
- Number of editions
- A link to the book's page on Open Library

## Error handling

- `try` / `except requests.exceptions.RequestException` handles network problems, such as no internet connection or a timeout.
- `response.status_code` is checked: `200` means success, `429` means too many requests, and any other code shows a general error message.
- If the search finds no books, the program shows a message instead of an empty report.
- Empty input is rejected, and a limit that is not a number (caught with `ValueError`) falls back to 5.

## How to run

```bash
# 1. Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # macOS / Linux

# 2. Install requests
python -m pip install requests

# 3. Run the program
python main.py
```

The `.venv` folder is not pushed to GitHub.

## Testing

I tested the program by changing the search text and the `limit` parameter. Searches I tried: (write the searches you actually ran here, for example a book title, an author name, and a nonsense word like `zzzzqqq` to check the "no books found" message).

## Output screenshot

(Add your screenshot of the program running here.)
