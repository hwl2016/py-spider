# encoding=utf-8
import csv
from zipfile import ZipFile
from StringIO import StringIO
from downloader import Downloader

class AlexaCallback:
    def __init__(self, max_urls=1000):
        self.max_urls = max_urls
        # 'http://s3.amazonaws.com/topsites'
        self.seed_url = 'http://s3.amazonaws.com/alexa-static/top-lm.csv.zip'

    def __call__(self, url, html):
        if url == self.seed_url:
            urls = []
            with ZipFile(StringIO(html)) as zf:
                csv_filename = zf.namelist()[0]
                for _, website in csv.reader(zf.open(csv_filename)):
                    urls.append('http://' + website)
                    if len(urls) == self.max_urls:
                        break
            return urls



if __name__ == '__main__':
    ac = AlexaCallback()
    ac()