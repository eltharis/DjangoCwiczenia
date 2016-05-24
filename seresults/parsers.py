# -*- coding: utf-8 -*-

from lxml import html
import requests


def fetch_aol(query):
    url = "http://search.aol.com/aol/search?enabled_terms=&s_it=comsearch&q={0}&s_chn=prt_maing13".format(query)
    r = requests.get(url)
    root = html.fromstring(r.text)

    li_list = root.xpath('//ul[@content="ALGO"]/li')
    items = []

    for li in li_list:
        link = li.xpath('./h3[@class="hac"]/a[@class="find"]')
        description = li.xpath('./p[@property="f:desc"]')

        # zabezpieczenie w przypadku gdy są odpowiedzi np. ze słownika AOL ( query = "test" )
        if link.__len__() == 1:
            item = (link[0].attrib['href'], link[0].text_content(), description[0].text_content())
            items.append(item)

    return items
