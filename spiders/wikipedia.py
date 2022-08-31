from asyncio.windows_events import NULL
import scrapy
from scrapy.http import Request
import csv


# with open('movies.csv', 'w', encoding='utf-8', newline='') as csv1:
#     fields = ['name', 'genre', 'actor', 'director', 'country', 'year']
#     writer = csv.DictWriter(csv1, fields, delimiter=',')
#     writer.writeheader()




class WikipediaSpider(scrapy.Spider):
    name = 'wikipedia'
    allowed_domains = ['en.wikipedia.org', 'ru.wikipedia.org']
    start_urls = [
        f'https://en.wikipedia.org/wiki/List_of_films:_A',
        f'https://en.wikipedia.org/wiki/List_of_films:_A',
        f'https://en.wikipedia.org/wiki/List_of_films:_C',
        f'https://en.wikipedia.org/wiki/List_of_films:_D',
        f'https://en.wikipedia.org/wiki/List_of_films:_E',
        f'https://en.wikipedia.org/wiki/List_of_films:_F',
        f'https://en.wikipedia.org/wiki/List_of_films:_G',
        f'https://en.wikipedia.org/wiki/List_of_films:_H',
        f'https://en.wikipedia.org/wiki/List_of_films:_I',
        f'https://en.wikipedia.org/wiki/List_of_films:_J%E2%80%93K',
        f'https://en.wikipedia.org/wiki/List_of_films:_L',
        f'https://en.wikipedia.org/wiki/List_of_films:_M',
        f'https://en.wikipedia.org/wiki/List_of_films:_N%E2%80%93O',
        f'https://en.wikipedia.org/wiki/List_of_films:_P',
        f'https://en.wikipedia.org/wiki/List_of_films:_Q%E2%80%93R',
        f'https://en.wikipedia.org/wiki/List_of_films:_S',
        f'https://en.wikipedia.org/wiki/List_of_films:_T',
        f'https://en.wikipedia.org/wiki/List_of_films:_U%E2%80%93W',
        f'https://en.wikipedia.org/wiki/List_of_films:_X%E2%80%93Z',
        f'https://en.wikipedia.org/wiki/List_of_films:_numbers'
    ]
    
            


    def parse(self, response):
        films_hrefs_list_a_eng = response.xpath('//@href').getall()

        for film in films_hrefs_list_a_eng:
            yield Request (f'https://en.wikipedia.org{film}', self.parse_single_film_en)
    
    
    def parse_single_film_en(self, response):
            link = str(response.xpath('//*[@lang="ru"]/@href').get())
            
            if link != 'None':
                #print('ПРИВЕТ ВСЕ НОРМ')
                #print(f'ССЫЛКА: {link}')
                yield Request (f'{link}', self.parse_single_film_ru)
            #else:
            #    pass
    
    def parse_single_film_ru(self, response):
        imdb = response.xpath('//span[@data-wikidata-property-id="P345"]').get()
        if imdb:
            name = response.xpath('//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[1]/th[1]/text()').get() 
            if name:
                pass
            else:
                name = response.xpath('//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[1]/th/text()').get() 
            
            genre = response.xpath('//span[@data-wikidata-property-id="P136"]/a/text()').getall()
            if genre == []:
                genre = response.xpath('//span[@data-wikidata-property-id="P136"]//text()').getall()
                if genre == []:
                    genre = genre = response.xpath('//span[@data-wikidata-property-id="P136"]/text()').getall()
            
            actor = response.xpath('//span[@data-wikidata-property-id="P161"]//a/text()').getall()
            if actor == []:
                actor = response.xpath('//div[@data-wikidata-property-id="P161"]//a/text()').getall()
                if actor == []:
                    actor = response.xpath('//span[@data-wikidata-property-id="P161"]/text()').getall()
                    if actor == []:
                        actor = response.xpath('//div[@data-wikidata-property-id="P161"]/text()').getall()

            director = response.xpath('//span[@data-wikidata-property-id="P57"]//a/text()').getall()
            if director == []:
                director = response.xpath('//span[@data-wikidata-property-id="P57"]/text()').getall()

            country = response.xpath('//span[@data-wikidata-property-id="P495"]//a/span/text()').getall()
            x = ' '
            y = '\xa0'
            if country == [] or y in country or x in country or country == [' ', ' ']:
                country = response.xpath('//span[@data-wikidata-property-id="P495"]/a/text()').getall()
                if country == [] or y in country or x in country or country == [' ', ' ']:
                    country = response.xpath('//span[@class="country-name"]//a/text()').getall()
                    if country == [] or y in country or x in country or country == [' ', ' ']:
                        country = response.xpath('//span[@data-wikidata-property-id="P495"]//a/text()').getall()
                        if country == [] or y in country or x in country:
                            country = response.xpath('//span[@data-wikidata-property-id="P495"]//a/span//text()').getall()
                            if country == [] or y in country or x in country:
                                country = response.xpath('//span[@data-wikidata-property-id="P495"]/span/text()').getall()
                            
                            
            
            year = str(response.xpath('//span[@class="dtstart"]/text()').getall()).strip()

            if year == [] or y in year or x in year or len(str(year)) < 8:
                year = str(response.xpath('//span[@data-wikidata-property-id="P577"]/a/text()').getall()).strip
                if year == [] or y in year or x in year or len(str(year)) < 8:
                    year = str(response.xpath('//span[@data-wikidata-property-id="P577"][1]//a/text()').getall()).strip()
                    if year == [] or y in year or x in year or len(str(year)) < 8:
                        year = str(response.xpath('//span[@data-wikidata-property-id="P577"]/text()').getall()).strip()
                        if year == [] or y in year or x in year or len(str(year)) < 8:
                            year = str(response.xpath('//span[@data-wikidata-property-id="P580"]//a/text()').getall()).strip
                            if year ==[] or y in year or x in year or len(str(year)) < 8:
                                year = str(response.xpath('//td[@class="plainlist"]/a/text()').getall()).strip()
                                if year == [] or y in year or x in year or len(str(year)) < 8:
                                    year = str(response.xpath('//span[@class="nowrap"]/text()').getall()).strip()
            #year = year.replace("'", '').replace("[", '').replace("]", '')
            # year = year
            # year = year
                                
                                
            
            #movie = {'name': name, 'genre': genre, 'actor': actor, 'director': director, 'country': country, 'year': year}
            #print(movie)
            # with open('movies.csv', 'a', encoding='utf-8', newline='') as csv1:
            #     fields = ['name', 'genre', 'actor', 'director', 'country', 'year']
            #     writer = csv.DictWriter(csv1, fields, delimiter=',')
            #     writer.writerow(movie)
            yield {
            'film_name': str(name).replace("'", '').replace("[", '').replace("]", ''),
            'director':str(director).replace("'", '').replace("[", '').replace("]", ''),
            'genre':str(genre).replace("'", '').replace("[", '').replace("]", ''),
            'year':str(year).replace("'", '').replace("[", '').replace("]", ''),
            'country':str(country).replace("'", '').replace("[", '').replace("]", ''),
            'actors': str(actor).replace("'", '').replace("[", '').replace("]", '')
            }


        