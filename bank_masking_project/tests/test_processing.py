import pytest
from datetime import datetime
from ..src.processing import filter_by_state, sort_by_date

# Общие тестовые данные
SAMPLE_DATA = [
    {"id": 1, "state": "EXECUTED", "date": "2023-10-01T12:00:00.000"},
    {"id": 2, "state": "PENDING", "date": "2023-09-15T08:30:00.000"},
    {"id": 3, "state": "EXECUTED", "date": "2023-10-15T08:00:00.000"},
    {"id": 4, "state": "CANCELED", "date": "2023-08-20T10:15:00.000"},
    {"id": 5, "state": "EXECUTED", "date": "2023-09-30T23:59:59.999"},
]


class TestFilterByState:
    """Тестирование фильтрации по статусу"""

    @pytest.mark.parametrize("state, expected_ids", [
        ("EXECUTED", [1, 3, 5]),
        ("PENDING", [2]),
        ("CANCELED", [4]),
        ("UNKNOWN", []),
    ])
    def test_filter_by_state(self, state: str, expected_ids: list[int]) -> None:
        """Параметризованный тест для разных статусов"""
        result = filter_by_state(SAMPLE_DATA, state)
        assert [item["id"] for item in result] == expected_ids

    def test_filter_empty_input(self) -> None:
        """Тест с пустым списком транзакций"""
        assert filter_by_state([]) == []

    def test_filter_invalid_state_type(self) -> None:
        """Тест с некорректным типом статуса"""
        with pytest.raises(TypeError):
            filter_by_state(SAMPLE_DATA, state=123)


class TestSortByDate:
    """Тестирование сортировки по дате"""

    SAMPLE_SORT_DATA = [
        {"id": 1, "date": "2023-10-10T12:00:00.000"},
        {"id": 2, "date": "2023-10-05T10:00:00.000"},
        {"id": 3, "date": "2023-10-15T08:00:00.000"},
        {"id": 4, "date": "2023-10-01T14:00:00.000"},
        {"id": 5, "date": "2023-10-07T16:00:00.000"},
    ]

    def test_sort_descending(self) -> None:
        """Тест сортировки по убыванию"""
        result = sort_by_date(self.SAMPLE_SORT_DATA, descending=True)
        assert [item["id"] for item in result] == [3, 1, 5, 2, 4]

    def test_sort_ascending(self) -> None:
        """Тест сортировки по возрастанию"""
        result = sort_by_date(self.SAMPLE_SORT_DATA, descending=False)
        assert [item["id"] for item in result] == [4, 2, 5, 1, 3]

    def test_sort_with_equal_dates(self) -> None:
        """Тест с одинаковыми датами"""
        modified_data = self.SAMPLE_SORT_DATA + [
            {"id": 6, "date": "2023-10-15T08:00:00.000"}
        ]
        result = sort_by_date(modified_data, descending=True)
        assert {item["id"] for item in result[:2]} == {3, 6}

    @pytest.mark.parametrize("invalid_data", [
        {"id": 99, "date": "invalid_date"},
        {"id": 99, "date": None},
        {"id": 99},
    ])
    def test_sort_with_invalid_dates(self, invalid_data: dict[str, any]) -> None:
        """Тест с некорректными датами"""
        with pytest.raises((ValueError, KeyError, TypeError)):
            sort_by_date(self.SAMPLE_SORT_DATA + [invalid_data])

    def test_sort_empty_input(self) -> None:
        """Тест с пустым списком"""
        assert sort_by_date([]) == []