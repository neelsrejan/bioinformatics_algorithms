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

def Reverse(text):
        reversed = []
        for i in range(len(text)-1,-1,-1):
                reversed.append(text[i])
        return ''.join(reversed)

#print(Reverse("AAAACCCGGT"))

#----------------------------------------------

def Complement(text):
        complemented = []
        for i in text:
                if i == "A":
                        i = "T"
                elif i == "T":
                        i = "A"
                elif i == "G":
                        i = "C"
                elif i == "C":
                        i = "G"
                complemented.append(i)
        return ''.join(complemented)

#print(Complement("TGGCCCAAAA"))

#-----------------------------------------------

def ReverseComplement(text):
        reversed = Reverse(text)
        return Complement(reversed)

#print(ReverseComplement("AAAACCCGGT"))

#-------------------------------------------------

def ApproximatePatternCount(text, pattern, d):
        count = 0
        for i in range(len(text)-len(pattern)):
                pattern2 = Text(i, len(pattern),text)
                if HammingDistance(pattern, pattern2) <= d:
                        count = count + 1
        return count

#print(ApproximatePatternCount("CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC","ATTCTGGA",3))

#-------------------------------------------------------------

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
        return FrequentWords

#print(FrequentWordsWithMismatches("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4, 1))

#----------------------------------------------------------------------------

def Suffix(pattern):
	if len(pattern) < 1:
		return
	else:
		return pattern[1:] 

#----------------------------------------------------------------------------

def Quotient(dividend, divisor):
	return dividend / divisor

#----------------------------------------------------------------------------

def Remainder(dividend, divisor):
        return dividend % divisor

#----------------------------------------------------------------------------

def NumberToSymbol(number):
        if number == 0:
                return "A"
        elif number  == 1:
                return "C"
        elif number == 2:
                return "G"
        elif number == 3:
                return "T"
#print(NumberToSymbol(0))
#print(NumberToSymbol(1))
#print(NumberToSymbol(2))
#print(NumberToSymbol(3))

#----------------------------------------------------------------------------

def SymbolToNumber(symbol):
	if symbol == "A":
		return 0
	elif symbol == "C":
		return 1
	elif symbol == "G":
		return 2
	elif symbol == "T":
		return 3
#print(SymbolToNumber("A"))
#print(SymbolToNumber("C"))
#print(SymbolToNumber("G"))
#print(SymbolToNumber("T"))

#----------------------------------------------------------------------------

def PatternToNumber(pattern):
	if len(pattern) == 0:
		return 0
	symbol = pattern[-1]
	prefix = pattern[0:len(pattern)-1]
	return 4*PatternToNumber(prefix) + SymbolToNumber(symbol)

#print(PatternToNumber("AGT"))

#----------------------------------------------------------------------------

def NumberToPattern(index, k):
	if k == 1:
		return NumberToSymbol(index)
	prefixIndex = Quotient(index,4)
	remainder = Remainder(index,4)
	symbol = NumberToSymbol(remainder)
	prefixPattern = NumberToPattern(prefixIndex,k-1)
	return str(prefixPattern) + str(symbol)

#print(NumberToPattern(11,3))
#print(NumberToPattern(9904,7))


#----------------------------------------------------------------------------

def Neighbors(pattern, d):
	if d == 0:
		return {pattern}
	if len(pattern) == 1:
		 return {"A","C","G","T"}
	Neighborhood = set()
	suffix = pattern[1:]
	SuffixNeighbors = Neighbors(Suffix(pattern),d)
	for text in SuffixNeighbors:
		if HammingDistance(Suffix(pattern),text) < d:
			Neighborhood.add("A" + str(text))
			Neighborhood.add("C" + str(text))
			Neighborhood.add("G" + str(text))
			Neighborhood.add("T" + str(text))
		else:
			Neighborhood.add(str(pattern[0])+ str(text))
	#print(Neighborhood)
	#NeighborList = []
	#for j in range(len(Neighborhood)):
	#	NeighborList.append(Neighborhood.pop())
	#return Neighborhood 
	#return ' '.join(Neighborhood)
	#return Neighborhood.split()

#print(Neighbors("ACG",1))
#print(" ")
#----------------------------------------------------------------------------

def Neighbors2(pattern, d):
        if d == 0:
                return {pattern}
        if len(pattern) == 1:
                 return {"A","C","G","T"}
        Neighborhood = set()
        Suffix = pattern[1:]
        SuffixNeighbors = Neighbors(Suffix,d)
        for text in SuffixNeighbors:
                if HammingDistance(Suffix(pattern),text) < d:
                        Neighborhood.add("A" + str(text))
                        Neighborhood.add("C" + str(text))
                        Neighborhood.add("G" + str(text))
                        Neighborhood.add("T" + str(text))
                else:
                        Neighborhood.add(str(pattern[0])+ str(text))
       #print(Neighborhood)
        NeighborList = []
        for j in range(len(Neighborhood)):
                NeighborList.append(Neighborhood.pop())
	#return NeighborList
        #return ' '.join(str(x) for x in NeighborList)
	return NeighborList.split()


#print(Neighbors2("ACG",1))


#----------------------------------------------------------------------------

def Neighbors3(pattern, d):
	if d == 0:
		return { pattern }
	if len(pattern) == 1:
		return { "A", "C", "G", "T" }
  
	Neighborhood = set()
	for i in range(len(pattern)):
		prefix = str(pattern[0:i])
		suffix = str(pattern[i+1:])
		if i == 0:
			prefix = ""
		if i == len(pattern)-1:
			suffix = ""
      
		Neighborhood.add(prefix + "A" + suffix)
		Neighborhood.add(prefix + "C" + suffix)
		Neighborhood.add(prefix + "G" + suffix)
		Neighborhood.add(prefix + "T" + suffix)

	NeighborhoodList = list(Neighborhood)
	return ' '.join(str(i) for i in NeighborhoodList)

print(Neighbors3("ACG",1))

#----------------------------------------------------------------------------

def FrequentWordsWithMismatchesAndRevComp(text, k, d):
        FrequentWords = []
        FrequentWordsDuplicate = []
        sumCount = 0
        for i in range(len(text)-k):
                pattern = Text(i, k, text)
		revPatt = ReverseComplement(pattern)
                tempCountPatt = ApproximatePatternCount(text, pattern, d)
		tempCountRevPatt = ApproximatePatternCount(text, revPatt, d)
		tempSumCount = tempCountPatt + tempCountRevPatt
                if tempSumCount > sumCount:
                        SumCount = tempSumCount
                        FrequentWordsDuplicate *= 0
                        FrequentWordsDuplicate.append(str(pattern))
                elif tempCount >= count:
                        FrequentWordsDuplicate.append(str(pattern))
        for j in FrequentWordsDuplicate:
                if j not in FrequentWords:
                        FrequentWords.append(j)
        return FrequentWords

#print(FrequentWordsWithMismatchesAndRevComp("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4, 1))
#print(FrequentWordsWithMismatchesAndRevComp("CTTGCCGGCGCCGATTATACGATCGCGGCCGCTTGCCTTCTTTATAATGCATCGGCGCCGCGATCTTGCTATATACGTACGCTTCGCTTGCATCTTGCGCGCATTACGTACTTATCGATTACTTATCTTCGATGCCGGCCGGCATATGCCGCTTTAGCATCGATCGATCGTACTTTACGCGTATAGCCGCTTCGCTTGCCGTACGCGATGCTAGCATATGCTAGCGCTAATTACTTAT", 9, 3))

