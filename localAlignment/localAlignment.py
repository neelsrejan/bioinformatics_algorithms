def localAlignment(str1, str2, pam):
        lenStr1 = len(str1)
        lenStr2 = len(str2)
        inf = float("inf")
        indel = 5
        dpMat = [[inf for i in range(lenStr1 + 1)] for i in range(lenStr2 + 1)]
        dpMat[0][0] = 0
	maxVal = 0
	max_dpMat = 0
	max_n = 0
	max_m = 0
	backMat = [[inf for i in range(lenStr1 + 1)] for i in range(lenStr2 + 1)]
	backMat[0][0] = 0
	
        for i in range(1, lenStr1+1):
		dpMat[0][i] = 0
		backMat[0][i] = 'l'
        for i in range(1, lenStr2+1):
		dpMat[i][0] = 0
		backMat[i][0] = 'u'
	
        for i in range(1,lenStr2+1):
                for j in range(1, lenStr1+1):
                        leftVal = int(dpMat[i][j-1]) - indel
			upVal = int(dpMat[i-1][j]) - indel
			leftChar = str1[j-1]
			upChar = str2[i-1]
			pamLeftIdx = pam[0].index(leftChar)
			pamUpIdx = pam[0].index(upChar)
			dVal = int(dpMat[i-1][j-1]) + pam[pamLeftIdx][pamUpIdx]
                        maxVal = max(leftVal, upVal, dVal)
			
			if maxVal == dVal and maxVal != leftVal and maxVal != upVal:
                                if maxVal < 0:
                                        maxVal = 0
                                        dpMat[i][j] = maxVal
                                        backMat[i][j] = 'd'
                                else:
                                        dpMat[i][j] = maxVal
                                        backMat[i][j] = 'd'
					if maxVal > max_dpMat:
						max_dpMat = maxVal
						max_n = i
						max_m = j
			elif maxVal == leftVal:
				if maxVal < 0:
					maxVal = 0
					dpMat[i][j] = maxVal
					backMat[i][j] = 'l'
				else:
					dpMat[i][j] = maxVal
                                        backMat[i][j] = 'l'
					if maxVal > max_dpMat:
						max_dpMat = maxVal
                                                max_n = i
                                                max_m = j
			elif maxVal == upVal:
				if maxVal < 0:
					maxVal = 0
					dpMat[i][j] = maxVal
					backMat[i][j] = 'u'
				else: 
					dpMat[i][j] = maxVal
					backMat[i][j] = 'u'
					if maxVal > max_dpMat:
						max_dpMat = maxVal
                                                max_n = i
                                                max_m = j
	
	backtrackArrLeft, backtrackArrUp = backtrackLocalAlignment(str1, str2, max_dpMat, max_n, max_m, dpMat, backMat)
        
	backtrackStrUp = ''.join([i for i in backtrackArrUp])
        backtrackStrLeft = ''.join([i for i in backtrackArrLeft])
        
	return max_dpMat, backtrackStrLeft, backtrackStrUp

def backtrackLocalAlignment(str1, str2, max_dpMat, max_n, max_m, dpMat, backMat):
	backtrackArrLeft = []
	backtrackArrUp = []
	maxVal = max_dpMat
	i = max_n
	j = max_m
	
	while maxVal != 0:
		if backMat[i][j] == 'd':
			maxVal = dpMat[i-1][j-1]
			backtrackArrLeft.insert(0, str1[j-1])
			backtrackArrUp.insert(0, str2[i-1])
			i = i-1
			j = j-1
		elif backMat[i][j] == 'l':
			maxVal = dpMat[i][j-1]
			backtrackArrLeft.insert(0, str1[j-1])
			backtrackArrUp.insert(0, "-")
			j = j-1
		elif backMat[i][j] == 'u':
			maxVal = dpMat[i-1][j]
			backtrackArrLeft.insert(0, "-")
			backtrackArrUp.insert(0, str2[i-1])
			i = i-1
	return backtrackArrLeft, backtrackArrUp
		
def main():

        input = open("input33.txt", "r")
        output = open("output33.txt", "w")

        str1 = str.strip(next(input))
        str2 = str.strip(next(input))
	
	pam = [[0, 'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y'], ['A', 2, -2, 0, 0, -3, 1, -1, -1, -1, -2, -1, 0, 1, 0, -2, 1, 1, 0, -6, -3], ['C', -2, 12, -5, -5, -4, -3, -3, -2, -5, -6, -5, -4, -3, -5, -4, 0, -2, -2, -8, 0], ['D', 0, -5, 4, 3, -6, 1, 1, -2, 0, -4, -3, 2, -1, 2, -1, 0, 0, -2, -7, -4], ['E', 0, -5, 3, 4, -5, 0, 1, -2, 0, -3, -2, 1, -1, 2, -1, 0, 0, -2, -7, -4], ['F', -3, -4, -6, -5, 9, -5, -2, 1, -5, 2, 0, -3, -5, -5, -4, -3, -3, -1, 0, 7], ['G', 1, -3, 1, 0, -5, 5, -2, -3, -2, -4, -3, 0, 0, -1, -3, 1, 0, -1, -7, -5], ['H', -1, -3, 1, 1, -2, -2, 6, -2, 0, -2, -2, 2, 0, 3, 2, -1, -1, -2, -3, 0], ['I', -1, -2, -2, -2, 1, -3, -2, 5, -2, 2, 2, -2, -2, -2, -2, -1, 0, 4, -5, -1], ['K', -1, -5, 0, 0, -5, -2, 0, -2, 5, -3, 0, 1, -1, 1, 3, 0, 0, -2, -3, -4], ['L', -2, -6, -4, -3, 2, -4, -2, 2, -3, 6, 4, -3, -3, -2, -3, -3, -2,  2, -2, -1], ['M', -1, -5, -3, -2, 0, -3, -2, 2, 0, 4, 6, -2, -2, -1, 0, -2, -1, 2, -4, -2], ['N', 0, -4, 2, 1, -3, 0, 2, -2, 1, -3, -2, 2, 0, 1, 0, 1, 0, -2, -4, -2], ['P', 1, -3, -1, -1, -5, 0, 0, -2, -1, -3, -2, 0, 6, 0, 0, 1, 0, -1, -6, -5], ['Q', 0, -5, 2, 2, -5, -1, 3, -2, 1, -2, -1, 1, 0, 4, 1, -1, -1, -2, -5, -4], ['R', -2, -4, -1, -1, -4, -3, 2, -2, 3, -3, 0, 0, 0, 1, 6, 0, -1, -2, 2, -4], ['S', 1, 0, 0, 0, -3, 1, -1, -1, 0, -3, -2, 1, 1, -1, 0, 2, 1, -1, -2, -3], ['T', 1, -2, 0, 0, -3, 0, -1, 0, 0, -2, -1, 0, 0, -1, -1, 1, 3, 0, -5, -3], ['V', 0, -2, -2, -2, -1, -1, -2, 4, -2, 2, 2, -2, -1, -2, -2, -1, 0, 4, -6, -2], ['W', -6, -8, -7, -7, 0, -7, -3, -5, -3, -2, -4, -4, -6, -5, 2, -2, -5, -6, 17, 0], ['Y', -3, 0, -4, -4, 7, -5, 0, -1, -4, -1, -2, -2, -5, -4, -4, -3, -3, -2, 0, 10]]

	max_dpMat, backtrackStrLeft, backtrackStrUp = localAlignment(str1, str2, pam)
	
        output.write(str(max_dpMat))
        output.write("\n")
        output.write(backtrackStrLeft)
        output.write("\n")
        output.write(backtrackStrUp)
	
if __name__ == "__main__":
	main()
