import scrapy
import urllib.parse as urlparse
from urllib.parse import parse_qs
from urllib.parse import urljoin


class MoviesSpider(scrapy.Spider):
    name = "movies"
    start_urls = [
        "https://www.imdb.com/search/title/?groups=top_250&sort=user_rating",
    ]

    def parse_synopsis_page(self, response):
        complete_movie_info = response.meta["main_movie_info"].copy()
        synopsis_text_nodes = response.xpath(
            '//ul[@id="plot-synopsis-content"]/li//text()').getall()
        complete_movie_info["synopsis"] = "".join(synopsis_text_nodes)
        yield complete_movie_info

    def parse(self, response):
        parsed = urlparse.urlparse(response.url)
        startIndexStr = parse_qs(parsed.query).get("start")
        pageSize = 50
        page = 1
        if startIndexStr != None and type(startIndexStr) == list:
            startIndex = int(startIndexStr[0], base=10)
            page = int((startIndex - 1) / 50 + 1)

        for movie in response.css("div.lister-item-content"):
            synopsis_link = movie.css(
                ".lister-item-header a::attr(href)")[0].get() + "plotsummary/"

            main_movie_info = {
                "title": movie.css(".lister-item-header a::text")[0].get(),
                "date": movie.css(".lister-item-header .lister-item-year::text")[0].get().replace('(', '').replace(')', ''),
                "rank": movie.css(".lister-item-header .lister-item-index::text")[0].get().replace('.', '')
            }
            yield response.follow(synopsis_link, callback=self.parse_synopsis_page, meta={"main_movie_info": main_movie_info})
            next_page = response.css(
                "a.lister-page-next.next-page::attr(href)").get()
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)
