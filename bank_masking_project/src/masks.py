"""
Модуль для маскировки номеров банковских карт и счетов.

Функции модуля позволяют скрывать часть цифр номера карты или счета,
оставляя только первые и последние цифры для идентификации.
"""


def get_mask_card_number(card_number: int | str) -> str:
    """
    Возвращает маскированный номер карты в формате:
    - Для 16 цифр: `XXXX XX** **** XXXX`
    - Для 20 цифр: `XXXX XXXX XXXX XXXX **XX`

    Примеры:
    >>> get_mask_card_number("7000792289606361")  # 16 цифр
    '7000 79** **** 6361'
    >>> get_mask_card_number("12345678901234567890")  # 20 цифр
    '1234 5678 9012 3456 **90'

    :param card_number: Номер карты (16 или 20 цифр). Может быть числом или строкой.
    :return: Маскированный номер карты.
    :raises ValueError: Если номер не 16 или 20 цифр, или содержит нечисловые символы.
    """
    card_str = str(card_number).strip()

    if not card_str.isdigit():
        raise ValueError("Номер карты должен содержать только цифры")

    if len(card_str) == 16:
        return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"
    elif len(card_str) == 20:
        return f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:16]} **{card_str[-2:]}"
    else:
        raise ValueError("Номер карты должен содержать 16 или 20 цифр")

def get_mask_account(account_number: int | str) -> str:
    """
    Возвращает маскированный номер счёта в формате: **XXXX.

    Пример:
    >>> get_mask_account("73654108430135874305")
    '**4305'
    >>> get_mask_account(73654108430135874305)
    '**4305'

    :param account_number: Номер счёта. Может быть целым числом или строкой.
    :return: Маскированный номер счёта, показывающий только последние 4 цифры.
    :raises ValueError: Если номер счёта содержит менее 4 цифр или содержит нечисловые символы.
    """
    account_str = str(account_number).strip()

    if not account_str.isdigit():
        raise ValueError("Номер счёта должен содержать только цифры")

    if len(account_str) < 4:
        raise ValueError("Номер счёта должен содержать минимум 4 цифры")

    return f"**{account_str[-4:]}"