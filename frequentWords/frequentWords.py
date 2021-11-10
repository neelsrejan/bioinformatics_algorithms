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

print(FrequentWords("CGTCCCCAGTAGCTTTGTAGCTTTACGGTAGAAACGTCCGGTAGCTTTGTAGCTTTCGTCCCCACGTCCCCAAACGTCCGCGTCCCCACGTCCCCAACGGTAGATCATAATTAGAACGTCCGGTAGCTTTAACGTCCGCGTCCCCATCATAATTAGAACGTCCGAACGTCCGACGGTAGAGTAGCTTTAACGTCCGACGGTAGATCATAATTAGAACGTCCGTCATAATTAGAACGTCCGAACGTCCGCGTCCCCAGTAGCTTTGTAGCTTTGTAGCTTTCGTCCCCATCATAATTAGACGGTAGAACGGTAGACGTCCCCAACGGTAGACGTCCCCACGTCCCCAAACGTCCGTCATAATTAGGTAGCTTTCGTCCCCAAACGTCCGACGGTAGATCATAATTAGGTAGCTTTACGGTAGATCATAATTAGTCATAATTAGCGTCCCCAACGGTAGAGTAGCTTTCGTCCCCAAACGTCCGCGTCCCCAGTAGCTTTAACGTCCGTCATAATTAGAACGTCCGCGTCCCCATCATAATTAGACGGTAGAAACGTCCGCGTCCCCATCATAATTAGGTAGCTTTGTAGCTTTACGGTAGATCATAATTAGTCATAATTAGCGTCCCCAACGGTAGAACGGTAGAACGGTAGATCATAATTAGCGTCCCCAAACGTCCGCGTCCCCATCATAATTAGGTAGCTTTCGTCCCCAAACGTCCGCGTCCCCATCATAATTAGCGTCCCCAAACGTCCGTCATAATTAGACGGTAGAGTAGCTTTGTAGCTTTGTAGCTTTTCATAATTAGCGTCCCCACGTCCCCAACGGTAGAAACGTCCGGTAGCTTTGTAGCTTTAACGTCCGAACGTCCGTCATAATTAGAACGTCCGACGGTAGATCATAATTAGTCATAATTAGAACGTCCG",11))
