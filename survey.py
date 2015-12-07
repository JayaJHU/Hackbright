print "Welcome to the survey!"
name1 = raw_input("What is your name?")
color1 = raw_input("What is your favorite color?")
hobby1 = raw_input("What is your favorite hobby?")
movie1 = raw_input("What is your favorite movie?")
#name2 = raw_input("What is your name?")
#color2 = raw_input("What is your favorite color?")
#hobby2 = raw_input("What is your favorite hobby?")
#movie2 = raw_input("What is your favorite movie?")
#print name1,"'s favorite color is", color1
#print name1,"'s favorite hobby is", hobby1
#print name1,"'s favorite movie is", movie1
#print name2,"'s favorite color is", color2
#print name2,"'s favorite hobby is", hobby2
#print name2,"'s favorite movie is", movie2
#print name1,"'s favorite color is:%s, favorite hobby is:%s  and favorite movie is:%s" % (color1, hobby1, movie1)
#print name1,"'s favorite color is:%s" %(color1)
#print name1,"'s favorite hobby is:%s" %(hobby1)
#print name1,"'s favorite movie is:%s" %(movie1)

def print_survey_results(name1,color1,hobby1,movie1):
	print "%s's favorite color is %s" %(name1, color1)
	print "%s's favorite color is %s" %(name1, hobby1)
	print "%s's favorite color is %s" %(name1, movie1)
print_survey_results(name1,color1,hobby1,movie1)