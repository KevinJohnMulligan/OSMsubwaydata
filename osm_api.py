from OSMPythonTools.nominatim import Nominatim
from OSMPythonTools.overpass import overpassQueryBuilder
from OSMPythonTools.overpass import Overpass
import json

nominatim = Nominatim()
overpass = Overpass()

encoding="utf-8"

def create_query(line_number, city_name):
    line_num = ('"ref" = "' + line_number + '"')
    query = overpassQueryBuilder(
            area=nominatim.query(city_name).areaId(), 
            elementType=['node', 'way', 'relation'], 
            selector=['"route"="subway"', line_num], 
            out='body;>;out skel qt')

    print("        +++query for line ", line_number, " in ", city_name)
    print(query)
    print("        +++\n")
    return query


def run_query(query):
    output = overpass.query(query)

    json_output = output.toJSON()
    #print(str(json_output))
    json_output = json.dumps(json_output, ensure_ascii=False)
    #print(json_output)
    return json_output


def write_to_file(file_contents, city_name):
    filename = city_name + '_output_lines.json'
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(file_contents)


def get_subway_line(line_number, city_name):
    query_var = create_query(line_number, city_name)
    json_output_var = run_query(query_var)
#    write_to_file(json_output_var, city_name)
    return json_output_var

#test run
#get_subway_line("1", 'Shenzhen')
