import scrapy



class Article(scrapy.Spider):
    name = 'article'
    page=2
    start_urls = [
        'https://www.theguardian.com/world/all'
    ]
    L=''

    def parse(self, response):
        #extracting the articles links that are in world news page
        links = response.xpath("//a[@class='u-faux-block-link__overlay js-headline-text']/@href").extract()
        for link in links:
            self.L=link
            #calling the method that will parse the contents of the current article page
            yield scrapy.Request(url=response.urljoin(link), callback=self.parseparagraph)
        #Going to the next page
        next_page= 'https://www.theguardian.com/world?page='+str(Article.page)
        if Article.page <= 1900:
            Article.page+=1
            yield scrapy.Request(url=next_page, callback=self.parse)
    #Scraping articles along with titles authors and links
    def parseparagraph(self, response):
        Ar=''
        A=response.xpath("//p/text()").getall()
        for i in A:
            Ar+=i
        yield {
            'author' : response.xpath("//a[@rel='author']/span/text()").extract_first(),
            'title' : response.xpath("//title/text()").extract_first(),
            'link' : self.L,
            'article' : Ar
        }