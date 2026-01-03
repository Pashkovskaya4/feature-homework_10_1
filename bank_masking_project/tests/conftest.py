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

@pytest.fixture
def result_transaction_usd() -> list:
    """Фикстура со списком транзакций по параметру 'USD'"""
    return (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        }
    ]
    )

@pytest.fixture
def transaction() -> list:
    """Фикстура со списком транзакций"""
    return (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
    )

@pytest.fixture
def descriptions() -> list:
    """Фикстура с результатами сортировки по операциям"""
    return ["Перевод организации",
            "Перевод со счета на счет",
            "Перевод со счета на счет",
            "Перевод с карты на карту",
            "Перевод организации"
            ]
