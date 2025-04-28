from datetime import datetime
from typing import Union


def mask_account_card(data: str) -> str:
    """Маскирует номер карты или счета"""
    if not data:
        return ""

    parts = data.split()
    if len(parts) < 2:
        return data

    *name_parts, number = parts
    name = " ".join(name_parts)

    if name.lower() == "счет":
        # Маскировка счета: последние 4 цифры
        if len(number) >= 4:
            return f"Счет **{number[-4:]}"
        return "Счет **"
    else:
        # Маскировка карты: 1234 56** **** 5678
        if len(number) == 16 and number.isdigit():
            return f"{name} {number[:4]} {number[4:6]}** **** {number[-4:]}"

    return data  # Если формат не распознан


def get_date(date_str: str) -> str:
    """Форматирует дату из ISO в DD.MM.YYYY"""
    try:
        date_obj = datetime.fromisoformat(date_str)
        return date_obj.strftime("%d.%m.%Y")
    except (ValueError, TypeError):
        return date_str  # Возвращаем исходное значение при ошибке