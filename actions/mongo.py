from pymongo import MongoClient
import pandas as pd
import numpy as np
from .sanitize import sanitize

def getDatabase():
    CONNECTION_STRING = 'mongodb://localhost:27019/Cognitivo'
    client = MongoClient(CONNECTION_STRING)
    return client['Cognitivo']

def migrateFromCsv():
    client = getDatabase()
    db = client
    columns = ["id","track_name","size_bytes","currency","price","rating_count_tot","rating_count_ver","user_rating","user_rating_ver","ver","cont_rating","prime_genre","sup_devices.num","ipadSc_urls.num","lang.num","vpp_lic"]
    df = pd.read_csv('AppleStore.csv', names=columns)
    df = df.iloc[1:]
    df = sanitize(df, 'rating_count_tot')
    df = sanitize(df, 'rating_count_ver')
    df = sanitize(df, 'size_bytes')
    df = sanitize(df, 'price')
    df.reset_index(inplace=True)
    data_dict = df.to_dict("records")
    db.appleStore.insert_many(data_dict)
