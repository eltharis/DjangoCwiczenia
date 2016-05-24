# -*- coding: utf-8 -*-

from lxml import html
import requests


def fetch_aol(query):
    URL = "http://search.aol.com/aol/search?enabled_terms=&s_it=comsearch&q={0}&s_chn=prt_maing13".format(query)
    r = requests.get(URL)
    root = html.fromstring(r.text)

    liList = root.xpath('//ul[@content="ALGO"]/li')
    items = []

    for li in liList:
        link = li.xpath('./h3[@class="hac"]/a[@class="find"]')
        description = li.xpath('./p[@property="f:desc"]')

        # zabezpieczenie w przypadku gdy są odpowiedzi np. ze słownika AOL ( query = "test" )
        if link.__len__() == 1:
            item = (link[0].attrib['href'], link[0].text_content(), description[0].text_content())
            items.append(item)

    return items
