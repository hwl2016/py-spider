# encoding=utf-8

# scrapy 框架
# 安装 python -m pip install scrapy
# 创建项目： scrapy startproject xxx(项目名)
# 创建爬虫： scrapy genspider country example.webscraping.com --template=crawl
# 运行项目： scrapy crawl country -s LOG_LEVEL=DEBUG
#            scrapy crawl country --output=countries.csv -s LOG_LEVEL=INFO

# 运行项目可能回报错：ImportError: No module named win32api
# python -m pip install pypiwin32

# shell 命令抓取
# scrapy shell http://example.webscraping.com/places/default/view/Albania-3