import pytest
from unittest.mock import patch, MagicMock

# Импортируем правильное имя функции
from bank_masking_project.src.external_api import convert_transaction_amount


# Тест 1: Простой тест транзакции в рублях
def test_convert_rub_transaction():
    """
    Тест 1: Транзакция в рублях - должна возвращаться без изменений
    """
    transaction = {
        "operationAmount": {
            "amount": "1500.75",
            "currency": {
                "code": "RUB"
            }
        }
    }

    result = convert_transaction_amount(transaction)

    # Проверяем результат
    assert result == 1500.75
    assert isinstance(result, float)


# ТЕСТ 2: USD транзакция с моком API
def test_convert_usd_transaction_with_mock():
    """Тест конвертации USD в RUB с моком внешнего API"""
    transaction = {
        "operationAmount": {
            "amount": "100.00",
            "currency": {
                "code": "USD"
            }
        }
    }

    # 1. Мокаем os.getenv чтобы вернуть тестовый API ключ
    with patch('bank_masking_project.src.external_api.os.getenv') as mock_getenv:
        mock_getenv.return_value = 'test-api-key-123'

        # 2. Мокаем requests.get чтобы не делать реальный HTTP запрос
        with patch('bank_masking_project.src.external_api.requests.get') as mock_get:
            # Настраиваем мок ответа от API
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_response.raise_for_status.return_value = None
            mock_response.json.return_value = {
                "success": True,
                "rates": {
                    "RUB": 91.5  # Курс доллара к рублю
                }
            }
            mock_get.return_value = mock_response

            # Вызываем функцию
            result = convert_transaction_amount(transaction)

            # Проверяем результат (100 USD * 91.5 = 9150 RUB)
            assert result == 9150.0
            assert isinstance(result, float)

            # Проверяем вызовы моков (опционально)
            mock_getenv.assert_called_once_with("EXCHANGE_RATES_API_KEY")
            mock_get.assert_called_once()

            # Можно проверить параметры вызова API
            call_args = mock_get.call_args
            assert call_args is not None
            # URL
            assert call_args[0][0] == "https://api.apilayer.com/exchangerates_data/latest"
            # Параметры
            assert call_args[1]['params'] == {"base": "USD", "symbols": "RUB"}
            # Заголовки
            assert call_args[1]['headers'] == {"apikey": "test-api-key-123"}
