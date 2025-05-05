# test  client
from fastapi.testclient import TestClient 
from ..main import app 
from fastapi import status

client = TestClient(app)

# sau khi chỉnh đường dẫn gõ 2 lệnh vào  cmd :   
#  uvicorn TodoAppMySQL.main:app --reload
#  pytest --disable-warnings

# Nó đúng khi tôi mở từ folder   010-PROJECT4_TESTING

# nếu lỗi thư mục hãy đảm bảo Tạo file __init__.py để đánh dấu các thư mục là package
def test_return_health_check():
    response = client.get('/healthy')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'status': 'healthy'}