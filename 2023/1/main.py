# Number mappings for part 2
number_mapping = {
	"one": "o1e",
	"two": "t2o",
	"three": "t3e",
	"four": "f4r",
	"five": "f5e",
	"six": "s6x",
	"seven": "s7n",
	"eight": "e8t",
	"nine": "n9e",
}

# The answer
answer = 0

# Read the file
input = open('input.txt', 'r')
lines = input.readlines()

# For each line in the file...
for line in lines:

	# replace any instance of written digits
	for key,value in number_mapping.items():
		line = line.replace(key, value)

	# strip all non-digit characters
	line = [x for x in line if x.isnumeric()]

	# add the first and last digit
	line = line[0] + line[-1]
	
	# add the result to the answer global variable
	answer += int(line)

print("{}".format(answer))