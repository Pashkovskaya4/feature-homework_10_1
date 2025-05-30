def filter_by_state(transactions: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """
    Фильтрует транзакции по статусу.

    :param transactions: Список словарей с транзакциями
    :param state: Статус для фильтрации (по умолчанию 'EXECUTED')
    :return: Отфильтрованный список транзакций
    """
    return [t for t in transactions if t.get('state') == state]


def sort_by_date(transactions: list[dict], reverse: bool = True) -> list[dict]:
    """
    Сортирует транзакции по дате.

    :param transactions: Список словарей с транзакциями
    :param reverse: Порядок сортировки (True - по убыванию, False - по возрастанию)
    :return: Отсортированный список транзакций
    """
    return sorted(
        transactions,
        key=lambda x: x['date'],
        reverse=reverse
    )