'''method Get in fastapi is used to get data from the server''' 

''' POST Request Method
        - Used to create data
        - POST can have a body that has additional information that GET dose not have
'''

''' PUT method
        - used to update data
        - PUT can have a body that has additional information (like POST) that GET does not have
'''

''' DELETE Request Method
        - used to delete data
'''

'''
Body() là một dependency trong FastAPI, dùng để trích xuất dữ liệu từ body của request khi gửi POST/PUT/PATCH request.
'''


# để chạy được cần mở môi trường ảo ở terminal trên cmd

# di chuyển đến nơi cần đến để chạy và lấy ra đường dẫn web 
'''(.venv) PS F:\python\full-stack-web\fast-api> cd F:\python\full-stack-web\fast-api\004_setup_fastapi
(.venv) PS F:\python\full-stack-web\fast-api\004_setup_fastapi> uvicorn method_Get_http:app --reload


uvicorn your_file:app --reload
'''



# khi có đường đẫn , truy cập vào các mục để xem kết quả
# http://127.0.0.1:8000/api-endpoint/books

# xem thất cả các method trong fastapi mà bạn viết 
# http://127.0.0.1:8000/docs
from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
]


@app.get("/api-endpoint")
async def first_api():
    return {"message": "Hello World"}

@app.get("/api-endpoint/books")
async def get_books():
    return BOOKS

# @app.get('/books/{dynamic_param}')
# async def read_all_books(dynamic_param):
#     return {'dynamic_param': dynamic_param} #{"dynamic_param":"book1"}


# http://127.0.0.1:8000/book/Title%20Two
@app.get('/book/{book_title}')
async def read_book(book_title: str):
    for book in BOOKS:
        print(book)
        if book.get('title').casefold() == book_title.casefold(): # chuyeen ve lower
            return book


# http://127.0.0.1:8000/books/Author%20One/science
@app.get('/books/{author}/{category}')
async def read_books_by_author_and_category(author: str, category: str):
    result = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold() and book.get('category').casefold() == category.casefold():
            result.append(book)

    return result


# thêm vào
@app.post('/books/create_book')
async def create_book(new_book = Body()):
    BOOKS.append(new_book) # thêm sách vào danh sách sách



# update 
@app.put('/books/books_update')
async def update_book(update_book = Body()):
    for i in range(len(BOOKS)):
        if(BOOKS[i].get('title').casefold() == update_book.get('title').casefold()):
            BOOKS[i] = update_book


# delete data
@app.delete('/books/delete_book') 
async def delebook(book = Body()):
    for b in BOOKS:
        if(b.get('title').casefold() == book.get('title').casefold()):
            BOOKS.remove(b)
            break
 



'''
@app.get("/api-endpoint")

Dòng này là một decorator (bộ trang trí) được sử dụng để định nghĩa một endpoint API.
@app.get chỉ định rằng endpoint này sẽ xử lý các yêu cầu HTTP GET.
"/api-endpoint" là đường dẫn (URL path) của endpoint. Khi một yêu cầu GET được gửi đến đường dẫn này, hàm first_api sẽ được gọi.
'''