from icrawler.builtin import GoogleImageCrawler

google_crawler = GoogleImageCrawler(storage={'root_dir': 'bag'})
google_crawler.crawl(keyword='bag', max_num=800)


google_crawler = GoogleImageCrawler(storage={'root_dir': 'iphone'})
google_crawler.crawl(keyword='iphone', max_num=800)

google_crawler = GoogleImageCrawler(storage={'root_dir': 'keyboard'})
google_crawler.crawl(keyword='keyboard', max_num=800)

