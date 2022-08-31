import scrapy
from scrapy.http import Request
import csv


class torrentspider(scrapy.Spider):
    name = 'torrent'
    allowed_domains = ['kinozal.tv']

    def start_requests(self):
        with open('movies.csv', newline='',encoding='utf-8') as f:
            reader = csv.reader(f)
            for line in reader:
                url = f'http://kinozal.tv/browse.php?s={line[0]}&g=0&c=1002&v=0&d={line[5]}&w=0&t=0&f=0'
                yield Request(url,meta = {'proxy':'http://113.176.195.145:4153'})

    def parse(self,response):
        href = response.xpath("//a[@class='r1']/@href").get() 
        yield Request(f'http://kinozal.tv{href}',
                        callback = self.parse_single_film,
                        meta = {'proxy':'http://113.176.195.145:4153'}
                    )

    def parse_single_film(self,response):

        film_name = response.xpath('//*[@id="main"]/div[2]/div/div[3]/div[2]/h2/text()[1]').get()
        actor_1 = response.xpath('//*[@id="main"]/div[2]/div/div[3]/div[2]/h2/a[2]/text()').get()
        actor_2 = response.xpath('//*[@id="main"]/div[2]/div/div[3]/div[2]/h2/a[3]/text()').get()
        actor_3 = response.xpath('//*[@id="main"]/div[2]/div/div[3]/div[2]/h2/a[4]/text()').get()
        actor_4 = response.xpath('//*[@id="main"]/div[2]/div/div[3]/div[2]/h2/a[5]/text()').get()
        year = response.xpath('//*[@id="main"]/div[2]/div/div[3]/div[2]/h2/text()[5]').get()
        director = response.xpath('//*[@id="main"]/div[2]/div/div[3]/div[2]/h2/a[1]/text()').get()
        genre = response.xpath('//*[@id="main"]/div[2]/div/div[3]/div[2]/h2/text()[7]').get()
        country = response.xpath('//*[@id="main"]/div[2]/div/div[3]/div[2]/h2/text()[9]').get()
        if 'СССР' in str(genre) or 'Россия' in str(genre):
            genre = response.xpath('//*[@id="main"]/div[2]/div[1]/div[3]/div[2]/h2/text()[5]').get()
            country = response.xpath('//*[@id="main"]/div[2]/div[1]/div[3]/div[2]/h2/text()[7]').get()
            year = response.xpath('//*[@id="main"]/div[2]/div[1]/div[3]/div[2]/h2/text()[3]').get()
        if film_name == None:
            film_name = response.xpath('//*[@id="main"]/div[2]/div[1]/div[3]/div[3]/h2/text()[1]').get()
            actor_1 = response.xpath('//*[@id="main"]/div[2]/div/div[3]/div[3]/h2/a[2]/text()').get()
            actor_2 = response.xpath('//*[@id="main"]/div[2]/div/div[3]/div[3]/h2/a[3]/text()').get()
            actor_3 = response.xpath('//*[@id="main"]/div[2]/div/div[3]/div[3]/h2/a[4]/text()').get()
            actor_4 = response.xpath('//*[@id="main"]/div[2]/div/div[3]/div[3]/h2/a[5]/text()').get()
            year = response.xpath('//*[@id="main"]/div[2]/div/div[3]/div[3]/h2/text()[5]').get()
            director = response.xpath('//*[@id="main"]/div[2]/div[1]/div[3]/div[3]/h2/a[1]/text()').get()
            genre = response.xpath('//*[@id="main"]/div[2]/div[1]/div[3]/div[3]/h2/text()[7]').get()
            country = response.xpath('//*[@id="main"]/div[2]/div[1]/div[3]/div[3]/h2/text()[9]').get()
            if 'СССР' in str(genre) or 'Россия' in str(genre):
                genre = response.xpath('//*[@id="main"]/div[2]/div/div[3]/div[3]/h2/text()[5]').get()
                country = response.xpath('//*[@id="main"]/div[2]/div/div[3]/div[3]/h2/text()[7]').get()
                year = response.xpath('//*[@id="main"]/div[2]/div/div[3]/div[3]/h2/text()[3]').get()

        kp_rating = response.xpath('//*[@id="main"]/div[2]/div/div[2]/ul/li[16]/a/span/text()').get()
        imdb_rating = response.xpath('//*[@id="main"]/div[2]/div/div[2]/ul/li[15]/a/span/text()').get()
        if kp_rating == None:
            kp_rating = response.xpath('//*[@id="main"]/div[2]/div/div[2]/ul/li[15]/a/span/text()').get()
            imdb_rating = response.xpath('//*[@id="main"]/div[2]/div/div[2]/ul/li[14]/a/span/text()').get()
            if kp_rating == None:
                kp_rating = response.xpath('//*[@id="main"]/div[2]/div/div[2]/ul/li[14]/a/span/text()').get()
                imdb_rating = response.xpath('//*[@id="main"]/div[2]/div/div[2]/ul/li[13]/a/span/text()').get()

        poster = response.xpath('//*[@id="main"]/div[2]/div/div[2]/ul/li[1]/a/img/@src').get()

        yield {
            'film_name': film_name,
            'director':director,
            'genre':genre,
            'year':year,
            'country':country,
            'actors': {actor_1,actor_2,actor_3,actor_4},
            'kp_rating': kp_rating,
            'imdb_rating': imdb_rating,
            'poster_url': poster
        }
