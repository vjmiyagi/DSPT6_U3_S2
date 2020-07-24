import os
import pandas as pd 
import sqlite3
from sqlalchemy import create_engine


url = 'https://raw.githubusercontent.com/vjmiyagi/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module1-introduction-to-sql/buddymove_holidayiq.csv'


df = pd.read_csv(url)
print(df.shape)
print(df.head())


engine = create_engine('sqlite://df.db', echo=True)
sqlite_connection = engine.connect()