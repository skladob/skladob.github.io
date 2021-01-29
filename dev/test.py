#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

import link_extractor

URL = 'https://sivik.ru'
QUERY = 'INSERT INTO href VALUES (?)'
DATABASE = r'SQL/db.sqlite3'


def new_func():
    links = link_extractor.getLinks('https://sivik.ru/')
    clinks = []
    for link in links:
        link.append(clinks)
    print(clinks)


new_func()
# links = link_extractor.getLinks('https://www.technovector.ru/')
# links.append(clinks)
# links = link_extractor.getLinks('https://ti-msk.ru/')
# links.append(clinks)
# links = link_extractor.getLinks('http://trommelberg.ru/')
# links.append(clinks)
# links = link_extractor.getLinks('https://honiton.ru/')
# links.append(clinks)
# links = link_extractor.getLinks('http://www.equinet.ru/')
# links.append(clinks)
# links = link_extractor.getLinks('https://gallax.ru/')
# links.append(clinks)
# links = link_extractor.getLinks('https://www.ttsauto.ru/#')
# links.append(clinks)
# links = link_extractor.getLinks('http://eurosiv.ru/')
# links.append(clinks)
# links = link_extractor.getLinks('https://si-tools.ru/')
# links.append(clinks)
# links = link_extractor.getLinks('https://www.haweka.ru/')
# links.append(clinks)
# links = link_extractor.getLinks('https://autel-russia.ru/')
# links.append(clinks)
# links = link_extractor.getLinks('http://www.atb.ru/')
# links.append(clinks)
# links = link_extractor.getLinks('https://www.mactak.ru/')
# links.append(clinks)
# links = link_extractor.getLinks('https://sibek.ru/')
# links.append(clinks)
# links = link_extractor.getLinks('https://www.hofmann-equipment.com/ru')
# links.append(clinks)
# links = link_extractor.getLinks('http://www.mkslift.ru/')
# links.append(clinks)
# links = link_extractor.getLinks('https://rtor.pro/')
# links.append(clinks)
# links = link_extractor.getLinks('http://drreifen.rocks/')
# links.append(clinks)
# print (clinks)
