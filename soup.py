from lxml import html
import requests


def get_soup():
    page = requests.get("http://www.greenrestaurante.com.br/our-menu/")
    tree = html.fromstring(page.content)
    menu_items = tree.xpath('//section[@class="menu-item"]')
    for item in menu_items:
        if item.xpath('span/strong/text()')[0] == 'SOPA':
            return item.xpath('span[@class="description"]/text()')[0]
