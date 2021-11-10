def overlapAlignment(str1, str2):
	n = len(str1)
	m = len(str2)
	inf = float("-inf")
	dpMat = [[inf for i in range(m+1)] for j in range(n+1)]
	backMat = [[inf for i in range(m+1)] for j in range(n+1)]
	dpMat[0][0] = 0
	backMat[0][0] = 0
	indel = 2
	
	for i in range(1,n+1):
		dpMat[i][0] = 0
		backMat[i][0] = 'u'
	for i in range(1, m+1):
		dpMat[0][i] = int(dpMat[0][i-1]) - indel
		backMat[0][i] = 'l'
	
	for i in range(1,n+1):
                for j in range(1,m+1):
                        leftVal = int(dpMat[i][j-1]) - indel
                        upVal = int(dpMat[i-1][j]) - indel
                        if str1[i-1] == str2[j-1]:
                                dVal = int(dpMat[i-1][j-1]) + 1
                        else:
                                dVal = int(dpMat[i-1][j-1]) - indel

                        dpMat[i][j] = max(leftVal, upVal, dVal)

                        if str1[i-1] == str2[j-1] and dpMat[i][j] == dpMat[i-1][j-1] + 1:
                                backMat[i][j] = 'd'
                        else:
                                if dpMat[i][j-1] == dpMat[i-1][j] and dpMat[i-1][j-1] == dpMat[i-1][j] + indel:
                                        backMat[i][j] = 'dm'
                                elif dpMat[i][j] == leftVal:
                                        backMat[i][j] = 'l'
                                elif dpMat[i][j] == upVal:
                                        backMat[i][j] = 'u'
				elif dpMat[i][j] == dVal:
					backMat[i][j] = 'd'
	#print(dpMat[n-2])
	#print(dpMat[n-1])
	#print(backMat[n-2])
	#print(backMat[n-1])

	#print(dpMat)
	#print(backMat)

	maxLastRow = inf
	maxLastM = inf
	maxLastN = n
	for i in range(m+1):
                if maxLastRow < dpMat[n][i]:
                        maxLastRow = dpMat[n][i]
                        maxLastM = i
			
        #print(maxLastRow)
	#print(maxLastN)
	#print(maxLastM)

	strUp, strLeft = backtrackOverlapAlignment(str1, str2, maxLastRow, maxLastN, maxLastM, dpMat, backMat)

	return maxLastRow, strUp, strLeft

def backtrackOverlapAlignment(str1, str2, maxLastRow, i, j, dpMat, backMat):
	backtrackArrLeft = []
        backtrackArrUp = []

        while j != 0:
		#print(i)
		#print(j)
                if backMat[i][j] == 'd' or backMat[i][j] == 'dm':
                        maxVal = dpMat[i-1][j-1]
                        backtrackArrLeft.insert(0, str1[i-1])
                        backtrackArrUp.insert(0, str2[j-1])
                        i = i-1
                        j = j-1
                        #print(maxVal)
                elif backMat[i][j] == 'l':
                        maxVal = dpMat[i][j-1]
                        backtrackArrLeft.insert(0, str1[i-1])
                        backtrackArrUp.insert(0, "-")
                        j = j-1
                        #print(maxVal)
                elif backMat[i][j] == 'u':
                        maxVal = dpMat[i-1][j]
                        backtrackArrLeft.insert(0, "-")
                        backtrackArrUp.insert(0, str2[j-1])
                        i = i-1
                        #print(maxVal)
        strLeft = ''.join(i for i in backtrackArrLeft)
        strUp = ''.join(i for i in backtrackArrUp)

        #print(strLeft)
	return strUp, strLeft

def main():
	input = open("input36.txt", "r")
	output = open("output36.txt", "w")

	str1 = str.strip(next(input))
	str2 = str.strip(next(input))

	#print(str1)
	#print(str2)

	maxVal, strUp, strLeft = overlapAlignment(str1, str2)

	output.write(str(maxVal))
	output.write("\n")
	output.write(strUp)
	output.write("\n")
	output.write(strLeft)
	output.write("\n")
	
	output.close()
	input.close()

if __name__ == "__main__":
	main()


