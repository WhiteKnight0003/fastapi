from fastapi import FastAPI, Body

app = FastAPI()



BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author One', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
]


@app.get('/books/{author_name}')
async def all_book_author(author_name : str):
    res = []
    for book in BOOKS:
        if book.get('author').casefold() == author_name.casefold():
            res.append(book)
    return res

