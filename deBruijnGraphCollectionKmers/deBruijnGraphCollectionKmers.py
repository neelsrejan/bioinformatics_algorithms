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

def deBruijnGraphCollectionKmers(kmers):
	deBruijnSet = []
	prefixSet = []
	kmer = kmers[0]
	prefixOfKmer = prefix(kmer)
	suffixOfKmer = suffix(kmer)
	pair = [prefixOfKmer, [suffixOfKmer]]
	prefixSet.append(prefixOfKmer)
	deBruijnSet.append(pair)
	for i in range(1,len(kmers)):
		kmer = kmers[i]
		prefixOfKmer = prefix(kmer)
		suffixOfKmer = suffix(kmer)
		pair = [prefixOfKmer, [suffixOfKmer]]
		if prefixOfKmer not in prefixSet:
			prefixSet.append(prefixOfKmer)
			deBruijnSet.append(pair)
		else:
			j = prefixSet.index(prefixOfKmer)
			deBruijnSet[j][1].append(suffixOfKmer)
	deBruijnSet.sort()
	return deBruijnSet



input = open("input3e.txt","r")
output = open("output3e.txt","w")
kmerList = []
for line in input:
	kmerList.append(line.strip())

deBruijnGraphSet = deBruijnGraphCollectionKmers(kmerList)
fullStr = ""
for i in deBruijnGraphSet:
	suffixStr = i[1][0]
	for j in range(1,len(i[1])):	
		suffixStr = suffixStr + "," + i[1][j]
	fullStr = i[0] + " -> " + suffixStr + "\n"
	output.write(fullStr)
input.close()
output.close()



