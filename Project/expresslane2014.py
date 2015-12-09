# Which month has the most number of cars?
# Which week has the most number of cars?
# Which day has the most number of cars?
# Which hour has the most number of cars?
# Which direction (237 Westbound or 237 Eastbound) has the most number of cars?

import csv
# Open the csv file
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
     	print row

# Calculate cars monthly
          traffic = trafficDataRaw
          split_traffic = traffic.split(",")
          split_datetime = datetime.split(" ") 
          cars = int(split_traffic[3])
          date = split_traffic[0].split(" ")[0]
          def calculateCarsMonth(cars, date):
               return cars * datetime 

          calculateCarsMonth(cars,date)