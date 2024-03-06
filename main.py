import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen

def get_phone_numbers(url):
    response = requests.get(url)
    html = urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(response.text, 'html.parser')
    phone_numbers = re.findall(r'(\+7)[-.\s]?\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{2})[-.\s]?(\d{2})',
                               html)
    if (len(phone_numbers)==0):
        phone_numbers = re.findall(r'(\+7|8)[-.\s]?\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{2})[-.\s]?(\d{2})',
                                   soup.get_text())
    phone_numbers = ['8' + ''.join(number[1:]) for number in phone_numbers]
    return list(set(phone_numbers))


print(get_phone_numbers("https://hands.ru/company/about"))
print(get_phone_numbers("https://repetitors.info"))
