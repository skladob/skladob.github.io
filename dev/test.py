#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

import link_extractor

URL = 'https://sivik.ru'
QUERY = 'INSERT INTO href VALUES (?)'
DATABASE = r'SQL/db.sqlite3'

links = link_extractor.getLinks(URL)
connect = sqlite3.connect(DATABASE)
connect.row_factory
cursor = connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS href(site TEXT)""")
connect.commit()
for data_links in links:
# print(type(links))
# print(links)
    cursor.executemany(QUERY, links)

connect.commit()
cursor.close()
connect.close()
