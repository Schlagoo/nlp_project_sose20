import scrapy
import urllib.parse as urlparse
from urllib.parse import parse_qs


class MoviesSpider(scrapy.Spider):
    name = "movies"
    start_urls = [
        "https://www.imdb.com/search/title/?groups=top_250&sort=user_rating",
    ]

    def parse(self, response):
        parsed = urlparse.urlparse(response.url)
        startIndexStr = parse_qs(parsed.query).get("start")
        pageSize = 50
        page = 1
        if startIndexStr != None and type(startIndexStr) == list:
            startIndex = int(startIndexStr[0], base=10)
            page = int((startIndex - 1) / 50 + 1)

        for movie in response.css("div.lister-item-content"):
            yield {
                "title": movie.css(".lister-item-header a::text")[0].get(),
                "date": movie.css(".lister-item-header .lister-item-year::text")[0].get().replace('(', '').replace(')', ''),
                "rank": movie.css(".lister-item-header .lister-item-index::text")[0].get().replace('.', '')
            }
            next_page = response.css(
                "a.lister-page-next.next-page::attr(href)").get()
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)
