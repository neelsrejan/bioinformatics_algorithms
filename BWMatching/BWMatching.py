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

def lastToFirst(first, last, idx):
        indexIs = -1
        letterToFind = last[int(idx)][0]
        indexToFind = last[int(idx)][1]
        for index, tuple  in enumerate(first):
                if tuple[0] == letterToFind and tuple[1] == indexToFind:
                        indexIs = index
                        break
        return indexIs

def BWMatching(first, last, pattern):
	patternSplit = [i for i in pattern]
	top = 0
	bottom = len(last)-1
	lastLetter = [i[0] for i in last]
	while top <= bottom:
		if len(patternSplit) != 0:
			symbol = patternSplit[-1]
			del patternSplit[-1]

			if symbol in lastLetter[top:bottom+1]:
				indexOfSymbol = [] 
				for i in range(top, top + (bottom-top)+1):
					if symbol == last[i][0]:
						indexOfSymbol.append(i)
				
				topIndex = indexOfSymbol[0]
				bottomIndex = indexOfSymbol[-1]
				top = lastToFirst(first, last, topIndex)
				bottom = lastToFirst(first, last, bottomIndex)
			else:
				return 0
		else:
			return bottom - top + 1 
		

def main():
	input = open("input62.txt", "r")
	output = open("output62.txt", "w")

	lastColStr = next(input).strip()
	patternInLine = next(input).strip()
	patternInArr = patternInLine.split(" ")
	lastCol = [i for i in lastColStr]
	
	firstCol = lastCol[:]
	firstCol.sort()

	organizedLastCol = enumerateRepeats(lastCol)
	organizedFirstCol = enumerateRepeats(firstCol)

	numMatches = []
	for pattern in patternInArr:
		numMatches.append(BWMatching(organizedFirstCol, organizedLastCol, pattern))
	
	count = 0
	for i in range(len(numMatches)-1):
		output.write(str(numMatches[i]))
		output.write(" ")
		count = count + 1
	output.write(str(numMatches[count]))

	output.close()
	input.close()


if __name__ == "__main__":
	main()
