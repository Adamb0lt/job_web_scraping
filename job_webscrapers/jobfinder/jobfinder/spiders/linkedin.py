from linkedin_login import login_linkedin
import scrapy


class LinkedinSpider(scrapy.Spider):
    name = "linkedin"
    allowed_domains = ["www.linkedin.com"]
    start_urls = ["https://www.linkedin.com/feed/"]

    def parse(self, response):
        #
