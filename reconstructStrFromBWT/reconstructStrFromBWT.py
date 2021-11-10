def enumerateRepeats(list):
	organized = []
	countA = 0
	countT = 0
	countG = 0
	countC = 0
	countS = 0
	for letter in list:
		if letter == "A":
			organized.append((letter, countA))
			countA = countA + 1
		elif letter == "T":
			organized.append((letter, countT))
			countT = countT + 1
		elif letter == "G":
			organized.append((letter, countG))
			countG = countG + 1
		elif letter == "C":
			organized.append((letter, countC))
			countC = countC + 1
		elif letter == "$":
			organized.append((letter, countS))
			coungS = countS + 1
	return organized

def reconstructStrFromBWT(first, last):
	str = []
	nextLetter = "$"
	nextIdx = 0
	index = -1
	while len(first) != 0:
		for idx, element in enumerate(last):
			if element[0] == nextLetter and element[1] == nextIdx:
				nextLetter = first[idx][0]
				nextIdx = first[idx][1]
				str.append(first[idx][0])
				#print(idx)
				#print(last[idx])
				del first[idx]
				del last[idx]
				#print(str)
				#print("\n")
	return ''.join([i for i in str])

def main():
	input = open("i62.txt", "r")
	output = open("o62.txt", "w")

	lastColStr = next(input).strip()
	lastCol = [i for i in lastColStr]
	#print(lastCol)
	firstCol = lastCol[:]
	firstCol.sort()
	#print(firstCol)
	#print("\n")
	organizedLastCol = enumerateRepeats(lastCol)
	organizedFirstCol = enumerateRepeats(firstCol)
	#print(organizedLastCol)
	#print("\n")
	#print(organizedFirstCol)
	#print(organizedFirstCol[0][0])
	#print(organizedFirstCol[1][0])
	#print(organizedFirstCol[0][1])
	string = reconstructStrFromBWT(organizedFirstCol, organizedLastCol)
	output.write(string)

	output.close()
	input.close()


if __name__ == "__main__":
	main()
