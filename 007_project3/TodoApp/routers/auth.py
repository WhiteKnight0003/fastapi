'''
Cách sử dụng trong dự án thực tế:
Đoạn code này thể hiện một phương pháp tổ chức tốt trong FastAPI, nơi bạn:

Phân chia chức năng: Mỗi module riêng biệt (như auth, users, products...) có router riêng.
Dễ quản lý: Mỗi router có thể có prefix, tags và dependencies riêng.
Dễ mở rộng: Khi cần thêm tính năng mới, bạn chỉ cần tạo router mới mà không cần sửa đổi code hiện có.

Trong một ứng dụng thực tế, router auth sẽ chứa các endpoint như:

/auth/login để đăng nhập
/auth/register để đăng ký
/auth/logout để đăng xuất
/auth/reset-password để đặt lại mật khẩu
'''


# authentication & Authorization

from fastapi import APIRouter

router= APIRouter()

@router.get('/auth/')
async def get_user():
    return {'user':'authenticated'}

