# Read the file
input = open('input.txt', 'r')
lines = input.readlines()

for line in lines:
	print("{}".format(line.strip()))
