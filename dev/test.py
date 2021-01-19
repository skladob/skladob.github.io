#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import link_extractor

TEMPFILE = 'tmp/templinks.txt'

with open('tmp/url.txt', 'r') as file:
    urls = file.read()
    for url in urls:
        print(url)
        # link_extractor.getLinks(url)


# for URL in list:
#     links = link_extractor.getLinks(URL)
#     for link in links:
#         i = link + '\n'
#         with open(TEMPFILE, 'a+') as file:
#             file.write(i)
