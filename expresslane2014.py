import csv

with open('ExpressLanesTrafficWithTolls-2014.csv', 'rb') as csvfile:
     trafficDataRaw = csv.reader(csvfile, delimiter=',', quotechar='|')
     trafficDataRaw.next()
     for row in trafficDataRaw:
     	if row[4] != '':
     		row[4] = int(row[4])
     	if row[3] != '':
     		row[3] = int(row[3])
     	if row[2] != '' or row[2] != "HOV ONLY" or row[2] != " ":
     		row[2] = float(row[2])
     	if row[2] == '' or row[2] == " " or row[2] == "HOV ONLY" or row[3] == '' or row[4] == '':
               row = int(0)
     	print row
