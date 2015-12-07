# i = 0
# while(i < 20):
# 	i = i + 1
# 	print i


# i = 0
# while (i <20):
# 	i = i + 1
# 	if i == 13:
# 		print "hello"
# 	else:
# 		print i

# i = 0
# while (i<100):
# 	i = i + 10
# 	print i

# i = 11
# while (i>0):
# 	i = i - 1
# 	if i == 0:
# 		print "Blastoff"
# 	else:
# 		print i

# fruit_list =["apples", "oranges", "bananas"]
# index = 0
# while index < len(fruit_list):
# 	if index == 0:
# 		print fruit_list[index]
# 	elif index == 1:
# 		print fruit_list[index]
# 	else:
# 		print fruit_list[index]
# 	index = index + 1

# def sum_nums(num):
# 	sum = 0
# 	i=0
# 	while (i < num):
# 		sum = sum + i
# 		i = i + 1
# 	return sum

# print sum_nums(3)

# def sum_nums(num):
# 	sum = 0
# 	i=0
# 	while (i <= num):
# 		sum = sum + i
# 		i = i + 1
# 	return sum

# print sum_nums(3)

# WIP Jaya
# def sum_nums2(num):
# 	sum = 0
# 	i=0
# 	while (i < num):
# 		sum = sum + (i + (-1))
# 		i = i + 1
# 	return sum

# print sum_nums2(-3)

#Hackbright Solutions....
def sum_nums2(num):
	sum = 0
	i=0
	if(num<0):
		while(i>=num):
		    sum+=i
		    i-=1
	else:
	   	while(i<=num):
	     	 sum += i
	    	 i+=1
	return sum

print sum_nums2(-3)


def fizz_buzz():
	i=1
	while(i<=100):
	    if(i%3==0 and i%5==0):
	        print “FizzBuzz”
	    elif(i%3==0):
	        print “Fizz”
	    elif(i%5==0):
	        print “Buzz”
	    else:
	        print i
	    i+=1
