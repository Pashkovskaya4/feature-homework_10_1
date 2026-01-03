from bank_masking_project.src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency_correct(transaction: list, result_transaction_usd: list) -> None:
    """Тест на корректность транзакций по заданной валюте"""
    assert list(filter_by_currency(transaction, "USD")) == result_transaction_usd


def test_transaction_descriptions(transaction: list, descriptions) -> None:
    """Тест на корректное предоставление описания операции"""
    assert list(transaction_descriptions(transaction)) == descriptions


def test_card_number_generator() -> None:
    """Тест на корректную генерацию номеров карт в заданном диапазоне"""
    generator = card_number_generator(1, 3)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
