def TrieMatching(text, words):
	lenWords = len(words[0])
	lenText = len(text)
	idx = 0
	idxArr = []
	while(idx <= lenText-lenWords):
		if text[0:lenWords] in words:
			idxArr.append(idx)	
			text = text[1:]
		else:
			text = text[1:]
		idx = idx + 1
	return idxArr

def main():
        input = open("input52.txt","r")
        output = open("output52.txt","w")

	text = next(input).strip()
        words = []
        for line in input:
                line = line.strip()
                words.append(line)
	#print(text)
	#print(words)
        idxArr = TrieMatching(text, words)
        for i in range(len(idxArr)-1):
		output.write(str(idxArr[i])+ " ")
	output.write(str(idxArr[-1]))
	output.close()
        input.close()
	
if __name__ == "__main__":
        main()
