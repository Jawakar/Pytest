import requests
import pprint
from metabasepy import Client
cli = Client(username="jawakar@raaho.in", password="92LjKfzOt1Xvqm", base_url="http://3.6.54.230:3000/metabase/")
cli.authenticate()

#Function to get complete details of all the dbs
def get_dbs():
    all_dbs = cli.databases.get()
    pprint.pprint(all_dbs,width=-1)

#Function to extract
def export_as_CSV(db_id):
    cli.dataset.export(database_id=db_id, query="select * from livinv_history;", export_format="csv")

export_as_CSV(4)
#get_dbs()