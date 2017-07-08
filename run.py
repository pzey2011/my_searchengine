#!/usr/bin/python
# filename: run.py
import os
import sqlite3
import re
from crawler import Crawler, CrawlerCache



if __name__ == "__main__":
    database_name = "crawler.txt"

    # Using SQLite as a cache to avoid pulling twice
    crawler = Crawler()
    root_re = re.compile('^/$').match
    crawler.crawl('http://www.tabnak.ir/', no_cache=root_re)
    try :
        print(crawler.content['tabnak.ir'])
    except KeyError as e:
        print(e)
