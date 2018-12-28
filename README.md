# PasteBin_SecurityScraper
A tool to scrape new Pastebin Pastes and search for potential breaches

## Configuration

All configuration is done in `config.py`. Notable configurations:

`SLACK`. Boolean. Default: False

If set to False, no Slack alerts will be sent. If set to true, a Slack alert will be sent to the configured channel. The alert will include the keyword hit and the URL for the paste.

`MONGO`. Boolean. Default: False

If set to False, nothing is written to MongoDB. If set to true, `pastebin-scraper.py` will add the keyword hit, the URL, and the raw paste text to the MongoDB DB configured in `MONGO_DB_NAME`. Authentication is theoretically supported, though I haven't tested it. There's an example in `config.py` of Mongo Auth.

## Intended Use

This is intended to be an extra eye for you, so to say. For best results, log everything to Mongo and configure Slack. 

The purpose of writing to Mongo is to avoid having nothing but useless, long-since-deleted links. 

Pastebin's scraping API has a 2 minute delay, so there's not much sense in running this script more frequently than every 2 minutes. That said, I don't care what you do.


