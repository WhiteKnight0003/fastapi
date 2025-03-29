# để chạy được cần mở môi trường ảo ở terminal trên cmd
'''.venv\Scripts\activate'''
# tắt môi trg ảo 
'''deactivate'''

# di chuyển đến nơi cần đến để chạy và lấy ra đường dẫn web 
'''(.venv) PS F:\python\full-stack-web\fast-api> cd F:\python\full-stack-web\fast-api\004_setup_fastapi
(.venv) PS F:\python\full-stack-web\fast-api\004_setup_fastapi> uvicorn method_Get_http:app --reload'''

# khi có đường đẫn , truy cập vào các mục để xem kết quả
# http://127.0.0.1:8000/api-endpoint/books

# xem thất cả các method trong fastapi mà bạn viết 
# http://127.0.0.1:8000/docs