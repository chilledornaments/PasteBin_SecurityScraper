#!/usr/bin/env python3

import requests, json, threading, time
from queue import Queue
try:
    import config
    print("imported config")
except Exception as e:
    print("unable to import config")
    print(str(e))
CONFIG = config.Config

if CONFIG.MONGO:
    import mongoConnection_

def PB_Scraper():
    print(CONFIG.KEYWORD_LIST)

    # Get latest pastes
    NEW_PASTES = requests.get(CONFIG.PASTEBIN_API_URL)
    NEW_PASTES_JSON = json.loads(NEW_PASTES.text)
    
    for new_post in NEW_PASTES_JSON:
        NEW_PASTE_KEY = new_post['key']
        PASTE_TO_CHECK = CONFIG.PASTEBIN_PASTE_URL+NEW_PASTE_KEY
        RAW_PASTE = requests.get(PASTE_TO_CHECK).text.lower()
        for KEYWORD in CONFIG.KEYWORD_LIST:
            if KEYWORD in RAW_PASTE:
                print("{} found in: {}".format(KEYWORD, str(PASTE_TO_CHECK)))
                if CONFIG.SLACK:
                    SlackAlert(KEYWORD, PASTE_TO_CHECK)
                if CONFIG.MONGO:
                    mongoConnection_.MongoPost_(KEYWORD, PASTE_TO_CHECK, RAW_PASTE)

if CONFIG.SLACK:
    def SlackAlert(KEYWORD, PASTEBIN_URL):
        HEADER = {'Content-Type': 'application/json'}
        SLACK_MESSAGE = "Alert: {} found in {}".format(KEYWORD, PASTEBIN_URL)
        JSON_DATA = {}

        JSON_DATA['channel'] = CONFIG.SLACK_CHANNEL
        JSON_DATA['icon_emoji'] = CONFIG.SLACK_ICON
        JSON_DATA['username'] = CONFIG.SLACK_USER
        JSON_DATA['attachments'] = [{
            'title': "PasteBin Alert",
            'color': '#439FE0',
            'fallback': "PasteBin Alert",
            'text': SLACK_MESSAGE
        }]
        try:
            requests.post(CONFIG.SLACK_WEBHOOK, data=json.dumps(JSON_DATA), headers=HEADER)
            print("Success")
            
        except Exception as e:
            print(str(e))



if __name__ == '__main__':
    scrape = threading.Thread(target=PB_Scraper)
    scrape.start()

