from urllib.request import urlopen
from bs4 import BeautifulSoup
from ..common.constants import DOLLAR_URL
from re import search


def one_dollar_to_bolivar():
    dollar_page = urlopen(DOLLAR_URL())
    soup = BeautifulSoup(dollar_page, 'html.parser')

    dollar_text = soup.find('div', attrs={'class': 'entry-content'})
    return float(search('([0-9]*[.,][0-9]*)+', dollar_text.text.strip()).group().replace('.', '').replace(',', '.'))


def bucks_to_bolivar(dollar_quantity: float) -> float:
    return round((one_dollar_to_bolivar() * dollar_quantity), 2)


def bolivars_to_bucks(bolivar_quantity: float) -> float:
    return round((bolivar_quantity / one_dollar_to_bolivar()), 2)


