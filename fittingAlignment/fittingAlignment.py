def fittingAlignment(str1, str2):
	n = len(str2)
        m = len(str1)
        inf = float("-inf")
        dpMat = [[inf for i in range(m+1)] for j in range(n+1)]
        backMat = [[inf for i in range(m+1)] for j in range(n+1)]
	dpMat[0][0] = 0
	backMat[0][0] = 0

	for i in range(1,m+1):
                dpMat[0][i] = 0
		backMat[0][i] = 'l'
        for i in range(1,n+1):
                dpMat[i][0] = dpMat[i-1][0] - 1
		backMat[i][0] = 'u'

	for i in range(1,n+1):
		for j in range(1,m+1):
			leftVal = int(dpMat[i][j-1]) - 1
			upVal = int(dpMat[i-1][j]) - 1
			if str1[j-1] == str2[i-1]:
				dVal = int(dpMat[i-1][j-1]) + 1
			else:
				dVal = int(dpMat[i-1][j-1]) - 1
			
			dpMat[i][j] = max(leftVal, upVal, dVal)
			
			if str1[j-1] == str2[i-1] and dpMat[i][j] == dpMat[i-1][j-1] + 1:
				backMat[i][j] = 'd'
			else:
				if dpMat[i][j-1] == dpMat[i-1][j] and dpMat[i-1][j-1] == dpMat[i-1][j] + 1:
					backMat[i][j] = 'dm'
				elif dpMat[i][j] == leftVal:
					backMat[i][j] = 'l'
				elif dpMat[i][j] == upVal:
					backMat[i][j] = 'u'
	

	#print(dpMat)	
	#print(backMat)

	maxLastRow = inf
	maxLastN = n
	maxLastM = inf
	for i in range(m+1):
		if maxLastRow < dpMat[n][i]:
			maxLastRow = dpMat[n][i]
			maxLastM = i
	#print(maxLastRow)

	strLeft, strUp = backtrackFittingAlignment(str1, str2, maxLastRow, n, maxLastM, dpMat, backMat)
	
	return maxLastRow, strLeft, strUp

def backtrackFittingAlignment(str1, str2, maxVal, i, j, dpMat, backMat):
	backtrackArrLeft = []
	backtrackArrUp = []
	
	while i != 0:
		if backMat[i][j] == 'd' or backMat[i][j] == 'dm':
                        maxVal = dpMat[i-1][j-1]
                        backtrackArrLeft.insert(0, str1[j-1])
                        backtrackArrUp.insert(0, str2[i-1])
                        i = i-1
                        j = j-1
			#print(maxVal)
                elif backMat[i][j] == 'l':
                        maxVal = dpMat[i][j-1]
                        backtrackArrLeft.insert(0, str1[j-1])
                        backtrackArrUp.insert(0, "-")
                        j = j-1
			#print(maxVal)
                elif backMat[i][j] == 'u':
                        maxVal = dpMat[i-1][j]
                        backtrackArrLeft.insert(0, "-")
                        backtrackArrUp.insert(0, str2[i-1])
                        i = i-1
			#print(maxVal)
        strLeft = ''.join(i for i in backtrackArrLeft) 
	strUp = ''.join(i for i in backtrackArrUp)
	
	return strLeft, strUp

def main():
	input = open("input35.txt", "r")
	output = open("output35.txt", "w")
	
	str1 = str.strip(next(input))
	str2 = str.strip(next(input))

	#print(str1)
	#print(str2)
	
	max, strLeft, strUp = fittingAlignment(str1, str2)

	output.write(str(max))
	output.write("\n")
	output.write(strLeft)
	output.write("\n")
	output.write(strUp)

	output.close()
	input.close()

if __name__ == "__main__":
	main()


