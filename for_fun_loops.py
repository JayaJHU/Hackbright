#for numbers in range(1,21):
	#print numbers


#for numbers in range(1,21):
	#if numbers == 13:
		#print "hello"
	#else:
		#print numbers

#for numbers in range(0,101,10):
	#print numbers

#for odds in range(0,11,3):
	#print odds

#for numbers in range(10,-1,-1):
	#print numbers

#for numbers in range(10,-1,-1):
	#if numbers == 0:
		#print "Blastoff"
	#else:
		#print numbers

#fruits = ["apples","oranges","bananas"]
#for items in fruits:
	#print items
	
#for index in range(len(fruits)):
#	print fruits[index]

#No.7
#def sum_nums(num):
#	sum = 0
	#for number in range(num):
		#sum = sum + number
	#return sum
#print sum_nums

# No.7 part a
#def sum_nums(num):
#	sum = 0
#	for number in range(num):
#		sum = sum + (number + 1)
#	return sum

#print sum_nums(3)

#No.7 part b
#def sum_nums2(num):
#	sum = 0
#	for number in range(num):
#		sum = sum + (number + (- 1))
#	return sum

#print sum_nums2(-3)

#7b Hackbright solution

#	    sum = 0
#	    if(num<0):
#	        for i in range(0, num-1, -1):
#	            sum += i
#	    else:
#	        for i in range(num+1):
#	            sum += i
#	    return sum

#print sum_nums2(-3)


def fizz_buzz():
	for i in range (1,101):
		if (i % 3 == 0):
			print "fizz"
		elif (i % 5 == 0):
			print "buzz"
		elif (i % 3 == 0 and i % 5 == 0):
			print "fizzbuzz"
		else:
			print i
	

print fizz_buzz()
