import scrapy
import urllib.parse as urlparse
from urllib.parse import parse_qs


class MoviesSpider(scrapy.Spider):
    name = "movies"
    start_urls = [
        "https://www.imdb.com/search/title/?groups=top_250&sort=user_rating",
        "https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=51&ref_=adv_nxt"
    ]

    def parse(self, response):
        parsed = urlparse.urlparse(response.url)
        startIndexStr = parse_qs(parsed.query).get("start")
        pageSize = 50
        page = 1
        if startIndexStr != None and type(startIndexStr) == list:
            startIndex = int(startIndexStr[0], base=10)
            page = int((startIndex - 1) / 50 + 1)

        filename = "posts-%s.html" % page
        with open(filename, "wb") as f:
            f.write(response.body)
