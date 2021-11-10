def reversal(subset):
	reversed = []
	#print(subset)
	for i in subset:
		negI = ""
		#print(i)
		if i.startswith("+"):
			#print(i.strip("+"))
			negI = "-" + str(i.strip("+"))
			#print(negI)
			reversed.insert(0,negI)
		elif i.startswith("-"):
			negI = "+" + str(i.strip("-"))
			#print(negI)
			reversed.insert(0,negI)
	return reversed		


def greedySortPermutation(permutation):
	approxRevDist = 0
	permutationList = []
	for i in range(1,len(permutation)+1):
		strToCheck = "+" + str(i)
		strValToCheck = str(i)
		#print(strToCheck)
		#print(permutation)
		#print("perm Val")
		#print(permutation[i-1])
		#print("order is")
		#print(strToCheck)
		#print("\n")
		if permutation[i-1] != strToCheck:
			#print("inside")
			for j in range(len(permutation)):
				if permutation[j][1:] == strValToCheck:
					indexToReverse = j
			#print("index to Rev")
			#print(indexToReverse)
			#indexToReverse = permutation.index(strToCheck)
			subset = permutation[i-1:indexToReverse+1]
			#print("subset")
			#print(subset)
			reversedSubset = reversal(subset)
			#print("reversedSub")
			#print(reversedSubset)
			del permutation[i-1:indexToReverse+1]
			#print("del permutation")
			#print(permutation)
			#print("\n")
			approxRevDist = approxRevDist + 1	
			for x in range(len(reversedSubset)-1,-1,-1):
				#print(reversedSubset[x])
				#print(i-1)
				#print("\n")
				permutation.insert(i-1, reversedSubset[x])
			
			#print("swap")
			#print(permutation)
			permutationList.append(permutation[:])
			#print(permutationList)
			#print("\n")
				
			#print(permutation[i-1])
			#print("-" + strToCheck)	
			if permutation[i-1] == "-" + strValToCheck:
				single = permutation[i-1]
				#print("single to switch")
				#print(single)
				#print(type(single))
				reversedVal = reversal([single])
				del permutation[i-1]
				approxRevDist = approxRevDist + 1
				permutation.insert(i-1, reversedVal[0])
				
				#print("flip")
				permutationList.append(permutation[:])
				#print(permutation)
				#print(permutationList)
				#print("\n")
	return permutationList

def main():
	input = open("input42.txt","r")
	output = open("output42.txt","w")

	line = next(input).strip()
	line = line.strip("()")
	permutation = line.split(" ")
	
	#print(permutation)
	#print("\n")
	permutationList = greedySortPermutation(permutation)
	#reversal(['-3', '+4', '+1'])
	#print(what)
	#print(type(permutation[1]))
	
	#for i in permutationList:
		#print(i)
		#print("\n")
	for i in permutationList:
		output.write("(")
		almostEnd = 0
		for j in range(len(i)-1):
			output.write(i[j])
			output.write(" ")
			almostEnd = j
		output.write(i[almostEnd+1])
		output.write(")")
		output.write("\n")
	
	output.close()
	input.close()

if __name__ == "__main__":
	main()
