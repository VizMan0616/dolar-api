from urllib.request import urlopen
from bs4 import BeautifulSoup
from ..common.constants import USD_URL
from re import search


def one_usd_to_ves():
    monitor_page = urlopen(USD_URL())
    soup = BeautifulSoup(monitor_page, 'html.parser')

    monitor_text = soup.find('div', attrs={'class': 'entry-content'})

    return float(search('([0-9]*[.,][0-9]*)+', monitor_text.text.strip()).group().replace('.', '').replace(',', '.'))


def usd_to_ves(usd: float) -> float:
    return round((one_usd_to_ves() * usd), 2)


def ves_to_usd(ves: float) -> float:
    return round((ves / one_usd_to_ves()), 2)


