def suffixArrToLongestRepeat(text1):
        suffixes = []
        for i in range(len(text1)):
                suffixes.append((text1[i:],i))
        suffixes.sort()

	lcp = [0]
	for i in range(len(suffixes)-1):
		substring1 = suffixes[i][0]
		substring2 = suffixes[i+1][0]
		count = 0
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
	input = open("input54.txt","r")
	output = open("output54.txt", "w")
	
	text = next(input).strip()
	
	substring = suffixArrToLongestRepeat(text)
	
	output.write(substring)
	
	output.close()
	input.close()

if __name__ == "__main__":
	main()
