import requests
import urllib.request
import time
from bs4 import BeautifulSoup


class Crawler:
    def __init__(self,url):
        self.url = url

    def source(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, "html.parser")
        return soup
