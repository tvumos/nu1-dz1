import requests
import json
from flask import Flask


def get_valutes_list():
    """
    Метод получения данных с сайта www.cbr-xml-daily.ru в формате JSON
    :return: Ответ с сайта www.cbr-xml-daily.ru в формате JSON
    """
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    data = json.loads(response.text)
    valutes = list(data['Valute'].values())
    return valutes


app = Flask(__name__)


def create_html(valutes):
    """
    Функция отрисовки страницы с таблицей курсы валют
    :param valutes: Таблица в формате JSON
    :return: HTML страница
    """
    text = '<h1>Курс валют</h1>'
    text += '<h3>по состоянию на: <body><script type="text/javascript">document.write(Date());</script></body></h3>'
    text += '<table style=" border-collapse: collapse; text-align: left;">'
    text += '<tr style=" text-align: center; padding: 1px 5px; border: 1px solid #000000; ">'
    for val in valutes[0]:
        text += f'<td style="padding: 1px 5px; border: 1px solid #000000; background-color: #D0D0D0; font-weight: bold;">' + val + '</td>'
    text += '</tr>'
    for valute in valutes:
        text += '<tr style=" padding: 1px 5px; border: 1px solid #000000; ">'
        for v in valute.values():
            text += f'<td style=" padding: 1px 5px; border: 1px solid #000000; ">{v}</td>'
        text += '</tr>'
    text += '</table>'
    return text


@app.route("/")
def index():
    valutes = get_valutes_list()
    print(valutes)
    html = create_html(valutes)
    return html


if __name__ == "__main__":
    app.run()
