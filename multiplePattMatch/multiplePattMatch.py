def multiplePattMatch(text, patterns):
        lenPatt = len(patterns[0])
        lenText = len(text)
        index = 0 
        indexArr = []
        while index <= lenText-lenPatt:
                if text[0:lenPatt] in patterns:
                        indexArr.append(index)    
                        text = text[1:]
                else:
                        text = text[1:]
                index = index + 1 
        return indexArr

def main():
        input = open("input58.txt","r")
        output = open("output58.txt","w")

        text = next(input).strip()
        patterns = []
        for line in input:
                line = line.strip()
                patterns.append(line)
        
	indexArr = multiplePattMatch(text, patterns)
        
	for i in range(len(indexArr)-1):
                output.write(str(indexArr[i])+ " ")
        output.write(str(indexArr[-1]))
        
	output.close()
        input.close()

if __name__ == "__main__":
        main()
