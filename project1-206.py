import os
import filecmp
from dateutil.relativedelta import *
from datetime import date


def getData(file):
# get a list of dictionary objects from the file
#Input: file name
#Ouput: return a list of dictionary objects where
#the keys are from the first row in the data. and the values are each of the other rows
	infile = open(file, 'r')
	lines = infile.readlines()
	dict_keys = lines[0].split(',')
	dict_list = []
	for line in lines[1:]:
		practice_dict = {}
		split_line = line.split(',')
		practice_dict[dict_keys[0]] = split_line[0]
		practice_dict[dict_keys[1]] = split_line[1]
		practice_dict[dict_keys[2]] = split_line[2]
		practice_dict[dict_keys[3]] = split_line[3]
		practice_dict[dict_keys[4][:-1]] = split_line[4][:-1]
		dict_list.append(practice_dict)
	return dict_list


def mySort(data,col):
# Sort based on key/column
#Input: list of dictionaries and col (key) to sort on
#Output: Return the first item in the sorted list as a string of just: firstName lastName
	sorted_list = sorted(data, key = lambda x: x[col])
	first_sorted = sorted_list[0]
	return first_sorted['First'] + " " + first_sorted['Last']

def classSizes(data):
# Create a histogram
# Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]
	class_dict = {}
	for d in data:
		if 'Class' in d.keys():
			if d['Class'] not in class_dict.keys():
				class_dict[d['Class']] = 1
			else:
				class_dict[d['Class']] += 1

	class_list = sorted([t for t in class_dict.items()], key=lambda x: x[1], reverse=True)
	return class_list


def findMonth(a):
# Find the most common birth month form this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data
	month_dict = {}
	for d in a:
		if 'DOB' in d.keys():
			dob = d['DOB'].split('/')
			if dob[0] not in month_dict.keys():
				month_dict[dob[0]] = 1
			else:
				month_dict[dob[0]] += 1
	month_list = sorted([t for t in month_dict.items()], key = lambda x: x[1], reverse = True)
	common_month = int(month_list[0][0])
	return common_month

def mySortPrint(a,col,fileName):
#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as fist,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
#Output: No return value, but the file is written
	sorted_list = sorted(a, key = lambda x: x[col])
	outfile = open(fileName, 'w')
	for d in sorted_list:
		outfile.write('{},{},{}\n'.format(d['First'], d['Last'], d['Email']))

def findAge(a):
# def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.
	year_list = []
	for d in a:
		if 'DOB' in d.keys():
			year_split = d['DOB'].split('/')
			year_list.append(int(year_split[2]))
	age_list = [2018-y for y in year_list]
	avg_age = sum(age_list) // len(age_list)
	return avg_age


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
