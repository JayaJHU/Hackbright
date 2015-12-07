# Please write a code that counts the number osf entries for each species of flora
# Please write a code that finds the average petal length of each species.

import csv

with open('flora.csv', 'rb') as csvfile:
    flowerCount = csv.reader(csvfile)
    setosa = 0
    versicolor = 0
    virginica = 0
    for row in flowerCount:
        # if '' not in row:        	
        # 	print row[4]
        if "setosa" == row[4]:
        	setosa += 1
        if "versicolor" == row[4]:
        	versicolor += 1
        if "virginica" == row[4]:
        	virginica += 1
    print "setosa", setosa
    print "versicolor", versicolor
    print "virginica", virginica




# with open ("flora.csv") as petalFlowers:
#     #flowerCount = petalFlowers.read()
#    	#flowerCount = petalFlowers.readlines()

# print flowerCount

#for row in flowerCount:
#B	print row[4]

# Write code that counts the number of entries for each species of flora

#def count_entries(species):
	#entry_counts = {}
#	for entry in species:
#		if(entry not in entry_count):
#			entry_counts[entry]=1
#		else:
#			entry_counts[entry]+=1
#	return entry_counts

#print count_entries()

