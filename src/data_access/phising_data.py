import sys
from typing import List
import os

import numpy as np
import pandas as pd

from src.configuration.mongo_db_connection import MongoDBClient
from src.exception import CustomException
from src.constant import *


class PhisingData:
    """
    This class exports MongoDB collections into pandas DataFrames
    """

    def __init__(self, database_name: str):
        try:
            self.database_name = database_name

            # Mongo URL env se
            self.mongo_url = os.getenv("MONGO_DB_URL")
            if self.mongo_url is None:
                raise Exception("Environment key 'MONGO_DB_URL' not found")

            # MongoDBClient se connection banao
            mongo_client = MongoDBClient(database_name=database_name)
            self.client = mongo_client.client
            self.database = mongo_client.database

        except Exception as e:
            raise CustomException(e, sys)

    def get_collection_names(self) -> List:
        """
        Returns list of collection names from the database
        """
        try:
            return self.database.list_collection_names()

        except Exception as e:
            raise CustomException(e, sys)

    def get_collection_data(self, collection_name: str) -> pd.DataFrame:
        """
        Returns the given collection as pandas DataFrame
        """
        try:
            collection = self.database[collection_name]
            data = list(collection.find())

            df = pd.DataFrame(data)

            # Remove ObjectId column
            if "_id" in df.columns:
                df.drop(columns=["_id"], inplace=True)

            df.replace({"na": np.nan}, inplace=True)
            return df

        except Exception as e:
            raise CustomException(e, sys)

    def export_collections_as_dataframe(self):
        """
        Yields (collection_name, dataframe)
        """
        try:
            collections = self.get_collection_names()

            for name in collections:
                df = self.get_collection_data(name)
                yield name, df

        except Exception as e:
            raise CustomException(e, sys)
