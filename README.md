# Article Crawler
 An application that allows you to scrape articles, titles and author names from news websites such as theguardian.com using Scrapy, stores the data in a hosted mongodb database and allows you to conduct keyword search.
 
 ## Installation
 
 Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Scrapy.

```bash
pip install scrapy
```

## Usage
First start the application "TheGuardian.exe" if you're using the application for the first time you might want to check the "Refresh documents" box
![TheGuardian](https://github.com/Elhaouri98/Article-Crawler/raw/master/screenshots/1.png)

## Setting up a search API

We will be storing the data in a hosted mongodb atlas cluster
![TheGuardian](https://github.com/Elhaouri98/Article-Crawler/raw/master/screenshots/2.png)

And Then we're gonna use mongodb stitch to create an API that allows us to insert the data crawled by our spider to our cluster
![TheGuardian](https://github.com/Elhaouri98/Article-Crawler/raw/master/screenshots/3.png)

To build the API that allows us to search by keyword we're gonna be using mongodb Stitch
![TheGuardian](https://github.com/Elhaouri98/Article-Crawler/raw/master/screenshots/5.png)

In stitch we're connect to our cluster create a search function and add text indexing to our collection
![TheGuardian](https://github.com/Elhaouri98/Article-Crawler/raw/master/screenshots/6.png)
![TheGuardian](https://github.com/Elhaouri98/Article-Crawler/raw/master/screenshots/4.png)

## Conclusion 

As a beginner this was the first time I used the Scrapy Framework, I had a good time learning about the whole subject of web scraping. Working with both MongoDb Atlas and Stitch was just as interesting, it is a powerful tool with a lot of utility that's opened a new door for me and an opportunity to learn new things. 
