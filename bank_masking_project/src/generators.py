def filter_by_currency(list_of_dict: list, currency: str) -> list:
    """Функция сортировки по заданной валюте транзакции"""
    for i in list_of_dict:
        for x, y in i.items():
            if x == "operationAmount":
                for z, m in y.items():
                    if z == "currency":
                        for j, o in m.items():
                            if o == currency and j == "code":
                                yield i


def transaction_descriptions(list_of_dict: list) -> str:
    """Функция, возвращающая описание транзакции"""
    for i in list_of_dict:
        for x, y in i.items():
            if x == "description":
                yield y


def card_number_generator(start: int, stop: int) -> str:
    """Функция для генерации номеров банковских карт"""
    while start == stop or start < stop and start <= 9999999999999999:
        new_card_num = str(start).rjust(16, "0")
        yield f"{new_card_num[0:4]} {new_card_num[4:8]} {new_card_num[8:12]} {new_card_num[12:16]}"
        start = start + 1
