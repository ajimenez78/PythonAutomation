#!/usr/bin/python
import requests, bs4, sys

PIRATE_PROXY_LIST_URL = 'https://thepiratebay-proxylist.org/'

class TorrentSearcher:
    QUERY_PATH = '/s/'
    
    def __init__(self, proxy_url):
        self.search_url = proxy_url + self.QUERY_PATH

    def search(self, query_string):
        payload = {'q': query_string}
        search_result_response = requests.post(self.search_url, params=payload)
        search_result_response.raise_for_status()
        search_result_soup = bs4.BeautifulSoup(search_result_response.text, 'html5lib')
        result_tables = search_result_soup.select('#searchResult')
        if (len(result_tables) > 0):
            self.search_result_table = result_tables[0]
        else:
            self.search_result_table = 'No results for search'
        
def build_torrent_searcher():
    proxy_response = requests.get(PIRATE_PROXY_LIST_URL)
    proxy_response.raise_for_status()
    return TorrentSearcher(best_proxy_from_html(proxy_response.text))

def best_proxy_from_html(html_proxy_list):
    proxy_list_soup = bs4.BeautifulSoup(html_proxy_list, 'html5lib')
    proxy_anchor_list = proxy_list_soup.select('.proxies td[title="URL"] a')
    return proxy_anchor_list[0].get('href')

print (str(sys.argv) + ' ' + str(len(sys.argv)))
if len(sys.argv) < 2:
    print('Usage: [python] torrent_searcher.py <search_string>')
else:
    searcher = build_torrent_searcher()
    searcher.search(sys.argv[1])
    print(searcher.search_result_table)
