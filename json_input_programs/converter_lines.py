import json 
import pandas as pd 
from pandas.io.json import json_normalize #package for flattening json in pandas df
from pandas.io.json import read_json #package for converting json string into pandas objects 

file_name = 'NingboLines.json'

#load json object
with open(file_name, encoding='utf-8') as f:
    inputJSON = json.load(f)

#manually remove "version data" and only leave elements 
#automate this later
 
subway_data = json_normalize(data=inputJSON['elements'], 
                            meta=['type','id', 'nodes','tags'],
                            errors='ignore',
                            record_prefix='_')
df = pd.DataFrame(subway_data.head(-1))

pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 50)
pd.set_option('display.width', 2000)

#print(list(df))

#--------NODE DATA----------------------------------------------------
nodes_df = df.loc[df['type'] == 'node']
#print(nodes_df[['id','lat','lon','type','tags.name']])

nodes_ids = nodes_df['id']
nodes_lats = nodes_df['lat']
nodes_lons = nodes_df['lon']
nodes_types = nodes_df['type']

#--------WAY DATA----------------------------------------------------
#nodes need to all belong to a way and get its way_id as its lineSegmentIndex
#each node has a way_id, which represents its lineSegment

ways_df = df.loc[df['type'] == 'way']
#print(ways_df[['id','nodes','type','tags.colour']])

ways_ids = ways_df['id']
ways_node_arrays = ways_df['nodes']
ways_colours = ways_df['tags.colour']

#print(ways_ids)
#print(ways_node_arrays)
#print(ways_colours)

ways_ids_list = []
for x in range(len(ways_ids)):
    ways_ids_list += [ways_ids.iloc[x]]

#print(ways_ids_list)



lineSegmentIndex = []
ways_id = 0 
ways_list = []    

for x in range(len(ways_ids)):
   ways_list  += [[ways_ids.iloc[x], ways_node_arrays[x]]] 

nodes_ids_list = []
for x in range(len(nodes_ids)):
    nodes_ids_list += [int(nodes_ids.iloc[x])]

for x in range(5):
    print("Way ID", ways_list[x][0],"\nNodes in this way   ",  ways_list[x][1], "\n")

for x in range(len(nodes_ids_list)):
    #check
    for y in range(len(ways_list)):

        #print(x, " of ", len(nodes_ids_list))
        #print(y, " of ", len(ways_list))
        #print("if (", nodes_ids_list[x])
        #print(" in ", ways_list[y][1],"):")
        #print(type(nodes_ids_list[x]))
        #print(type(ways_list[y][1][0]))
        if (nodes_ids_list[x] in ways_list[y][1]):
            #connect
            lineSegmentIndex += [ways_list[y][0]]
#--------LINE Printout----------------------------------------------------

lines_header = "city, lineSegmentIndex, latitude, longitude"
lines_list = ""
for x in range(len(nodes_ids)):
   lines_list  += (str(nodes_ids.iloc[x]) + ", " 
               + str(lineSegmentIndex[x]) + ", "
               + str(nodes_lats.iloc[x]) + ", " 
               + str(nodes_lons.iloc[x]) + "\n")


print(lines_header)
print(lines_list)

