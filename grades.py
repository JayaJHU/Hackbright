# Write a python program that associates a percentage grade from
# the class_grades.txt with a letter grade
# You program should printout:
# The A(s) are [97]
# The B(s) [87,86,88]
# The C(s) are[74]
# The D(s) are[]

with open ("class_grades.txt") as classGrades:
    #readGrades = classGrades.read()
   	readGrades = classGrades.readlines()

#print readGrades

#def letterGrade(score):
	
	#if score >= 90:
		#return "A"
	#elif score >= 80:
		#return "B" 
	#elif score >= 70:
		#return "C"
	#elif score >= 60:
		#return "D"
	#elif score >= 50:
		#return "E"
	#else:
		#return "F"


#for grades in classGrades:
	#print "The 'As' are", letterGrade

#print sorted(readGrades)
readGrades.sort()
print readGrades


A = readGrades[12:]
A.append(100)
print "The 'A(s)' are", A
B = readGrades[9:12]
print "The 'B(s)' are", B
C = readGrades[4:9]
print "The 'C(s)' are", C
D = readGrades[2:4]
print "The 'D(s)' are", D
E = readGrades[1]
print "The 'E' is", E

	


