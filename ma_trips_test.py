from distutils.command import check
from turtle import width
#from metabasepy import Client
import pprint
import pandas as pd


'''
# metabase credentials to access the dbs
cli = Client(username="jawakar@raaho.in", password="92LjKfzOt1Xvqm", base_url="http://3.6.54.230:3000/metabase/")
cli.authenticate()

def get_dbs():
    all_dbs = cli.databases.get()
    pprint.pprint(all_dbs, width=-1)

get_dbs()

def export_as_CSV(db_id):
    cli.dataset.export(database_id=db_id, query="select * from ma_trips;", export_format="csv")

export_as_CSV(7)
'''

import pandas as pd
df = pd.read_csv("G:\Cdrive\Desktop\scripts\Pytest\query_result_2022-03-27.csv")


from datetime import datetime, timedelta
yesterday_date = datetime.strftime(datetime.now() - timedelta(2), '%Y-%m-%dT%H:%M:%S')
df['updated_at'] = df['updated_at'].astype(pd.StringDtype())
filtered_df = df[(df['updated_at']) > (yesterday_date)]

import pytest
import logging
logging.basicConfig(filename='test.log', format='%(asctime)s,%(msecs)03d %(levelname)s %(message)s', 
level=logging.WARNING, datefmt='%Y-%m-%dT%H:%M:%S')

def check_unique_indents(filtered_df):
    boolean = filtered_df['indent_no'].is_unique
    return boolean

def test_unique_indents():
    result = check_unique_indents(filtered_df)
    if result == False:
        logging.warning('indent numbers repeat')
    assert result

test_unique_indents()