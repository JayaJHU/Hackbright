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
     # print trafficDataRaw.next()

     # Using dictionaries
     traffic_month = {"jan": 0, "feb": 0, "mar": 0, "apr":0, "may":0, "june":0, "july":0, "aug":0, "sept":0, "oct":0, "nov": 0, "dec": 0}
     traffic_hours_am = {"am5": 0, "am6": 0, "am7": 0, "am8": 0, "am9": 0}
     traffic_hours_pm = {"pm3": 0, "pm4": 0, "pm5": 0, "pm6": 0, "pm7": 0}
     traffic_week = {"week 0":0,"week 1":0,"week 2":0,"week 3":0,"week 4":0,"week 5":0,"week 6":0,"week 7":0,"week 8":0,"week 9":0,"week 10":0,"week 11":0, "week 12":0,"week 13":0,"week 14":0,"week 15":0,"week 16":0,"week 17":0,"week 18":0,"week 19":0,"week 20":0,"week 21":0, "week 22":0,"week 23":0,"week 24":0,"week 25":0,"week 26":0,"week 27":0,"week 28":0,"week 29":0,"week 30":0,"week 31":0,"week 32":0,"week 33":0,"week 34":0,"week 35":0,"week 36":0,"week 37":0, "week 38":0,"week 39":0,"week 40":0,"week 41":0,"week 42":0,"week 43":0,"week 44":0,"week 45":0,"week 46":0,"week 47":0,"week 48":0,"week 49":0,"week 50":0,"week 51":0,"week 52":0}

     ##### Using for loop and counters
     ### Monthly, Weekly, Daily,Hourly and Direcction car count code
     Monday = 0
     Tuesday = 0
     Wednesday = 0
     Thursday = 0
     Friday = 0
     West = 0
     East = 0
     # print trafficDataRaw.next()[1][-1]
     for row in trafficDataRaw:
          row[3] = int(row[3])
          iDate = row[0].split(" ") ### splitting datetime into half
          date_str = iDate[0]  ### date 
          time = iDate[1]  ### time 
          # print date_str
          # print time

          #Calculate car count on 237 Westbound and 237 Eastbound
          # print row[1][-1]
          if row[1][-1] == 'E':
               East+=row[3]
          else:
               West+=row[3]
          

          dateTime = row[0]  ### (date and time together)
          date = dateTime.split()[0] ### (splitting date and time. Showing date only, 1/1/2014 format)
          # print date
          monthlist = date.split("/")  ### (splitting date into list, i.e.[{'1','1','2014'])
          # print monthlist
          monthlist[1] = monthlist[1] + ", "    ### (concatenate i.e. 1,)

          if monthlist[0] == '1':
               monthlist[0] = "January "
          if monthlist[0] == "2":
               monthlist[0] = "February "
          if monthlist[0] == '3':
               monthlist[0] = "March "
          if monthlist[0] == '4':
               monthlist[0] = "April "
          if monthlist[0] == '5':
               monthlist[0] = "May "
          if monthlist[0] == '6':
               monthlist[0] = "June "
          if monthlist[0] == '7':
               monthlist[0] = "July "
          if monthlist[0] == '8':
               monthlist[0] = "August "
          if monthlist[0] == '9':
               monthlist[0] =  "September "
          if monthlist[0] == '10':
               monthlist[0] = "October "
          if monthlist[0] == '11':
               monthlist[0] = "November "
          if monthlist[0] == '12':
               monthlist[0] = "December "
          date_string = "".join(monthlist)
          # print date_string  ### (prints January 1, 2014 format)
          weekday = datetime.datetime.strptime(date_string, '%B %d, %Y').strftime('%A')  
          # print weekday   ### (prints day only, i.e Monday)
          week = datetime.datetime.strptime(date_string, '%B %d, %Y').strftime('%W')  
          # print week    ### (prints week only, i.e. week 0, week 1, etc.)

     # Counting cars week by week for a total of 52 weeks.  January 1, 2014 fall on a Wednesday.  Hence, all days in a new year preceding the first Monday are considered to be in week 0.
          if week == '00':
               traffic_week['week 0'] +=row[3]
          if week == '01':
               traffic_week['week 1'] +=row[3]
          if week == '02':
               traffic_week['week 2'] +=row[3]
          if week == '03':
               traffic_week['week 3'] +=row[3]
          if week == '04':
               traffic_week['week 4'] +=row[3]
          if week == '05':
               traffic_week['week 5'] +=row[3]
          if week == '06':
               traffic_week['week 6'] +=row[3]
          if week == '07':
               traffic_week['week 7'] +=row[3]
          if week == '08':
               traffic_week['week 8'] +=row[3]
          if week == '09':
               traffic_week['week 9'] +=row[3]
          if week == '10':
               traffic_week['week 10'] +=row[3]
          if week == '11':
               traffic_week['week 11'] +=row[3]
          if week == '12':
               traffic_week['week 12'] +=row[3]
          if week == '13':
               traffic_week['week 13'] +=row[3]
          if week == '14':
               traffic_week['week 14'] +=row[3]
          if week == '15':
               traffic_week['week 15'] +=row[3]
          if week == '16':
               traffic_week['week 16'] +=row[3]
          if week == '17':
               traffic_week['week 17'] +=row[3]
          if week == '18':
               traffic_week['week 18'] +=row[3]
          if week == '19':
               traffic_week['week 19'] +=row[3]
          if week == '20':
               traffic_week['week 20'] +=row[3]
          if week == '21':
               traffic_week['week 21'] +=row[3]
          if week == '22':
               traffic_week['week 22'] +=row[3]
          if week == '23':
               traffic_week['week 23'] +=row[3]
          if week == '24':
               traffic_week['week 24'] +=row[3]
          if week == '25':
               traffic_week['week 25'] +=row[3]
          if week == '26':
               traffic_week['week 26'] +=row[3]
          if week == '27':
               traffic_week['week 27'] +=row[3]
          if week == '28':
               traffic_week['week 28'] +=row[3]
          if week == '29':
               traffic_week['week 29'] +=row[3]
          if week == '30':
               traffic_week['week 30'] +=row[3]
          if week == '31':
               traffic_week['week 31'] +=row[3]
          if week == '32':
               traffic_week['week 32'] +=row[3]
          if week == '33':
               traffic_week['week 33'] +=row[3]
          if week == '34':
               traffic_week['week 34'] +=row[3]
          if week == '35':
               traffic_week['week 35'] +=row[3]
          if week == '36':
               traffic_week['week 36'] +=row[3]
          if week == '37':
               traffic_week['week 37'] +=row[3]
          if week == '38':
               traffic_week['week 38'] +=row[3]
          if week == '39':
               traffic_week['week 39'] +=row[3]
          if week == '40':
               traffic_week['week 40'] +=row[3]
          if week == '41':
               traffic_week['week 41'] +=row[3]
          if week == '42':
               traffic_week['week 42'] +=row[3]
          if week == '43':
               traffic_week['week 43'] +=row[3]
          if week == '44':
               traffic_week['week 44'] +=row[3]
          if week == '45':
               traffic_week['week 45'] +=row[3]
          if week == '46':
               traffic_week['week 46'] +=row[3]
          if week == '47':
               traffic_week['week 47'] +=row[3]
          if week == '48':
               traffic_week['week 48'] +=row[3]
          if week == '49':
               traffic_week['week 49'] +=row[3]
          if week == '50':
               traffic_week['week 50'] +=row[3]
          if week == '51':
               traffic_week['week 51'] +=row[3]
          if week == '52':
               traffic_week['week 52'] +=row[3]
          


          # Counting cars on Monday, Tuesday, Wednesday, Thursday, Friday 
          mondays = {"January" : 0, "February":0, "March":0, "April":0, "May":0, "June":0, "July":0, "August":0, "September":0, "October":0, "November":0, "December":0}
          tuesdays = {"January":0, "February":0, "March":0, "April":0, "May":0, "June":0, "July":0, "August":0, "September":0, "October":0, "November":0, "December":0}
          wednesdays = {"January":0, "February":0, "March":0, "April":0, "May":0, "June":0, "July":0, "August":0, "September":0, "October":0, "November":0, "December":0}
          thurdays = {"January":0, "February":0, "March":0, "April":0, "May":0, "June":0, "July":0, "August":0, "September":0, "October":0, "November":0, "December":0}
          fridays = {"January":0, "February":0, "March":0, "April":0, "May":0, "June":0, "July":0, "August":0, "September":0, "October":0, "November":0, "December":0}

          if weekday == "Monday":
               Monday += row[3]
          if weekday == "Tuesday":
               Tuesday += row[3]
          if weekday == "Wednesday":
               Wednesday += row[3]
          if weekday == "Thursday":
               Thursday += row[3]
          if weekday == "Friday":
               Friday += row[3]
          
          
          # Hourly car count in the morning (AM) and evening(PM)
          hour = time.split(':')[0]
          if hour == '5':
               traffic_hours_am['am5'] +=row[3]
          elif hour == '6':
               traffic_hours_am['am6'] +=row[3]
          elif hour == '7':
               traffic_hours_am['am7'] +=row[3]
          elif hour == '8':
               traffic_hours_am['am8'] +=row[3]
          elif hour == '9':
               traffic_hours_am['am9'] +=row[3]
          elif hour == '15':
               traffic_hours_pm['pm3'] +=row[3]
          elif hour == '16':
               traffic_hours_pm['pm4'] +=row[3]
          elif hour == '17':
               traffic_hours_pm['pm5'] +=row[3]
          elif hour == '18':
               traffic_hours_pm['pm6'] +=row[3]


          month = date_str.split("/")[0]
          # Number of cars in a month
          if month == "1":
               traffic_month['jan'] +=row[3]         
          elif month == "2":
               traffic_month['feb'] +=row[3] 
          elif month == "3":
               traffic_month['mar'] +=row[3] 
          elif month == "4":
               traffic_month['apr'] +=row[3] 
          elif month == "5":
               traffic_month['may'] +=row[3] 
          elif month == "6":
               traffic_month['june'] +=row[3] 
          elif month == "7":
               traffic_month['july'] +=row[3] 
          elif month == "8":
               traffic_month['aug'] +=row[3] 
          elif month == "9":
               traffic_month['sept'] +=row[3] 
          elif month == "10":
               traffic_month['oct'] +=row[3] 
          elif month == "11":
               traffic_month['nov'] +=row[3] 
          elif month == "12":
               traffic_month['dec'] +=row[3] 

     # Printing total number of cars on each day on 237 Westbound and Eastbound     
     print "Monday car count:", Monday
     print "Tuesday car count:", Tuesday
     print "Wednesday car count:", Wednesday
     print "Thursday car count:", Thursday
     print "Friday car count:", Friday

     # Printing total number of cars hourly for morning and evening timeframe on 237 Westbound and Eastbound
     print "5 AM hourly car count:", traffic_hours_am['am5']
     print "6 AM hourly car count:", traffic_hours_am['am6']
     print "7 AM hourly car count:", traffic_hours_am['am7']
     print "8 AM hourly car count:", traffic_hours_am['am8']
     print "9 AM hourly car count:", traffic_hours_am['am9']
     print "3 PM hourly car count:", traffic_hours_pm['pm3']
     print "4 PM hourly car count:", traffic_hours_pm['pm4']
     print "5 PM hourly car count:", traffic_hours_pm['pm5']
     print "6 PM hourly car count:", traffic_hours_pm['pm6']


     # Printing total number of cars each month on 237 Westbound and Eastbound
     print "January car count:", traffic_month['jan']   
     print "February car count:", traffic_month['feb']
     print "March car count:", traffic_month['mar']
     print "April car count:", traffic_month['apr']
     print "May car count:", traffic_month['may']
     print "June car count:", traffic_month['june']
     print "July car count:", traffic_month['july']
     print "August car count:", traffic_month['aug']
     print "September car count:", traffic_month['sept']
     print "October car count:", traffic_month['oct']
     print "November car count:", traffic_month['nov']
     print "December car count:", traffic_month['dec']


     # Printing total number of cars on 237 Westbound and Eastbound 
     print "Number of cars on 237 Westbound:", West
     print "Number of cars on 237 Eastbound:", East


     # Printing total number of cars weekly on 237 Westbound and Eastbound
     print "Car count for week 0:", traffic_week['week 0']
     print "Car count for week 1:", traffic_week['week 1']
     print "Car count for week 2:", traffic_week['week 2']
     print "Car count for week 3:", traffic_week['week 4']
     print "Car count for week 5:", traffic_week['week 5']
     print "Car count for week 6:", traffic_week['week 6']
     print "Car count for week 7:", traffic_week['week 7']
     print "Car count for week 8:", traffic_week['week 8']
     print "Car count for week 9:", traffic_week['week 9']
     print "Car count for week 10:", traffic_week['week 10']
     print "Car count for week 11:", traffic_week['week 11']
     print "Car count for week 12:", traffic_week['week 12']
     print "Car count for week 13:", traffic_week['week 13']
     print "Car count for week 14:", traffic_week['week 14']
     print "Car count for week 15:", traffic_week['week 15']
     print "Car count for week 16:", traffic_week['week 16']
     print "Car count for week 17:", traffic_week['week 17']
     print "Car count for week 18:", traffic_week['week 18']
     print "Car count for week 19:", traffic_week['week 19']
     print "Car count for week 20:", traffic_week['week 20']
     print "Car count for week 21:", traffic_week['week 21']
     print "Car count for week 22:", traffic_week['week 22']
     print "Car count for week 23:", traffic_week['week 23']
     print "Car count for week 24:", traffic_week['week 24']
     print "Car count for week 25:", traffic_week['week 25']
     print "Car count for week 26:", traffic_week['week 26']
     print "Car count for week 27:", traffic_week['week 27']
     print "Car count for week 28:", traffic_week['week 28']
     print "Car count for week 29:", traffic_week['week 29']
     print "Car count for week 30:", traffic_week['week 30']
     print "Car count for week 31:", traffic_week['week 31']
     print "Car count for week 32:", traffic_week['week 32']
     print "Car count for week 33:", traffic_week['week 33']
     print "Car count for week 34:", traffic_week['week 34']
     print "Car count for week 35:", traffic_week['week 35']
     print "Car count for week 36:", traffic_week['week 36']
     print "Car count for week 37:", traffic_week['week 37']
     print "Car count for week 38:", traffic_week['week 38']
     print "Car count for week 39:", traffic_week['week 39']
     print "Car count for week 40:", traffic_week['week 40']
     print "Car count for week 41:", traffic_week['week 41']
     print "Car count for week 42:", traffic_week['week 42']
     print "Car count for week 43:", traffic_week['week 43']
     print "Car count for week 44:", traffic_week['week 44']
     print "Car count for week 45:", traffic_week['week 45']
     print "Car count for week 46:", traffic_week['week 46']
     print "Car count for week 47:", traffic_week['week 47']
     print "Car count for week 48:", traffic_week['week 48']
     print "Car count for week 49:", traffic_week['week 49']
     print "Car count for week 50:", traffic_week['week 50']
     print "Car count for week 51:", traffic_week['week 51']
     print "Car count for week 52:", traffic_week['week 52']
