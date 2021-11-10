def suffixArrToLongestCommonSubsequence(text):
        suffixes = []
	count = 0
        for i in range(len(text)):
		if i == (len(text)/2)-1 or i == len(text)-1:
			count = count + 1
                else:
			if count == 0:
				suffixes.append((text[i:], i, "r"))
			else:
				suffixes.append((text[i:], i, "b"))
        suffixes.sort()
        
	lcp = [0] 
        for i in range(len(suffixes)-1):
                substring1 = suffixes[i][0]
                substring2 = suffixes[i+1][0]
                count = 0
		if suffixes[i][2] == suffixes[i+1][2]:
			lcp.append(-1)
		else:
			if len(substring1) < len(substring2):
				for i in range(len(substring1)):
					if substring1[i] == substring2[i]:
						count = count + 1 
					else:
						break
				lcp.append(count)
			else:
				for i in range(len(substring2)+1):
					if substring2[i] == substring1[i]:
						count = count + 1 
					else:
						break
				lcp.append(count)

	maxLcp = max(lcp)
        lcpIndex = lcp.index(maxLcp)

        substring = suffixes[lcpIndex-1][0]
        longestRepeat = substring[0:maxLcp]

        return str(longestRepeat)

def main():
        input = open("input55.txt","r")
        output = open("output55.txt", "w")

        str1 = next(input).strip()
	str2 = next(input).strip()
	#print(len(str1))
	text = str1 + "#" + str2 + "$"
	#print(text)
	#print(len(text))
	#text1 = "abca#bcad$daca%"
        substring = suffixArrToLongestCommonSubsequence(text)

        output.write(substring)

        output.close()
        input.close()

if __name__ == "__main__":
        main()
