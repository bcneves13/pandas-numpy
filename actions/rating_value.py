import pandas as pd
import numpy as np
from natsort import index_natsorted
from .sanitize import sanitize

columns = ["id","track_name","size_bytes","currency","price","rating_count_tot","rating_count_ver","user_rating","user_rating_ver","ver","cont_rating","prime_genre","sup_devices.num","ipadSc_urls.num","lang.num","vpp_lic"]
def rating_value(prime_genere, sort_by, output, top):
    df = pd.read_csv('AppleStore.csv', names=columns)
    if type(prime_genere) == list:
        df = df[(df['prime_genre'].isin(prime_genere))]
    else:
        df = df[(df['prime_genre'] == prime_genere)]
    df = sanitize(df, sort_by)
    df = df.sort_values(sort_by, ascending=False)

    # # result = df.to_numpy()
    # # resultdf = pd.DataFrame(result, columns)
    pd.DataFrame(df.iloc[:top]).to_csv('csvs/'+output+'.csv')
    pd.DataFrame(df.iloc[:top]).to_json('jsons/'+output+'.json', orient='records')