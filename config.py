import os
class Config(object):

    PASTEBIN_LIMIT = "250"
    # For scraping initially
    PASTEBIN_API_URL = "https://scrape.pastebin.com/api_scraping.php?limit="+PASTEBIN_LIMIT
    # Note, you don't need an API key, just a whitelisted IP
    PASTEBIN_PASTE_URL = "https://scrape.pastebin.com/api_scrape_item.php?i="
    
    # Keywords are used for defining what you're looking for (i.e. company name)

    # You can give an absolute path -- if you do, comment out the current KEYWORDS_FILE
    # If running a cron outside of your home directory, I recommend specifying the full path

    # KEYWORDS_FILE = "/path/to/keywords/file.txt"
    
    # Or you can edit the existing keywords.txt 
    KEYWORDS_FILE = os.path.join(os.getcwd(), "keywords.txt")
    KEYWORD_LIST = []
    with open(KEYWORDS_FILE, "r") as KWF:
        for line in KWF:
            line = line.strip('\n')
            KEYWORD_LIST.append(line)
    KWF.close()    

    # True or false, should a Slack notification be sent?
    SLACK = False
    # If set to True, provide these values
    # Incoming webhook
    SLACK_WEBHOOK = ""
    # Channel to post in
    SLACK_CHANNEL = ""
    # Icon for message
    SLACK_ICON = ""
    # Username to post as
    SLACK_USER = ""

    # Mongo Settings
    # Set to true to store in Mongodb
    MONGO = False
    MONGO_PORT = 27017
    MONGO_DB_NAME = 'pastebin_scraper'
    # Of course, replace localhost with remote host if necessary
    # Mongo times out for me when the port isn't an int, so here we are
    MONGO_URL = 'mongodb://localhost:%i' %(MONGO_PORT)
    

    # If the database requires authentication:
    # MONGO_URL = 'mongodb://username:password@host:%i' %(MONGO_PORT)

    
    