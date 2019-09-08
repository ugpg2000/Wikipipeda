import requests
import re
from bs4 import BeautifulSoup
from tika import parser
import json

# Subroutine for webpages
# Proven that it works for facebook (in current state)
def webpage(url):
    r = requests.get(url)
    # Parse through the text to find "terms of usage"
    try:
        location = [m.start() for m in re.finditer('terms of service', r.text.lower())]
        soup = r.text[location[0]:]
    except:
        return 2

    location = [m.start() for m in re.finditer('<script>', soup.lower())]

    soup_stripped = soup[:location[0]]
    soup_stripped = BeautifulSoup(soup_stripped, "html.parser").get_text()

    # Prints our desired piece of code!!!
    print(soup_stripped)
    # All text.
    return soup_stripped


def pdf(file_location):
    raw = parser.from_file(file_location)
    print(raw['content'])
    return raw['content']


def tester():
    data = {}
    data['key'] = []
    data['key'].append({
        'rating': '6.44',
        'potential_options':[{
            'wikipedia': '10',
            'cbc': '9.23',
            'tvo': '9.22'
        }]
    })
    return data