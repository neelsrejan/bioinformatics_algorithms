def stringByGenomePath(kmers):
	string = kmers[0]
	for i in range(1,len(kmers)):
		kmer = kmers[i]
		string = string + kmer[-1]
	return string

input = open("input3b.txt","r")
output = open("output3b.txt","w")
kmersSet = []
for line in input:
	kmersSet.append(line.strip())

finalString = stringByGenomePath(kmersSet)
output.write(finalString)
input.close()
output.close()

#print(stringByGenomePath(["ACCGA","CCGAA","CGAAG","GAAGC","AAGCT"]))
