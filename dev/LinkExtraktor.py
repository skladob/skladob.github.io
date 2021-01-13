import link_extractor


def get_link(url):
    links = link_extractor.getLinks(url)
    for link in links:
        result = link_extractor.getLinks(link)
        for a in result:
            print(a)










if __name__ == "__main__":
    get_link('https://sivik.ru')
