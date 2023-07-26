from multiprocessing import Pool
from multiprocessing import cpu_count
import pandas as pd
from modules.dataframe import create_dataframe
from modules.base import client
if __name__ == "__main__":
    num_cores = cpu_count() - 1
    with Pool() as pool:
        data = pd.concat(pool.map(create_dataframe, range(num_cores)))
    data_dict = data.to_dict('records')
    db = client["company"]
    collection = db["employees"]
    collection.insert_many(data_dict)

from pymongo import MongoClient

uri = "mongodb://192.168.101.101:32000/?directConnection=true"
client = MongoClient(uri)
