def Text(i,k,text):
        subsetArr = []
        for letter in range(i,i+k):
                subsetArr.append(text[letter])
        subset = str(''.join(subsetArr))
        return subset

#print(Text(4,3,"GACCATACTG"))

#-----------------------------------------------------------

def PatternCount(text, pattern):
        count = 0
        for i in range(len(text)-len(pattern)+1):
                window = Text(i, len(pattern), text)
                if window  == pattern:
                        count = count+1
        return count

#print(PatternCount("GCGCG","GCG"))

#-----------------------------------------------------------

def FrequentWords(text, k):
        FrequentPatterns = []
        FreqPattDuplicate = []
        Count = [None]*(len(text)-k)
        for i in range(len(text)-k):
                pattern = Text(i,k,text)
                Count[i] = PatternCount(text, pattern)
        maxCount = max(Count)
        for i in range(len(text)-k):
                if Count[i] == maxCount:
                        FreqPattDuplicate.append(Text(i,k,text))
        for x in FreqPattDuplicate:
                if x not in FrequentPatterns:
                        FrequentPatterns.append(x)
        return FrequentPatterns

#print(FrequentWords("ACGTTGCATGTCGCATGATGCATGAGAGCT",4))

#-----------------------------------------------------------------

def HammingDistance(string1, string2):
        distance = 0
        for i in range(len(string1)):
                if string1[i] != string2[i]:
                        distance = distance + 1
        return distance

#-----------------------------------------------------------

def ApproximatePatternCount(text, pattern, d):
	count = 0
        for i in range(len(text)-len(pattern)):
                pattern2 = Text(i, len(pattern),text)
                if HammingDistance(pattern, pattern2) <= d:
                        count = count + 1
        return count

#print(ApproximatePatternCount("CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC","ATTCTGGA",3))

#-------------------------------------------------------------

#def Neighbors(pattern, d):
	

#------------------------------------------------------------

def FrequentWordsWithMismatches(text, k, d):
	FrequentWords = []
	FrequentWordsDuplicate = []
	count = 0
	for i in range(len(text)-k):
		pattern = Text(i, k, text)
		tempCount = ApproximatePatternCount(text, pattern, d)
		if tempCount > count:
			count = tempCount
			FrequentWordsDuplicate *= 0
			FrequentWordsDuplicate.append(str(pattern))
		elif tempCount >= count:
			FrequentWordsDuplicate.append(str(pattern))
	for j in FrequentWordsDuplicate:
		if j not in FrequentWords:
			FrequentWords.append(j)
	return ' '.join([str(i) for i in FrequentWords])

print(FrequentWordsWithMismatches("GGGGTGGGGGGGTGGGTTCCTGGGGGCGTTCGAGGTCTGCGAGGTCTGCGAGGTCTGTTCCTGGGGGCGTTGGGCGTTGGGCGTTCGAGGTCTGGGGGTGGGGGGCGTTTTCCTGGGTCTAAGAACGAGGTCTGTTCCTGGGGGCGTTGTCTAAGAAGGGCGTTGTCTAAGAAGGGCGTTCGAGGTCTGGGGCGTTGGGCGTTGGGGTGGGCGAGGTCTGTTCCTGGTTCCTGGCGAGGTCTGTTCCTGGTTCCTGGGGGCGTTCGAGGTCTGGGGGTGGGCGAGGTCTGCGAGGTCTGGGGGTGGGTTCCTGGGGGGTGGGGGGGTGGGGGGCGTTGTCTAAGAACGAGGTCTGGGGCGTTGTCTAAGAAGGGGTGGGGGGGTGGGGGGCGTTGGGGTGGGGGGGTGGGTTCCTGGCGAGGTCTGGGGCGTTGTCTAAGAATTCCTGGGGGGTGGGTTCCTGGCGAGGTCTGCGAGGTCTGCGAGGTCTGGGGGTGGGGGGGTGGGGTCTAAGAAGTCTAAGAACGAGGTCTGTTCCTGGCGAGGTCTGGGGGTGGGGGGGTGGGGGGGTGGGCGAGGTCTGCGAGGTCTGGTCTAAGAAGGGGTGGGGGGGTGGGCGAGGTCTGCGAGGTCTGGGGGTGGGGTCTAAGAACGAGGTCTGGGGCGTTCGAGGTCTGTTCCTGGGTCTAAGAATTCCTGGGTCTAAGAATTCCTGGGGGCGTTTTCCTGGGGGGTGGGGGGGTGGGGGGGTGGGGTCTAAGAAGGGGTGGGTTCCTGGGGGGTGGGGGGCGTTCGAGGTCTG",5,3))
