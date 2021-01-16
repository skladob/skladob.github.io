#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

import link_extractor

url = 'https://sivik.ru'
query = 'INSERT INTO href VALUES (site)'

links = link_extractor.getLinks(url)
connect = sqlite3.connect('newDataBase.db')
connect.row_factory
cursor = connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS href(site TEXT)""")
connect.commit()
for data_links in links:
    cursor.execute(query, data_links)

connect.commit()
cursor.close()
connect.close()
