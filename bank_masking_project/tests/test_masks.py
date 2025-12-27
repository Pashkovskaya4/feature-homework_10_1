from bank_masking_project.src.masks import get_mask_card_number, get_mask_account
import pytest


@pytest.mark.parametrize("card_number, expected", [
    ("7000792289606361", "7000 79** **** 6361"),  # 16 цифр
    ("12345678901234567890", "1234 5678 9012 3456 **90"),  # 20 цифр
])
def test_get_mask_card_number_valid(card_number: str, expected: str) -> None:
    """Тестирование правильности маскировки номера карты для валидных данных"""
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("invalid_card", [
    "123",  # слишком короткий
    "700079228960636A",  # содержит букву
    "700079228960636123456",  # 21 цифра (не 16 и не 20)
])
def test_get_mask_card_number_invalid(invalid_card: str) -> None:
    """Тестирование обработки невалидных номеров карт"""
    with pytest.raises(ValueError):
        get_mask_card_number(invalid_card)


@pytest.mark.parametrize("account_number, expected", [
    ("73654108430135874305", "**4305"),
    ("1234567890", "**7890"),
])
def test_get_mask_account_valid(account_number: str, expected: str) -> None:
    """Тестирование правильности маскировки номера счета"""
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize("invalid_account", [
    "123",  # слишком короткий
    "7365410843013587430A",  # содержит букву
])
def test_get_mask_account_invalid(invalid_account: str) -> None:
    """Тестирование обработки невалидных номеров счетов"""
    with pytest.raises(ValueError):
        get_mask_account(invalid_account)
