from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

# không dùng được hàm tạo vs pydantic
# Pydantic Model for Book with a custom factory method
class Book(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: int

    # Custom factory method to mimic __init__ behavior
    @classmethod
    def create(cls, id: int, title: str, author: str, description: str, rating: int):
        return cls(id=id, title=title, author=author, description=description, rating=rating)


BOOKS = [
    Book.create(1, 'Computer Science Pro', 'codingwithroby', 'A very nice book!', 5),
    Book.create(2, 'Be Fast with FastAPI', 'codingwithroby', 'A great book!', 5),
    Book.create(3, 'Master Endpoints', 'codingwithroby', 'A awesome book!', 5),
    Book.create(4, 'HP1', 'Author 1', 'Book Description', 2),
    Book.create(5, 'HP2', 'Author 2', 'Book Description', 3),
    Book.create(6, 'HP3', 'Author 3', 'Book Description', 1)
]

@app.get('/books/all_book')
async def read_all_book():
    return BOOKS

# create book
@app.post('/books/create_book')
async def create(book: Book):
    BOOKS.append(book.model_dump())
    return {"message": "Book created successfully"}

