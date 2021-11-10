def longestCommonSubsequence(str1,str2):
	str1Arr = [i.split() for i in str1]
	str2Arr = [i.split() for i in str2]
	#print(str1Arr)
	#print(str2Arr)
	inf = float("inf")
	n = len(str1Arr)+1
        m = len(str2Arr)+1
	#print(n)
	#print(m)
	dpMat = [[inf for i in range(n)] for j in range(m)]
	#print(dpMat)	
	for i in range(len(str1Arr)+1):
		dpMat[0][i] = 0
	for i in range(len(str2Arr)+1):
		dpMat[i][0] = 0
	#print(dpMat)

	#substring = []
	for i in range(1,m):
		for j in range(1,n):
			upVal = dpMat[i-1][j]
			leftVal = dpMat[i][j-1] 	
			dVal = dpMat[i-1][j-1]
			if str1Arr[j-1] == str2Arr[i-1]:
				dVal = dpMat[i-1][j-1]+1
			dpMat[i][j] = max(upVal,leftVal,dVal)
			
	#print(dpMat)
	#print(backtrack(str1Arr, str2Arr, dpMat, n, m))
	return backtrack(str1Arr, str2Arr, dpMat, n, m)
	#print(substringArr)	
	#substring = substringArr.strip("[").strip("]").strip("'")
	#print(substring)

def backtrack(str1, str2, dpMat, n, m):
	#print(str1)
	#print(str1[0])
	#print(str1[3][0])
	currVal = dpMat[m-1][n-1]
	#print(currVal)
	#print(m)
	#print(n)
	if n == 1 and m == 1:
		return ""
	if dpMat[m-2][n-1] == dpMat[m-1][n-2]:
		if currVal != dpMat[m-2][n-2]:
			#print(str(str1[n-2]))
			return backtrack(str1, str2, dpMat, n-1, m-1) + str(str1[n-2][0]) 
		else:
			return backtrack(str1, str2, dpMat, n-1, m-1)	
	else:
		if dpMat[m-2][n-1] == currVal:
			return backtrack(str1, str2, dpMat, n, m-1)
		else:
			return backtrack(str1, str2, dpMat, n-1, m)


'''
def recBacktrack(str1, str2, dpMat, n, m):
	currVal = dpMat[m-1][n-1]
	substring = ""
	while n != 1 and m != 1:
		print(n)
		print(m)
		if dpMat[m-2][n-1] == dpMat[m-1][n-2]:
			if currVal != dpMat[m-2][n-2]:	
				substring = substring + str(str1[n-2][0])
				print(substring)
				print(str1[n-2][0])
				n = n - 1
				m = m - 1
				currVal = dpMat[m-1][n-1]
				#substring = substring + str(str1[n-2][0])
			else:
				n = n - 1
				m = m - 1
		else:
			if dpMat[m-2][n-1] == currVal:
				m = m-1
			else:
				n = n-1
				'''

def main():
	input = open("input73.txt","r")
	output = open("output73.txt","w")

	str1 = str.strip(next(input))
	str2 = str.strip(next(input))

	#print(str1)
	#print(str2)

	subsequence = longestCommonSubsequence(str1,str2)

	output.write(subsequence)
	output.write("\n")

	input.close()
	output.close()

if __name__ == "__main__":
	main()
