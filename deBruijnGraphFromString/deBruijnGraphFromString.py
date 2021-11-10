def prefix(kmer):
        if len(kmer) <= 1:
                return kmer
        else:
                return kmer[0:len(kmer)-1]

def suffix(kmer):
        if len(kmer) <= 1:
                return kmer
        else:
                return kmer[1:len(kmer)]


def deBruijnGraphFromString(k, text):
	deBruijnSet = []
	k = int(k)
	kmer = text[0:k]
	toSlide = len(text)-int(k)+1
	prefixSet = []
	prefixOfKmer = prefix(kmer)
	suffixOfKmer = suffix(kmer)
	pair = [prefixOfKmer,[suffixOfKmer]]
	prefixSet.append(prefixOfKmer)
	deBruijnSet.append(pair)
	for i in range(1,toSlide):
		i = int(i)
		kmer = text[i:i+k]
		prefixOfKmer = prefix(kmer)
		suffixOfKmer = suffix(kmer)
		pair = [prefixOfKmer,[suffixOfKmer]]
#		print(prefixOfKmer)
#		print(prefixSet)
		if prefixOfKmer not in prefixSet:
			prefixSet.append(prefixOfKmer)
			deBruijnSet.append(pair)
		else:
			j = prefixSet.index(prefixOfKmer)
			deBruijnSet[j][1].append(suffixOfKmer)
	deBruijnSet.sort()
#	print(deBruijnSet[0][0])
	return deBruijnSet

input = open("input3d.txt","r")
output = open("output3d.txt","w")
arguments = []
for line in input:
	arguments.append(line.strip())
#print(arguments[0] + "\n" + arguments[1])
deBruijnPairs = deBruijnGraphFromString(arguments[0],arguments[1])
fullStr = ""
for i in deBruijnPairs:	
	suffixStr = i[1][0]
	for j in range(1,len(i[1])):	
		suffixStr = suffixStr + "," + i[1][j] 
	fullStr = i[0] + " -> " + suffixStr + "\n"
	output.write(fullStr)
input.close()
output.close()


#print(deBruijnGraphFromString(4,"AAGATTCTCTAC"))
		
