from typing import Optional
from fastapi import FastAPI, Body, Path , Query , HTTPException
from pydantic import BaseModel, Field
from starlette import status

'''
- Trong Pydantic, Field được sử dụng để cung cấp các ràng buộc bổ sung, giá trị mặc định và metadata cho các trường trong mô hình (BaseModel). 
Nó tương tự như Column trong SQLAlchemy hoặc validators trong các thư viện khác.

- Optional[int] trong Python là một kiểu dữ liệu từ module typing được sử dụng để chỉ ra rằng một biến có thể có kiểu dữ liệu int 
hoặc có giá trị None. Đây là một cách để khai báo kiểu dữ liệu cho các biến có thể không có giá trị (tùy chọn).

- Path trong FastAPI được sử dụng để xác thực và kiểm tra các tham số đường dẫn (path parameters)

- Query trong FastAPI được sử dụng để xác thực và kiểm tra các tham số truy vấn (query parameters)

- # ví dụ ở đây {book_id} là tham số đường dẫn 
@app.delete('/books/delete/{book_id}')

- cái này là tham số truy vấn
 @app.get('/books/find_rating/rate')
async def rating_book(book_rating: int =   Query(gt=0, lt=6)):

- HTTPException trong FastAPI là một lớp (class) đặc biệt được sử dụng để phát sinh các ngoại lệ HTTP có kiểm soát. 
Nó cho phép bạn dừng quá trình xử lý yêu cầu và trả về phản hồi lỗi với status code và message tùy chỉnh.
'''


'''
Status code trong FastAPI là các mã số HTTP được sử dụng để chỉ định kết quả của một yêu cầu. FastAPI cho phép bạn kiểm soát các status code này một cách dễ dàng.
Một số status code phổ biến trong FastAPI:

200 OK: Yêu cầu thành công (mặc định cho các phương thức GET)
201 Created: Tài nguyên đã được tạo thành công (thường dùng cho POST)
204 No Content: Yêu cầu thành công nhưng không có nội dung trả về
400 Bad Request: Yêu cầu không hợp lệ
401 Unauthorized: Cần xác thực
403 Forbidden: Không có quyền truy cập
404 Not Found: Không tìm thấy tài nguyên
422 Unprocessable Entity: Dữ liệu đầu vào không hợp lệ (FastAPI tự động trả về khi xác thực thất bại)
500 Internal Server Error: Lỗi máy chủ
'''


app = FastAPI()

# không dùng được hàm tạo vs pydantic
# Pydantic Model for Book with a custom factory method
class Book():
    id: int
    title: str 
    author: str
    description: str
    rating: int
    publish_date : int

    def __init__(self, id: int, title: str, author: str, description: str, rating: int, publish_date : int):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.publish_date = publish_date


# Pydantic Model for BookRequest
# min_length is length minimum 
# max_length is length maximum
class BookRequest(BaseModel):
    id: Optional[int] = Field(title= 'id is not needed')
    title: str = Field(min_length=3) # Field : đặt điều kiện cho biến 
    author: str = Field(min_length= 1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt= 0 , lt=6)
    publish_date : int = Field(title='choose date', gt = 1900, lt = 2033)
    '''
        gt=0 (greater than 0) → rating phải lớn hơn 0, nghĩa là rating ≥ 0.
        lt=6 (less than 6) → rating phải nhỏ hơn 6, nghĩa là rating ≤ 5.
    '''


    # create json_schema_extra with pydantic 2
    class Config:
        json_schema_extra = {
            'example': {
                'title': 'A new book',
                'author': 'codingwithroby',
                'description': 'A new description',
                'rating': 5 ,
                'publish_date' : 2029
            }
        }

BOOKS = [
    Book(1, 'Computer Science Pro', 'codingwithroby', 'A very nice book!', 5, 2030),
    Book(2, 'Be Fast with FastAPI', 'codingwithroby', 'A great book!', 5, 2031),
    Book(3, 'Master Endpoints', 'codingwithroby', 'A awesome book!', 5, 2030),
    Book(4, 'HP1', 'Author 1', 'Book Description', 2, 2023),
    Book(5, 'HP2', 'Author 2', 'Book Description', 3 , 2021),
    Book(6, 'HP3', 'Author 3', 'Book Description', 1, 2024)
]

@app.get('/books/all_book', status_code=status.HTTP_200_OK)
async def read_all_book():
    return BOOKS


# create book
# default example value : {"id": 0, "title": "string",  "author": "string", "description": "string", "rating": 0 }
@app.post('/books/create_book', status_code=status.HTTP_201_CREATED)
async def create(book: BookRequest):
    new_book = Book(**book.model_dump()) 
    # nếu k có ** thì nó chuyển đối tượng thành các dict tương ứng
    # nếu có ** , nó phân rã đối tượng về dạng các đối số riêng lẻ như hàm tạo
    BOOKS.append(find_book_id(new_book))
    # BOOKS.append(book.model_dump())
    

'''với path =0 , nếu ID là 0 hoặc số âm như /books/find_id/-1, 
FastAPI sẽ tự động trả về lỗi 422 Unprocessable Entity mà không cần bạn phải viết code kiểm tra thêm.'''
@app.get('/books/find_id/{find_id}' , status_code=status.HTTP_200_OK)
async def find_book_by_id(find_id: int = Path(gt=0)):
    for b in BOOKS:
        if(b.id == find_id):
            return b
    raise HTTPException(status_code=404, detail='Item not found')
# khi bạn sử dụng raise HTTPException(status_code=404, detail='Item not found'), bạn đang tự định nghĩa lỗi cho ứng dụng của mình

def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) ==0 else BOOKS[-1].id +1
    return book


# find rating book
@app.get('/books/find_rating/{book_rating}' , status_code=status.HTTP_200_OK)
async def rating_book(book_rating: int):
    books_to_return = []
    for b in BOOKS:
        if(b.rating == book_rating):
            books_to_return.append(b)
    return books_to_return

# find rating book
@app.get('/books/find_rating/rate')
async def rating_book(book_rating: int =   Query(gt=0, lt=6)):
    books_to_return = []
    for b in BOOKS:
        if(b.rating == book_rating):
            books_to_return.append(b)
    return books_to_return

# find publish book
@app.get('/books/find_publish/{book_publish}')
async def rating_book(book_publish: int = Path(gt=0)):
    books_to_return = []
    for b in BOOKS:
        if(b.publish_date == book_publish):
            books_to_return.append(b)
    return books_to_return

# update book
@app.put('/books/update_book' , status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    for i in range(len(BOOKS)):
        if(BOOKS[i].id == book.id):
            BOOKS[i] = book
            break
    raise HTTPException(status_code=404, detail='Item not found')
            
# delete book
# update book
# ví dụ ở đây {book_id} là tham số đường dẫn 
@app.delete('/books/delete/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def dele_book(book_id : int = Path(gt=0)):
    for i in range(len(BOOKS)):
        if(BOOKS[i].id == book_id):
           BOOKS.pop(i)
           break
         #  BOOKS.remove(BOOKS[i])
            



