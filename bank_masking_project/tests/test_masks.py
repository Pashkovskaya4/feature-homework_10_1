import pytest
from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    # Проверяем правильную маскировку
    card_number = 7000792289606361
    assert get_mask_card_number(card_number) == "7000 79** **** 6361"

    # Проверяем, что если длина не 16, будет ошибка
    with pytest.raises(ValueError):
        get_mask_card_number(123)


def test_get_mask_account():
    # Проверяем правильную маскировку
    account_number = 73654108430135874305
    assert get_mask_account(account_number) == "**4305"

    # Проверяем, что если меньше 4 цифр, будет ошибка
    with pytest.raises(ValueError):
        get_mask_account(123)
