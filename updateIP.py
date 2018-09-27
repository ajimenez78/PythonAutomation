#!/usr/bin/python
import requests, bs4, re

IP_RETRIEVAL_SERVICE_URL = 'http://ip4.me/'
IP_STORAGE_SERVICE_URL = 'https://script.google.com/macros/s/AKfycbwZaRt7GQcNqSy3xQfMiAAsP7DSWSjr3_cmF87Oi8Vj_ql4S10W/exec'

response = requests.get(IP_RETRIEVAL_SERVICE_URL)
response.raise_for_status()
ip_service_soup = bs4.BeautifulSoup(response.text, 'html5lib')
font_elements = ip_service_soup.select('tr > td > font')
ip_regex = re.compile(r'(\d{1,3}\.){3}\d{1,3}')
found_ip = None
for element in font_elements:
    ip_match = ip_regex.search(element.getText())
    if ip_match:
        found_ip = ip_match.group()
        break
    
if found_ip:
    payload = {'ip': found_ip}
    requests.post(IP_STORAGE_SERVICE_URL, params=payload)
