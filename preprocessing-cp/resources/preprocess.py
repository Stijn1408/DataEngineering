import os

from flask import jsonify
# from google.cloud import storage
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
from statsmodels.sandbox.regression.sympy_diff import df
import pandas as pd
import sqlalchemy as db
from sqlalchemy import Column, Float, Table, Integer
from sqlalchemy.ext.declarative import declarative_base

# class DBUtil:
#
#     def __init__(self, dataset):
#         # The database URL is provided as an env. variable
#         if 'DB_URL' in os.environ:
#             db_url = os.environ['DB_URL']
#         else:
#             db_url = 'sqlite:///features.db'
#         # create the database
#         self.engine = db.create_engine(db_url, echo=True)
#         self._reflect()

# def pd_to_sql(data):
#     if 'DB_URL' in os.environ:
#         db_url = os.environ['DB_URL']
#     else:
#         db_url = 'sqlite:///features.db'
#         # create the database
#     engine = db.create_engine(db_url, echo=True)
#     data = data.to_sql("Table", con=engine, if_exists='replace', index=False)
#     return data
#
    # def _reflect(self):
    #     self.Base = declarative_base()
    #     self.Base.metadata.reflect(self.engine)
    #

def preprocessing(dataset):
    scaler = MinMaxScaler()
    df_scaled = pd.DataFrame(scaler.fit_transform(dataset), columns=dataset.columns)
    #print(len(df_scaled))
    #new_scaled = pd_to_sql(df_scaled)
    print(type(df_scaled))
    return df_scaled


        