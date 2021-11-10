def kmerCompositionOfAString(k, text):
	kmerList = []
	for i in range(len(text)-k+1):
#		if len(text[i:i+k-1]) == k:
			kmerList.append(text[i:i+k])
	kmerList.sort()
	kmerList = list(filter(None,kmerList))
	return kmerList

input = open("input3a.txt","r")
output = open("output3a.txt","w")
arguments = []
for line in input:	
	arguments.append(line.strip())
input.close()
#print(arguments)
kmerSet = kmerCompositionOfAString(int(arguments[0]),str(arguments[1]))
for i in kmerSet:
	output.write(i + "\n")
output.close()

#print(kmerCompositionOfAString(5,"CAATCCAAC"))
