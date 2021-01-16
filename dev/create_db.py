#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3


connect = sqlite3.connect('newDataBase.db')
connect.row_factory
cursor = connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS href(site TEXT)""")
connect.commit()
cursor.close()
connect.close()
