import pytest
from datetime import datetime
from bank_masking_project.src.widget import mask_account_card, get_date


class TestMaskAccountCard:
    """Тесты для функции маскировки карт и счетов"""

    # Параметризованные тесты для валидных данных
    @pytest.mark.parametrize("input_data, expected", [
        # Тесты для карт
        ("1234567890123456", "1234 56** **** 3456"),
        ("Visa 1234567890123456", "Visa 1234 56** **** 3456"),
        ("MasterCard 1234 5678 9012 3456", "MasterCard 1234 56** **** 3456"),
        ("МИР 1234567890123456", "МИР 1234 56** **** 3456"),

        # Тесты для счетов
        ("12345678901234567890", "**7890"),
        ("Счет 12345678901234567890", "Счет **7890"),
        ("Account 12345678901234567890", "Account **7890"),

        # Граничные случаи
        ("", ""),
        ("Card ", "Card "),
        ("Счет ", "Счет "),
    ])
    def test_mask_valid(self, input_data: str, expected: str) -> None:
        assert mask_account_card(input_data) == expected

    # Тесты для невалидных данных
    @pytest.mark.parametrize("invalid_input", [
        None,
        1234567890123456,
        ["1234567890123456"],
        {"card": "1234567890123456"},
    ])
    def test_mask_invalid(self, invalid_input: any) -> None:
        with pytest.raises(ValueError):
            mask_account_card(invalid_input)


class TestGetDate:
    """Тесты для функции форматирования даты"""

    @pytest.mark.parametrize("input_date, expected", [
        ("2023-12-31T12:34:56.789", "31.12.2023"),
        ("2020-01-01T00:00:00.000", "01.01.2020"),
        ("1999-12-31T23:59:59.999", "31.12.1999"),
    ])
    def test_get_date_valid(self, input_date: str, expected: str) -> None:
        assert get_date(input_date) == expected

    @pytest.mark.parametrize("invalid_date", [
        "",
        "invalid_date_string",
        "2023-13-01T00:00:00.000",  # Несуществующий месяц
        "2023-12-32T00:00:00.000",  # Несуществующий день
        None,
        1234567890,
        datetime.now(),  # Объект datetime вместо строки
    ])
    def test_get_date_invalid(self, invalid_date: any) -> None:
        with pytest.raises(ValueError):
            get_date(invalid_date)