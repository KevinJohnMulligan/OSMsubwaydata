import json 
import pandas as pd 
from pandas.io.json import json_normalize #package for flattening json in pandas df
import osm_api as api
import format_json_to_csv as rc

city_name = 'Shenzhen'
#city_name = 'Ningbo'
file_name = city_name + '_output_lines.json'
line_number = "1"
city_lines = ["1","2","3"]
city_lines = ["1","2","3","4","5","7","9","11"]




def read_json_file():
    #load json object
    with open(file_name, encoding='utf-8') as f:
        inputJSON = json.load(f)


def create_file(lines_list):
    filename = city_name + '_output_lines.csv'
    with open(filename, 'w', encoding='utf-8') as file:
    #    file.write(lines_header)
        file.write(lines_list)

    #with open(filename, 'r', encoding='utf-8') as file:
    #    print('-------- - -  -   -   file contents:\n',file.read())
    print('end of file')

data = ""
for no in range(len(city_lines)):
    print(" get data for subway line ", city_lines[no], "in ", city_name)
    inputJSON = json.loads(api.get_subway_line(city_lines[no], city_name))
    data += rc.process_data(inputJSON, city_name) + "\n"
    print('                      ------------API queried, JSON data created------------\n\n')

#remove last new line character
data =data[:-1] 
print(data)
create_file(data)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
