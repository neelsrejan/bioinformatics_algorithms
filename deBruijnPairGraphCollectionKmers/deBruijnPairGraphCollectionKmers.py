'''
def prefix(kmer,d):
        if len(kmer) <= 1:
                return kmer
        else:
                return kmer[0:len(kmer)-d]

def suffix(kmer,d):
        if len(kmer) <= 1:
                return kmer
        else:
                return kmer[d:len(kmer)]

def deBruijnPairGraphCollectionKmers(kmersT, kmersB, d):
        deBruijnSet = []
        prefixSetT = []
	prefixSetB = []
	

        kmerT = kmersT[0]
	kmerB = kmersB[0]
        prefixOfKmerT = prefix(kmerT,d)
	prefixOfKmerB = prefix(kmerB,d)
        suffixOfKmerT = suffix(kmerT,d)
	suffixOfKmerB = suffix(kmerB,d)

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
'''

input = open("exampleInput30.txt","r")
output = open("exampleOutput30.txt", "w")

firstLine = next(input)
firstLine = firstLine.strip()
splitFirst = firstLine.split(" ")
d = splitFirst[1]
print(d)


kmerListTop = []
kmerListBottom = []
for line in input:
	line = line.strip()
        #print(line)
        splitLine = line.split("|")
        #print(splitLine)
        kmerListTop.append(splitLine[0])
        kmerListBottom.append(splitLine[1])
print(kmerListTop)
print(kmerListBottom)
input.close()
output.close()

deBruijnGraphSet = deBruijnPairGraphCollectionKmers(kmerListTop, kmerListBottom, d)
fullStr = ""
for i in deBruijnGraphSet:
        suffixStr = i[1][0]
        for j in range(1,len(i[1])):
                suffixStr = suffixStr + "," + i[1][j]
        fullStr = i[0] + " -> " + suffixStr + "\n"
        output.write(fullStr)
input.close()
output.close()
'''
