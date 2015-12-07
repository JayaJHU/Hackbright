def add(num1,num2):
	return num1 + num2
# print add (4,5)

def subtract(num1,num2):
 	return num1 - num2
# print subtract(9,5)

def multiply(num1,num2):
 	return num1 * num2
# print multiply(6,4)


def divide(num1,num2):
 	return num1 / num2
# print multiply(35,5)


def modulo(num1,num2):
 	return num1 % num2
# print modulo(7,3)

def power(num1,num2):
	return num1 ** num2
# # print power(3,3)


# def square(num):
#  	return num ** 2
# print square(2)

def square(num):
 	return power(num,2)
# print square(2)


# import math

# def square(num):
#  	return math.pow (num,2)
# print square(5)

#print add(4,5) + subtract(9,6)
#print divide(12,2) - 60
#print add(1,2) + 3
#print square (add(1,2))
#print modulo(3,4) / power(9,9)
#print multiply(7,add(3,8))
#print subtract(add(1,2),3) * add(4,5)

age = add(30,4)
height = subtract(78,2)
weight = multiply(6,24)
iq = divide(100,2)
print "Age: %d, Height:%d, Weight:%d, IQ:%d" %(age, height,weight,iq)
