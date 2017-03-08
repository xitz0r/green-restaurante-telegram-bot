from lxml import html
import requests


def get_soup_and_juice():
    page = requests.get("http://www.greenrestaurante.com.br/our-menu/")
    tree = html.fromstring(page.content)
    menu_items = tree.xpath('//section[@class="menu-item"]')
    soup = ''
    juice = ''

    for item in menu_items:
        if item.xpath('span/strong/text()')[0].upper() == 'SOPA':
            soup = item.xpath('span[@class="description"]/text()')[0]

    if soup == '':
        menu_items = tree.xpath('//div[@class="col-md-10 col-md-offset-1 menu-category-group"]')
        for item in menu_items:
            if 'SOPA' in item.xpath('h2/text()')[0].upper():
                soup = item.xpath('section[@class="menu-item"]/span[@class="title"]/strong/text()')[0]

    menu_items = tree.xpath('//div[@class="col-md-10 col-md-offset-1 menu-category-group"]')
    for item in menu_items:
        if item.xpath('h2/text()')[0].upper() == 'REFRESCO DO DIA ':
            juice = item.xpath('section/span[@class="title"]/strong/text()')[0]

    return soup, juice
