from datetime import datetime
from typing import Union


def mask_account_card(data: str) -> str:
    """
    Маскирует номера карт (16 цифр) и счетов (20 цифр) в переданной строке.
    Форматы:
    - Карта: 1234567890123456 -> 1234 56** **** 3456
    - Счет: 12345678901234567890 -> **7890
    - Сохраняет префиксы (Visa, Счет и т.д.)
    """
    if not isinstance(data, str):
        raise ValueError("Input must be a string")

    if not data:
        return data

    # Извлекаем цифры и префикс
    digits = ''.join(filter(str.isdigit, data))
    prefix = next((word for word in data.split() if not word.isdigit()), "")

    # Маскировка карты
    if len(digits) == 16:
        masked = f"{digits[:4]} {digits[4:6]}** **** {digits[-4:]}"
        return f"{prefix} {masked}".strip() if prefix else masked

    # Маскировка счета
    elif len(digits) == 20:
        return f"{prefix} **{digits[-4:]}".strip() if prefix else f"**{digits[-4:]}"

    return data


def get_date(date_string: str) -> str:
    """
    Преобразует дату из формата ISO 8601 (YYYY-MM-DDTHH:MM:SS.XXX)
    в формат DD.MM.YYYY
    """
    if not date_string:
        raise ValueError("Empty date string")

    try:
        date_part = date_string.split('T')[0]
        date_obj = datetime.strptime(date_part, "%Y-%m-%d")
        return date_obj.strftime("%d.%m.%Y")
    except (ValueError, IndexError, AttributeError):
        raise ValueError(f"Invalid date format: {date_string}")
