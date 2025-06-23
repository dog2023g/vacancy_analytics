import requests
import datetime
from lxml import etree


def add_months(sourcedate, months):
    """
    Добавление нужного количества месяцев к данной дате
    :param sourcedate: Данная дата
    :param months: Количество месяцев, которые нужно добавить
    :return: Новый экземпляр даты
    """
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    return datetime.date(year, month, 1)


def get_rate_currencies(session, date_):
    """
    Получение списка с курсом валют на данную дату
    :param session: Сессия requests
    :param date_: Данная дата
    :return: Список с курсом валют на данную дату
    """
    # Форматирование даты для запроса
    date_str = date_.strftime("%d/%m/%Y")
    # Список для добавления в таблицу
    result = {}

    # Получение xml данных о курсе валют на данную дату
    response = session.get(url + date_str)

    # Инициализация парсера xml
    parser = etree.XMLParser(recover=True)
    root = etree.fromstring(response.content, parser)

    # Создание словаря с данными о валютах (ключ - ID валюты, значение - данные о валюте)
    valutes = {v.get('ID'): v for v in root.xpath('//Valute')}

    # Заполнение списка курсами валют
    for currency_id in currencies_ids:
        valute = valutes.get(currency_id)
        if valute is not None:
            vunit = valute.find('VunitRate').text.replace(',', '.', 1)
            result[id_to_currency[currency_id]] = float(vunit)

    return date_.strftime("%Y-%m"), result


def main():
    """
    Создание таблицы с курсами валют за период с 01.01.2003 до 01.11.2024 включительно, за первое число каждого месяца
    :return:
    """
    with requests.Session() as session:
        # Добавление данных о курсе валют с 2003 по 2024 годы
        start_year = 2003
        end_year = 2024
        start_date = datetime.date(start_year, 1, 1)
        # Количество месяцев
        count_months = (end_year-start_year+1)*12
        for i in range(count_months):
            current_date = add_months(start_date, i)
            date, cur = get_rate_currencies(session, current_date)
            currencies_result[date] = cur
    print(currencies_result)


url = "https://www.cbr.ru/scripts/XML_daily.asp?date_req="
currencies = {
    "BYR": "R01090",
    "USD": "R01235",
    "EUR": "R01239",
    "KZT": "R01335",
    "UAH": "R01720",
    "AZN": "R01020A",
    "KGS": "R01370",
    "UZS": "R01717",
    "GEL": "R01210"
}
id_to_currency = {
    "R01090": "BYR",
    "R01235": "USD",
    "R01239": "EUR",
    "R01335": "KZT",
    "R01720": "UAH",
    "R01020A": "AZN",
    "R01370": "KGS",
    "R01717": "UZS",
    "R01210": "GEL"
}
currencies_ids = list(currencies.values())

currencies_result = {}

if __name__ == "__main__":
    main()
