import csv

with open('ExpressLanesTrafficWithTolls-2014_copy.csv', 'rb') as csvfile:
     trafficDataRaw = csv.reader(csvfile, delimiter=',', quotechar='|')
     trafficDataRaw.next()
     for row in trafficDataRaw:
       	if row[4] != '':
       		row[4] = int(row[4])
          # else row[4] == '':
          #      row[4] = 0
       	if row[3] != '':
       		row[3] = int(row[3])
          # else row[3] == '':
          #      row[3] = 0
       	if row[2] != '' or row[2] != "HOV ONLY" or row[2] != " ":
       		row[2] = float(row[2])
     	# else row[2] == '' or row[2] == " " or row[2] == "HOV ONLY":
      #          row[2] = 0
        #print row



        



     # trafficData = list(trafficDataRaw)
     # print trafficData
          #print ("Row #" + str(trafficDataRaw.line_num) + ' ' + str(row))
     
