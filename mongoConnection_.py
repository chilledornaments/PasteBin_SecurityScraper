from pymongo import MongoClient
import config
CONFIG = config.Config

def MongoPost_(KW, LINK, RAW):
    
    client = MongoClient(CONFIG.MONGO_URL)
    
    # DB will be created if it doesn't already exist
    db = client[CONFIG.MONGO_DB_NAME]
    paste_info = db.pastes
    paste_data = {
        'Keyword': KW,
        'PastebinLink': LINK,
        'RawData': RAW
    }
    paste_info.insert_one(paste_data)
