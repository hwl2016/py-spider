# encoding=utf-8

import sys
import lxml.html
from PySide.QtGui import *
from PySide.QtCore import *
from PySide.QtWebKit import *

def getHtml():
    url = 'http://example.webscraping.com/dynamic'
    app = QApplication([])
    webview = QWebView()
    loop = QEventLoop()
    webview.loadFinished.connect(loop.quit)
    webview.load(QUrl(url))
    loop.exec_()
    html = webview.page().mainFrame().toHtml()
    tree = lxml.html.fromstring(html)
    content = tree.cssselector('#results')[0].text_content()
    print content

def helloword():
    app = QApplication(sys.argv)
    label = QLabel("Hello World")
    label.show()
    app.exec_()
    sys.exit()

def test():
    from selenium import webdriver
    options = webdriver.ChromeOptions();
    driver = webdriver.Chrome("E:\chromedriver.exe", chrome_options=options)
    # driver = webdriver.Firefox()



if __name__ == '__main__':
    test()
