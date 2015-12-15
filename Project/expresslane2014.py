# Which month has the `most number of cars?
# Which week has the most number of cars?
# Which day has the most number of cars?
# Which hour has the most number of cars?
# Which direction (237 Westbound or 237 Eastbound) has the most number of cars?

import csv
import datetime

# Open the csv file
# def open_data():
#      with open('ExpressLanesTrafficWithTolls-2014.csv', 'rb') as csvfile:
#           trafficDataRaw = csv.reader(csvfile, delimiter=',', quotechar='|')
#           trafficDataRaw.next()
#           return trafficDataRaw
     

def total_2014():
     total_traffic = 0
     with open('ExpressLanesTrafficWithTolls-2014.csv', 'rb') as csvfile:
          trafficDataRaw = csv.reader(csvfile, delimiter=',', quotechar='|')
          trafficDataRaw.next()
          for row in trafficDataRaw:
               row[3] = int(row[3])
               total_traffic += row[3]
     return total_traffic
          # date = row[0].split(" ")
          # date_str = date[0]
          # time = date[1]
          # print date_str
          # print time
     

def month_traffic():
     month_traffic = {"jan": 0 }
     with open('ExpressLanesTrafficWithTolls-2014.csv', 'rb') as csvfile:
          trafficDataRaw = csv.reader(csvfile, delimiter=',', quotechar='|')
          trafficDataRaw.next()
          for row in trafficDataRaw:
               row[3] = int(row[3])
               total_traffic += row[3]
     

def main():
     print total_2014()

main()
     
     # #print trafficDataRaw.next()

     # # Using dictionaries
     # traffic_month = {"jan": 0, "feb": 0, "mar": 0, "apr":0, "may":0, "june":0, "july":0, "aug":0, "sept":0, "oct":0, "nov": 0, "dec": 0}
     # traffic_hours_am = {"am5": 0, "am6": 0, "am7": 0, "am8": 0, "am9": 0}
     # traffic_hours_pm = {"pm3": 0, "pm4": 0, "pm5": 0, "pm6": 0, "pm7": 0}
     
     # Monday = 0
     # # Using for loop and counters
     # for row in trafficDataRaw:
     #      row[3] = int(row[3])
     #      # date = row[0].split(" ")
     #      # date_str = date[0]
     #      # time = date[1]
     #      # print date_str
     #      # print time

     #      dateTime = row[0]
     #      date = dateTime.split()[0]
     #      #print date
     #      monthlist = date.split("/")
     #      monthlist[1] = monthlist[1] + ", "

     #      if monthlist[0] == '1':
     #           monthlist[0] = "January "
     #      if monthlist[0] == "2":
     #           monthlist[0] = "February "
     #      if monthlist[0] == '3':
     #           monthlist[0] = "March "
     #      if monthlist[0] == '4':
     #           monthlist[0] = "April "
     #      if monthlist[0] == '5':
     #           monthlist[0] = "May "
     #      if monthlist[0] == '6':
     #           monthlist[0] = "June "
     #      if monthlist[0] == '7':
     #           monthlist[0] = "July "
     #      if monthlist[0] == '8':
     #           monthlist[0] = "August "
     #      if monthlist[0] == '9':
     #           monthlist[0] =  "September "
     #      if monthlist[0] == '10':
     #           monthlist[0] = "October "
     #      if monthlist[0] == '11':
     #           monthlist[0] = "November "
     #      if monthlist[0] == '12':
     #           monthlist[0] = "December "
     #      date_string = "".join(monthlist)
     #      print date_string
     #      weekday = datetime.datetime.strptime(date_string, '%B %d, %Y').strftime('%A')
     #      print weekday
          
     #      mondays = {"January" : 0 }
     #      if weekday == "Monday":
     #           Monday += row[3]

     #      print "monday traffic: ", Monday
          
     #      print monthlist

     #      # Car count in the morning
     #      # if time[0] == '5':
     #      #      traffic_hours_am['am5'] +=row[3]
     #      # if time[0] == '6':
     #      #      traffic_hours_am['am6'] +=row[3]
     #      # if time[0] == '7':
     #      #      traffic_hours_am['am7'] +=row[3]
     #      # if time[0] == '8':
     #      #      traffic_hours_am['am8'] +=row[3]
     #      # if time[0] == '9':
     #      #      traffic_hours_am['am9'] +=row[3]
     
          
     #      # if row[4] != '':
     # 	# 	row[4] = int(row[4])
     # 	# if row[3] != '':
     # 	# 	row[3] = int(row[3])
     # 	# if row[2] != '' or row[2] != "HOV ONLY" or row[2] != " ":
     # 	# 	row[2] = float(row[2])

     #      if row[0][0:2] == "1/":
     #           traffic_month['jan'] +=row[3]         
     #      elif row[0][0:2] == "2/":
     #           traffic_month['feb'] +=row[3] 
     #      elif row[0][0:2] == "3/":
     #           traffic_month['mar'] +=row[3] 
     #      elif row[0][0:2] == "4/":
     #           traffic_month['apr'] +=row[3] 
     #      elif row[0][0:2] == "5/":
     #           traffic_month['may'] +=row[3] 
     #      elif row[0][0:2] == "6/":
     #           traffic_month['june'] +=row[3] 
     #      elif row[0][0:2] == "7/":
     #           traffic_month['july'] +=row[3] 
     #      elif row[0][0:2] == "8/":
     #           traffic_month['aug'] +=row[3] 
     #      elif row[0][0:2] == "9/":
     #           traffic_month['sept'] +=row[3] 
          
     #      if row[0][0:3] == "10/":
     #           traffic_month['oct'] +=row[3] 
     #      elif row[0][0:3] == "11/":
     #           traffic_month['nov'] +=row[3] 
     #      elif row[0][0:3] == "12/":
     #           traffic_month['dec'] +=row[3] 

     # # print "jan", jan
     # # print "dec:", dec
     #      #print row
     # # Number of cars in a month
     # print "January", traffic_month['jan']      
     # print "February", traffic_month['feb']
     # print "March", traffic_month['mar']
     # print "April", traffic_month['apr']
     # print "May", traffic_month['may']
     # print "June", traffic_month['june']
     # print "July", traffic_month['july']
     # print "August", traffic_month['aug']
     # print "September", traffic_month['sept']
     # print "October", traffic_month['oct']
     # print "November", traffic_month['nov']
     # print "December", traffic_month['dec']

     # #Number cars hourly for the morning timeframe
     # # print "5 AM hourly car count is", traffic_hours_am['am5']
     # # print "6 AM hourly car count is", traffic_hours_am['am6']
     # # print "7 AM hourly car count is", traffic_hours_am['am7']
     # # print "8 AM hourly car count is ", traffic_hours_am['am8']
     # # print "9 AM hourly car count is", traffic_hours_am['am9']
     


