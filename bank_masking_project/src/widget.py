def mask_account_card(account_info: str) -> str:
    """Маскирует номер карты или счета."""
    parts = account_info.split()
    number = parts[-1]
    name = " ".join(parts[:-1])

    if "счет" in account_info.lower():
        masked_number = "**" + number[-4:]
    else:
        # Маскировка карты: 7000 79** **** 6361
        masked_number = f"{number[:4]} {number[4:6]}** **** {number[-4:]}"

    return f"{name} {masked_number}"


def get_date(date_str: str) -> str:
    """Преобразует дату из формата '2024-03-11T02:26:18.671407' в '11.03.2024'."""
    from datetime import datetime

    date_obj = datetime.strptime(date_str.split("T")[0], "%Y-%m-%d")
    return date_obj.strftime("%d.%m.%Y")

if __name__ == "__main__":
    # Тест маскировки карт и счетов
    test_cases = [
        "Visa Platinum 7000792289606361",
        "Maestro 1596837868705199",
        "Счет 73654108430135874305",
        "MasterCard 7158300734726758",
        "Счет 35383033474447895560",
    ]

    for case in test_cases:
        print(f"{case} → {mask_account_card(case)}")

    # Тест форматирования даты
    print(get_date("2024-03-11T02:26:18.671407"))  # Должно вернуть "11.03.2024"