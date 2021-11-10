def editDistance(str1, str2):
	n = len(str2)
	m = len(str1)
	inf = float("inf")
	dpMat = [[inf for i in range(m+1)] for j in range(n+1)]
	dpMat[0][0] = 0
	for i in range(1,m+1):
		dpMat[0][i] = dpMat[0][i-1] + 1
	for i in range(1,n+1):
		dpMat[i][0] = dpMat[i-1][0] + 1
	for i in range(1,n+1):
		for j in range(1,m+1):
			if str1[j-1] == str2[i-1]:
				dpMat[i][j] = dpMat[i-1][j-1]
			else:
				dpMat[i][j] = min(dpMat[i-1][j],dpMat[i][j-1],dpMat[i-1][j-1]) + 1
	return dpMat[n][m]

def main():
	input = open("input34.txt", "r")
	output = open("output34.txt", "w")
	
	str1 = str.strip(next(input))
	str2 = str.strip(next(input))
	
	#print(str1)
	#print(str2)
	
	editVal = editDistance(str1, str2)

	output.write(str(editVal))
	
	output.close()
	input.close()

if __name__ == "__main__":
	main()
