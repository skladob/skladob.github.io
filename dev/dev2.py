#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

hosts = ['https://siwik.ru/', 'https://www.technovector.ruc/']


def response(hosts):
    for host in hosts:
        r = requests.get(host)
        print(r.status_code)
        # response = r.content
        # if r.status_code == 200:
        #     print (response)
        #     return response
        # elif r.status_code == 404:
        #     print('URL:', r.url, 'not found.')
        # elif r.status_code != 200:
        #     print(r.status_code)
response(hosts)
