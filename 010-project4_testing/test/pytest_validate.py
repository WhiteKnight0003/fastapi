import pytest
# chỉ cần gõ pytest vào cmd , nó tự chạy 
# có thể nó có nhiều trường để test , chỉ cần 1 cái sai là sai hết 

# Validate giá trị đơn giản
def test_basic_values():
    # Kiểm tra bằng nhau
    assert 5 == 5
    
    # Kiểm tra không bằng nhau
    assert 5 != 10
    
    # Kiểm tra lớn hơn/nhỏ hơn
    assert 10 > 5
    assert 5 < 10
    assert 10 >= 10
    assert 5 <= 5
    
    # Kiểm tra boolean
    assert True
    assert not False


# Validate kiểu dữ liệu và instances
def test_type_validation():
    # Kiểm tra kiểu dữ liệu với isinstance
    assert isinstance("hello", str)
    assert isinstance(42, int)
    assert isinstance(3.14, float)
    assert isinstance([1, 2, 3], list)
    assert isinstance({"key": "value"}, dict)
    
    # Kiểm tra không phải kiểu dữ liệu
    assert not isinstance("10", int)
    assert not isinstance(42, str)
    
    # Kiểm tra kiểu trực tiếp
    assert type("hello") is str
    assert type(42) is int


# Validate chuỗi
def test_string_validation():
    # Kiểm tra chuỗi con
    assert "world" in "hello world"
    assert "xyz" not in "hello world"
    
    # Kiểm tra bắt đầu và kết thúc
    assert "hello world".startswith("hello")
    assert "hello world".endswith("world")
    
    # Kiểm tra độ dài
    assert len("hello") == 5
    
    # Kiểm tra chuỗi rỗng
    assert "" == ""
    assert not "hello"  # Sai - chuỗi không rỗng nên là True
    assert bool("")  # Sai - chuỗi rỗng là False


# Validate collections
def test_list_validation():
    my_list = [1, 2, 3, 4, 5]
    
    # Kiểm tra phần tử trong danh sách
    assert 3 in my_list
    assert 10 not in my_list
    
    # Kiểm tra độ dài
    assert len(my_list) == 5
    
    # Kiểm tra phần tử tại vị trí
    assert my_list[0] == 1
    assert my_list[-1] == 5
    
    # So sánh toàn bộ danh sách
    assert my_list == [1, 2, 3, 4, 5]
    assert my_list != [5, 4, 3, 2, 1]

def test_dict_validation():
    my_dict = {"name": "Alice", "age": 30}
    
    # Kiểm tra key tồn tại
    assert "name" in my_dict
    assert "email" not in my_dict
    
    # Kiểm tra giá trị
    assert my_dict["name"] == "Alice"
    assert my_dict.get("age") == 30
    assert my_dict.get("email", "not found") == "not found"
    
    # So sánh toàn bộ dict
    assert my_dict == {"name": "Alice", "age": 30}


# Validate với toán tử logic
def test_logical_operators():
    x, y = 5, 10
    
    # AND logic
    assert x > 0 and y > 0
    
    # OR logic
    assert x > 10 or y > 5
    
    # Kết hợp
    assert (x < 10 and y > 5) or x == y


# Validate ngoại lệ
def test_exceptions():
    # Kiểm tra ngoại lệ được raise
    with pytest.raises(ZeroDivisionError):
        1 / 0
    
    # Kiểm tra nội dung ngoại lệ
    with pytest.raises(ValueError) as excinfo:
        int("xyz")
    assert "invalid literal" in str(excinfo.value)
    
    # Kiểm tra một hàm có thể raise ngoại lệ
    with pytest.raises(KeyError):
        my_dict = {}
        my_dict["non_existent_key"]


# Validate đối tượng tùy chỉnh
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def test_custom_objects():
    person = Person("Alice", 30)
    
    # Kiểm tra thuộc tính
    assert person.name == "Alice", 'Name is Alice'
    assert person.age == 30
    
    # Kiểm tra kiểu đối tượng
    assert isinstance(person, Person)
    
    # Kiểm tra thuộc tính tồn tại
    assert hasattr(person, "name")
    assert not hasattr(person, "email")


# Validate approximation (giá trị xấp xỉ)
def test_approximation():
    # Kiểm tra giá trị gần đúng (hữu ích cho số thực)
    assert pytest.approx(0.1 + 0.2) == 0.3
    
    # Với dung sai cụ thể
    assert 5.0 == pytest.approx(5.1, abs=0.2)
    assert 5.0 == pytest.approx(5.1, rel=0.05)  # 5% difference allowed


# Validate với fixtures
@pytest.fixture
def sample_data():
    return {"users": ["Alice", "Bob"], "active": True}

def test_with_fixture(sample_data):
    # Validate dữ liệu từ fixture
    assert len(sample_data["users"]) == 2
    assert "Alice" in sample_data["users"]
    assert sample_data["active"] is True


# Validate với parametrize
@pytest.mark.parametrize("input,expected", [
    (1, 1),
    (2, 4),
    (3, 9),
    (4, 16)
])
def test_square(input, expected):
    assert input * input == expected
    
@pytest.mark.parametrize("value,type_", [
    ("string", str),
    (123, int),
    (3.14, float),
    (True, bool)
])
def test_types(value, type_):
    assert isinstance(value, type_)

# Validate với pytest.xfail  (sử dụng tính năng builtin của pytest) - cho phép bắt nhiều lỗi hơn 
def test_multiple_assertions():
    assert 1 == 1
    assert 2 == 2
    
    if 3 != 4:
        pytest.xfail("3 is not equal to 4")
    
    if 5 != 6:
        pytest.xfail("5 is not equal to 6")


# Validate None và truthy/falsy
def test_none_and_truthiness():
    # Kiểm tra None
    x = None
    assert x is None
    y = "something"
    assert y is not None
    
    # Kiểm tra truthy/falsy
    assert bool([1, 2, 3])  # List không rỗng là truthy
    assert not bool([])     # List rỗng là falsy
    assert bool("")  # Chuỗi rỗng là falsy
    assert bool(0)   # Số 0 là falsy