# Which month has the `most number of cars?
# Which week has the most number of cars?
# Which day has the most number of cars?
# Which hour has the most number of cars?
# Which direction (237 Westbound or 237 Eastbound) has the most number of cars?

import csv

import datetime

# Open the csv file
with open('ExpressLanesTrafficWithTolls-2014.csv', 'rb') as csvfile:
     trafficDataRaw = csv.reader(csvfile, delimiter=',', quotechar='|')
     trafficDataRaw.next()
     print trafficDataRaw.next()
     traffic_month = {"jan": 0, "feb": 0, "mar": 0, "dec": 0,
     "apr": 0, "nov": 0}

     traffic_hours = {"am5": 0}

     for row in trafficDataRaw:
          row[3] = int(row[3])
          date = row[0].split(" ")
          date_str = date[0]
          time= date[1]
          # print date_str
          # print time
          if time[0] == '5':
               traffic_hours['am5'] +=row[3]
          
          # if row[4] != '':
     	# 	row[4] = int(row[4])
     	# if row[3] != '':
     	# 	row[3] = int(row[3])
     	# if row[2] != '' or row[2] != "HOV ONLY" or row[2] != " ":
     	# 	row[2] = float(row[2])
          if row[0][0:2] == "1/":
               traffic_month['jan'] +=row[3]         
          elif row[0][0:2] == "2/":
               traffic_month['feb'] +=row[3] 
          elif row[0][0:2] == "3/":
               traffic_month['mar']+=row[3] 
          elif row[0][0:2] == "4/":
               traffic_month['apr'] +=row[3] 

          if row[0][0:3] == "11/":
               traffic_month['nov'] +=row[3] 
          elif row[0][0:3] == "12/":
               traffic_month['dec'] +=row[3] 

     # print "jan", jan
     # print "dec:", dec
          #print row
     print "jan", traffic_month['jan']      
     print "feb", traffic_month['feb']
     print "mar", traffic_month['mar']
     print "apr", traffic_month['apr']
     print "nov", traffic_month['nov']
     print "dec", traffic_month['dec']

     print traffic_hours['am5']/365


# # Calculate cars monthly
#           traffic = trafficDataRaw
#           split_traffic = traffic.split(",")
#           split_datetime = datetime.split(" ") 
#           cars = int(split_traffic[3])
#           date = split_traffic[0].split(" ")[0]
#           def calculateCarsMonth(cars, date):
#                return cars * datetime 

#           calculateCarsMonth(cars,date)