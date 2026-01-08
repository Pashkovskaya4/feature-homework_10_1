import json
from typing import List, Dict, Any
import os


def load_transactions_from_json(file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает транзакции из JSON-файла.

    Args:
        file_path: Путь до JSON-файла с транзакциями

    Returns:
        Список словарей с данными транзакций.
        Возвращает пустой список если:
        - файл не найден
        - файл пустой
        - файл не содержит список
        - произошла ошибка декодирования JSON
    """
    # Проверяем существование файла
    if not os.path.exists(file_path):
        return []

    # Проверяем, что это файл (а не директория)
    if not os.path.isfile(file_path):
        return []

    try:
        # Открываем файл для чтения
        with open(file_path, 'r', encoding='utf-8') as file:
            # Проверяем, что файл не пустой
            if os.stat(file_path).st_size == 0:
                return []

            # Загружаем данные из JSON
            data = json.load(file)

            # Проверяем, что данные - это список
            if isinstance(data, list):
                return data
            else:
                return []

    except (json.JSONDecodeError, OSError, IOError):
        # Возвращаем пустой список при любых ошибках чтения/парсинга
        return []
