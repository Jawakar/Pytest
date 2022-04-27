from codeop import CommandCompiler
import pandas as pd
import pytest
import logging

logging.basicConfig(filename='test.log', level=logging.WARNING, 
format='%(asctime)s:%(levelname)s:%(message)s')

df = pd.read_csv("G:\Cdrive\Desktop\scripts\Pytest\query_result_2022-03-19T152151.761Z.csv")

# method to check null values from livin_hist
def find_null(df):
    ans = df.isna().sum()
    count = 0
    for i in ans:
        if i>0 :
            count = count+1
    return count

# test method to check
def test_data():
    ans = find_null(df)
    if ans>0:
        logging.warning('{} Null values exists'.format(ans))
    assert ans==0

test_data()