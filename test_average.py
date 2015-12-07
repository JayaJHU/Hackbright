
def average(num1,num2,num3):
    """Returns the average of three numbers."""
    total = num1+num2+num3
    return total / 3.0

n1 = float(raw_input("Enter first number: "))
n2 = float(raw_input("Enter second number: "))
n3 = float(raw_input("Enter third number: "))

#value = str( average (n1,n2,n3) / 3)
value = float(average (n1,n2,n3))
#print "One third of the average is ", "%.2f" %value
print "The average is ", "%.2f" %value

