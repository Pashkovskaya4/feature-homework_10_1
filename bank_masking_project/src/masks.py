"""
Модуль для маскировки номеров банковских карт и счетов.
"""


def get_mask_card_number(card_number: int) -> str:
    """
    Возвращает маскированный номер карты в формате: XXXX XX** **** XXXX.

    Пример:
    Вход: 7000792289606361
    Выход: "7000 79** **** 6361"

    :param card_number: Номер банковской карты в виде целого числа (16 цифр).
    :return: Маскированный номер карты в виде строки.
    """
    card_str = str(card_number)
    if len(card_str) != 16:
        raise ValueError("Номер карты должен содержать ровно 16 цифр.")

    masked_card = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"
    return masked_card


def get_mask_account(account_number: int) -> str:
    """
    Возвращает маскированный номер счёта в формате: **XXXX.

    Пример:
    Вход: 73654108430135874305
    Выход: "**4305"

    :param account_number: Номер счёта в виде целого числа.
    :return: Маскированный номер счёта в виде строки.
    """
    account_str = str(account_number)
    if len(account_str) < 4:
        raise ValueError("Номер счёта должен содержать минимум 4 цифры.")

    masked_account = f"**{account_str[-4:]}"
    return masked_account
