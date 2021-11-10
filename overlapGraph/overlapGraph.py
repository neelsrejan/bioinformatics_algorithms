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


def overlapGraph(kmers):
	overlapSet = []
	suffixSet = []
	prefixSet = []
	for i in kmers:
		suffixSet.append([i,suffix(i)])
		prefixSet.append([i,prefix(i)])
	for j in suffixSet:
		for k in prefixSet:
			if j[1] == k[1]:
				overlapSet.append(j[0] + " -> " + k[0])
	overlapSet.sort()
	return overlapSet

input = open("input3c.txt","r")
output = open("output3c.txt","w")
kmers = []
for line in input:
	kmers.append(line.strip())

overlap = overlapGraph(kmers)
for i in overlap:
	output.write(i + "\n")

input.close()
output.close()
#print(prefix("neel"))
#print(suffix("neel"))
