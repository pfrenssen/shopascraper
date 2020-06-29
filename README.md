shopa.be scraper
===============

Scrapes the product data from the https://www.shopa.be/ website.


Requirements
------------

* [Pipenv](https://github.com/pypa/pipenv)
* [Scrapy](https://scrapy.org)


Installation
------------

```
$ pipenv install
```


Usage
-----

Scrape the products of the partner named `shop-name` and store the data in `output.json`:

```
$ pipenv run scrapy crawl products -a partner=shop-name -o output.json
```
