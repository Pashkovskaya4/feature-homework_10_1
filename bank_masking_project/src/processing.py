from datetime import datetime


def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Фильтрует транзакции по статусу.

    :param transactions: Список транзакций
    :param state: Статус транзакции (любая строка)
    :return: Отфильтрованный список транзакций
    """
    if not isinstance(state, str):
        raise TypeError("Статус должен быть строкой")

    return [t for t in transactions if t.get("state") == state]


def sort_by_date(transactions: list[dict], descending: bool = True) -> list[dict]:
    """
    Сортирует транзакции по дате.

    :param transactions: Список транзакций
    :param descending: Сортировка по убыванию
    :return: Отсортированный список
    :raises: ValueError, KeyError, TypeError
    """

    def get_date(item):
        if "date" not in item:
            raise KeyError("Отсутствует ключ 'date'")

        date_str = item["date"]
        if date_str is None:
            raise ValueError("Дата не может быть None")

        try:
            return datetime.fromisoformat(date_str)
        except (TypeError, ValueError):
            raise ValueError(f"Неверный формат даты: {date_str}")

    try:
        return sorted(
            transactions,
            key=get_date,
            reverse=descending
        )
    except Exception as e:
        raise e