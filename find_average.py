# Create a function findAverage that has three parameters, num1, num2 and num3
# findAverage should find average of 3 numbers
# findAverage(3,4,4) and findAverage(1,2,3)
# If user passes a string then return message "Sorry the inputs are invalid"
# instead of calculating the average

# Call findAverage("6",8,7) and findAverage(2,9,"hi")


def findAverage(num1,num2,num3):
    total = num1 + num2 + num3
    average = total / 3.0
    return average
    


num1 = input("Enter your first number:")
num2 = input("Enter your second number:")
num3 = input("Enter your third number:")


if (type(num1)==str or type(num2)==str or type(num3)==str):
    print "Sorry the inputs are invalid"
else:
    print findAverage(num1,num2,num3)

#value = float(findAverage(n1,n2,n3))
#print "The average is", "%.2f" %value


#print "The average is:", "%.2f" %findAverage(n1,n2,n3)                                            
#print findAverage(1,2,3)
#print findAverage("6",8,7)
#print findAverage(2,9,"hi")
    
