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
	#print(letterToFind)
	#print(indexToFind)
	for index, tuple  in enumerate(first):
		if tuple[0] == letterToFind and tuple[1] == indexToFind:
			indexIs = index
			break
	return indexIs

def main():
        input = open("input61.txt", "r")
        output = open("output61.txt", "w")

        lastColStr = next(input).strip()
	idx = next(input).strip()
        lastCol = [i for i in lastColStr]
        firstCol = lastCol[:]
        firstCol.sort()

	organizedLastCol = enumerateRepeats(lastCol)
        organizedFirstCol = enumerateRepeats(firstCol)

	#print(firstCol)
	#print(lastCol[339])
	stringIdx = lastToFirst(organizedFirstCol, organizedLastCol, idx)
        output.write(str(stringIdx)) 

        output.close()
        input.close()

if __name__ == "__main__":
        main()
