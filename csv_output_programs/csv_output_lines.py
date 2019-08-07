#set env variable PYTHONIOENCODING=utf_8

filename = 'lines.csv'

coordlist = [] 
coordlist += [["0755",0,114.118666, 22.532083]] 
coordlist +=[["0755",0,114.118932, 22.533262]]
coordlist += [["0755",0,114.11898, 22.533468]]
coordlist += [["0755",0,114.119126, 22.534242]] 
coordlist += [["0755",0,114.119159, 22.53443]]
coordlist += [["0755",1,114.119175, 22.534614]]
coordlist += [["0755",1,114.118983, 22.538809]]
coordlist += [["0755",1,114.118909, 22.53968]]
coordlist += [["0755",1,114.118834, 22.540552]]

print()
headerstring = "city,linesegmentindex, latitude, longitude\n" 
writestring = ""

for x in range(len(coordlist)): 
     writestring += (str(coordlist[x][0])+', ' 
                 + str(coordlist[x][1])+', ' 
                 + str(coordlist[x][2])+', ' 
                 + str(coordlist[x][3])+'\n' )

with open(filename, 'w', encoding='utf-8') as file:
    file.write(headerstring)
    file.write(writestring)

with open(filename, 'r', encoding='utf-8') as file:
    print('-------- - -  -   -   file contents:\n\n',file.read())


#--------------goal-------------------------
#city, lineSegmentIndex, latitude, longitude
#0755, 0, 114.118666, 22.532083
#0755, 0, 114.118666, 22.532083
#0755, 0, 114.118666, 22.532083
#0755, 1, 114.118666, 22.532083
#0755, 1, 114.118666, 22.532083
#0755, 1, 114.118666, 22.532083











