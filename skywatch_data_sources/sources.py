from operator import itemgetter

import requests
from bs4 import BeautifulSoup


def get_data_sources():
    """
    Parses www.skywatch.com and returns a list of its available data sources
    """
    url = 'https://www.skywatch.com/sitemap.xml'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')

    images = soup.find_all('image:image')

    sources = []
    for image in images:
        if image.find('image:title').get_text() == 'Sources':
            source, resolution, _ = image.find(
                'image:caption').get_text().split(' / ')
            splited_source = source.split(' Provider: ')

            data = {
                'Source': splited_source[0].strip(),
                'Provider': splited_source[1].strip(),
                'Resolution': resolution.split(': ')[1].strip(),
            }

            sources.append(data)

    return sorted(sources, key=itemgetter('Provider'))
