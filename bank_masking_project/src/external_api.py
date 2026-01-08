import requests
import os
from typing import Dict, Any, Optional
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()


def convert_transaction_amount(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    Args:
        transaction: Словарь с данными о финансовой транзакции

    Returns:
        Сумма транзакции в рублях (float)

    Raises:
        ValueError: Если валюта не поддерживается или данные некорректны
        KeyError: Если отсутствуют обязательные поля в транзакции
    """
    try:
        # Извлекаем данные из транзакции
        amount = float(transaction["operationAmount"]["amount"])
        currency = transaction["operationAmount"]["currency"]["code"]

        # Если валюта уже в рублях - возвращаем как есть
        if currency == "RUB":
            return round(amount, 2)

        # Если валюта в USD или EUR - конвертируем через API
        elif currency in ("USD", "EUR"):
            # Получаем API ключ из переменных окружения
            api_key = os.getenv("EXCHANGE_RATES_API_KEY")
            if not api_key:
                raise ValueError("API ключ не найден. Установите переменную окружения EXCHANGE_RATES_API_KEY")

            # Формируем запрос к API
            url = f"https://api.apilayer.com/exchangerates_data/latest"
            params = {
                "base": currency,
                "symbols": "RUB"
            }
            headers = {
                "apikey": api_key
            }

            # Выполняем запрос к API
            response = requests.get(url, params=params, headers=headers, timeout=10)
            response.raise_for_status()  # Проверяем статус ответа

            # Парсим ответ
            data = response.json()

            # Проверяем успешность запроса к API
            if not data.get("success", True):
                raise ValueError(f"Ошибка API: {data.get('error', {}).get('message', 'Неизвестная ошибка')}")

            # Получаем курс валюты
            exchange_rate = data["rates"]["RUB"]

            # Конвертируем сумму
            converted_amount = amount * exchange_rate
            return round(converted_amount, 2)

        # Если валюта не поддерживается
        else:
            raise ValueError(f"Неподдерживаемая валюта: {currency}")

    except KeyError as e:
        raise KeyError(f"Отсутствует обязательное поле в транзакции: {e}")
    except ValueError as e:
        raise ValueError(f"Некорректные данные: {e}")
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"Ошибка соединения с API: {e}")
    except Exception as e:
        raise RuntimeError(f"Неожиданная ошибка при конвертации: {e}")


# Пример использования
if __name__ == "__main__":
    # Тестовые данные
    test_transaction_usd = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "700",
            "currency": {
                "name": "доллары",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }

    test_transaction_rub = {
        "id": 441945887,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "50000",
            "currency": {
                "name": "рубли",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }

    # Тестирование конвертации USD -> RUB
    try:
        # Установите переменную окружения EXCHANGE_RATES_API_KEY для теста
        if os.getenv("EXCHANGE_RATES_API_KEY"):
            result_usd = convert_transaction_amount(test_transaction_usd)
            print(f"700 USD = {result_usd} RUB")
        else:
            print("Для тестирования конвертации установите EXCHANGE_RATES_API_KEY в .env файле")
    except Exception as e:
        print(f"Ошибка при конвертации USD: {e}")

    # Тестирование транзакции в рублях
    try:
        result_rub = convert_transaction_amount(test_transaction_rub)
        print(f"50000 RUB = {result_rub} RUB (без конвертации)")
    except Exception as e:
        print(f"Ошибка при обработке RUB: {e}")

