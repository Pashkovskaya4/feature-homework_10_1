import pytest
from datetime import datetime, timedelta

@pytest.fixture
def sample_operations() -> list[dict[str, any]]:
    """Основной набор тестовых данных"""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-10-01T12:00:00.000"},
        {"id": 2, "state": "PENDING", "date": "2023-09-15T08:30:00.000"},
        {"id": 3, "state": "EXECUTED", "date": "2023-10-05T15:45:00.000"},
        {"id": 4, "state": "CANCELED", "date": "2023-08-20T10:15:00.000"},
        {"id": 5, "state": "EXECUTED", "date": "2023-09-30T23:59:59.999"},
    ]

@pytest.fixture(params=[
    ("EXECUTED", [1, 3, 5]),
    ("PENDING", [2]),
    ("CANCELED", [4]),
    ("UNKNOWN", []),
])
def state_test_cases(request):
    """Параметризованные случаи для тестирования фильтрации по state"""
    return request.param

@pytest.fixture(params=[
    (True, [3, 1, 5, 2, 4]),  # descending
    (False, [4, 2, 5, 1, 3]),  # ascending
])
def sort_direction_cases(request):
    """Параметризованные случаи для тестирования направления сортировки"""
    return request.param

@pytest.fixture
def edge_case_operations() -> list[dict[str, any]]:
    """Крайние случаи для операций"""
    return [
        {"id": 6, "state": "", "date": "2023-01-01T00:00:00.000"},  # пустой state
        {"id": 7, "state": None, "date": "2023-01-02T00:00:00.000"},  # None state
        {"id": 8, "date": "2023-01-03T00:00:00.000"},  # отсутствует state
    ]

@pytest.fixture(params=[
    {"date": "invalid_date"},  # неверный формат даты
    {"date": None},  # None вместо даты
    {},  # отсутствует дата
    {"date": "2023-13-01T00:00:00.000"},  # несуществующая дата
])
def invalid_date_case(request):
    """Параметризованные невалидные даты"""
    return request.param

@pytest.fixture
def card_number() -> str:
    return "1234567890123456"  # Пример номера карты