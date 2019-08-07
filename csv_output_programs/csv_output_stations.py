#set env variable PYTHONIOENCODING=utf_8

filename = 'stations.csv'

stationlist = []
stationlist += [["0755", "LouHu", "罗湖", 114.118666, 22.532083]] 
stationlist += [["0755", "Guo", "国贸", 114.118909, 22.53968]]

print()

headerstring = "city, stationNameEN, stationNameZH, latitude, longitude"
writestring = "" 

for x in range(len(stationlist)):
    writestring += ('\"' + str(stationlist[x][0])+'\", ' + '\"' 
                + str(stationlist[x][1])+'\", ' + '\"' 
                + str(stationlist[x][2])+'\", ' 
                + str(stationlist[x][3])+', ' 
                + str(stationlist[x][4])+'\n')


with open(filename, 'w', encoding='utf-8') as file:
    file.write(writestring)

with open(filename, 'r', encoding='utf-8') as file:
    print('-------- - -  -   -   file contents:\n',file.read())














