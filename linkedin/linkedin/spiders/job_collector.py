import os
import dotenv
import scrapy


def build_url() -> str:
    query = os.environ["SCRAPY_QUERY"]
    query = query.replace(" ", "%20")
    location = os.environ["SCRAPY_LOCATION"]
    base_url = (
        "https://www.linkedin.com/jobs/search"
        f"?keywords={query}"
        f"&location={location}"
        "&position=1"
        "&pageNum=0"
    )
    return base_url


def parse_detail_page(job: scrapy.http.Response) -> dict:
    text_description = job.xpath(
        "//section[1]/div/div/section[1]/div/div/section"
    ).getall()
    title = job.xpath(
        "//section[1]/div/section[2]/div/div[1]/div/h1/text()"
    ).get()
    yield {"title": title, "url": job.url, "text": text_description}


class JobCollectorSpider(scrapy.Spider):
    name = "job_collector"
    allowed_domains = ["*"]

    def start_requests(self):
        dotenv.load_dotenv(
            os.path.join(os.path.dirname(__file__), '../../../config.env'))
        yield scrapy.Request(url=build_url(), callback=self.parse)

    def parse(
            self, response: scrapy.http.Response, **kwargs
    ) -> scrapy.Request:
        for job in response.xpath(
                "//ul[@class='jobs-search__results-list']/li/div/a/@href"
        ).getall():
            yield scrapy.Request(
                job,
                callback=parse_detail_page,
            )
