import json 
import pandas as pd 
from pandas.io.json import json_normalize #package for flattening json in pandas df
import osm_api as api



def process_data(inputJSON, city_name):
    subway_data = json_normalize(data=inputJSON['elements'], 
                                 meta=['type','id', 'nodes','tags'],
                                 errors='ignore',
                                 record_prefix='_')
    df = pd.DataFrame(subway_data.head(len(subway_data)))
    print(list(df))
    if len(df) ==0:
        print("%%%%%%%%    NO DATA FOUND   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        quit()

    pd.set_option('display.max_columns', 10)
    pd.set_option('display.max_rows', 50)
    pd.set_option('display.width', 2000)

    #print((df))
    #--------NODE DATA-------------------------------------------------------------------
    nodes_df = df.loc[df['type'] == 'node']
    #print(nodes_df[['id','lat','lon','type','tags.name']])

    nodes_ids = nodes_df['id']
    nodes_lats = nodes_df['lat']
    nodes_lons = nodes_df['lon']

    #--------WAY DATA--------------------------------------------------------------------
    #nodes need to all belong to a way and get its way_id as its lineSegmentIndex
    #each node has a way_id, which represents its lineSegment

    ways_df = df.loc[df['type'] == 'way']
    #print(ways_df)
    ways_ids = ways_df['id']
    ways_node_arrays = ways_df['nodes']
    ways_colours = ways_df['tags.name:en']
    #ways_colours = ways_df['tags.colour']

    ways_ids_list = []
    for x in range(len(ways_ids)):
        ways_ids_list += [ways_ids.iloc[x]]


    lineSegmentIndex = []
    nodes_colour = []
    ways_id = 0 
    ways_list = []    

    #for x in range(len(ways_node_arrays)):
    #    print("ways node arrays", ways_node_arrays)

    for x in range(len(ways_ids)):
    #    print("x   ", x)
    #    print("ways ids iloc   ", ways_ids.iloc[x])
    #    print("ways node arrays   ", ways_node_arrays.iloc[x])
        ways_list  += [[ways_ids.iloc[x], ways_node_arrays.iloc[x]]] 


    nodes_ids_list = []

    for x in range(len(nodes_ids)):
        nodes_ids_list += [int(nodes_ids.iloc[x])]

    for x in range(len(nodes_ids_list)):
        #check
        for y in range(len(ways_list)):
            if (nodes_ids_list[x] in ways_list[y][1]):
                #connect
                lineSegmentIndex += [ways_list[y][0]]

    #--------Arrange by line sections----------------------------------------------------
    node_array = []
    for x in range(len(nodes_ids)):
       node_array  += [[city_name , 
                        nodes_ids.iloc[x] , 
                        lineSegmentIndex[x], 
                        nodes_lats.iloc[x], 
                        nodes_lons.iloc[x]]]

    ordered_ids = []
    for x in range(len(ways_list)):
        for y in range(len(ways_list[x][1])):
             ordered_ids += [ways_list[x][1][y]] 
    print()
    print()
    #new order that arrays should be called in
    new_order = []
    for x in range(len(nodes_ids_list)):
        new_order += [nodes_ids_list.index((ordered_ids[x]))]

    #--------LINE Printout--------------------------------------------------------------

    lines_header = "city, nodeID, lineSegmentIndex, latitude, longitude, colour, service\n"
    lines_header = "city, nodeID, lineSegmentIndex, latitude, longitude, lineName, service\n"
    lines_list = ""


    for x in range(len(nodes_ids)):
        #print(type(nodes_service[new_order[x]]))
        #if (nodes_service[new_order[x]] == 'nan'):
        #if (lineSegmentIndex[new_order[x]] == 708859444):
            lines_list += (str(city_name) + ", "
                       + str(nodes_ids.iloc[new_order[x]]) + ", " 
                       + str(lineSegmentIndex[new_order[x]]) + ", "
                       + str(nodes_lats.iloc[new_order[x]]) + ", " 
                       + str(nodes_lons.iloc[new_order[x]]) + "\n")

    #remove last 'new line character'
    lines_list = lines_list[:-1] 
    return lines_list


#process_data(inputJSON)


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
