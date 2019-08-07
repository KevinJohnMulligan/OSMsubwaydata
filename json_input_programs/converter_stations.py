import json 
import pandas as pd 
from pandas.io.json import json_normalize #package for flattening json in pandas df
from pandas.io.json import read_json #package for converting json string into pandas objects 

file_name = 'NingboStations1.json'

#load json object
with open(file_name, encoding='utf-8') as f:
    inputJSON = json.load(f)

#manually remove version data and only leave elements 
#automate this later
 
subway_data = json_normalize(data=inputJSON['elements'], 
                            meta=['type','id', 'nodes','tags'],
                            errors='ignore',
                            record_prefix='_')
df = pd.DataFrame(subway_data.head(-1))

pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 100)
pd.set_option('display.width', 1000)

print(list(df))

ways_df = df.loc[df['type'] == 'way']
print(ways_df[['id','nodes','type','tags.colour']])

nodes_df = df.loc[df['type'] == 'node']
print(nodes_df[['id','lat','lon','type','tags.name']])

nodes_ids = nodes_df['id']
nodes_lats = nodes_df['lat']
nodes_lons = nodes_df['lon']
nodes_types = nodes_df['type']


nodes_ids_list = []
for x in range(len(nodes_ids)):
    nodes_ids_list += [nodes_ids.iloc[x]]


print(type(nodes_ids))
print(type(nodes_ids_list))
print(nodes_ids_list[0:10])

