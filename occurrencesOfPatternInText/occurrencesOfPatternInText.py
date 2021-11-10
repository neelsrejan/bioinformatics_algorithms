def occurrencesOfPatternInText(text, multiplePatterns):
        lenPatterns = len(multiplePatterns[0])
        lenText = len(text)
        idx = 0 
        arrIndex = []
        while idx <= lenText-lenPatterns:
                if text[0:lenPatterns] in multiplePatterns:
                        arrIndex.append(idx)    
                        text = text[1:]
                else:
                        text = text[1:]
                idx = idx + 1 
        return arrIndex

def main():
        input = open("input64.txt","r")
        output = open("output64.txt","w")

        text = next(input).strip()
        multiplePatterns = []
        for line in input:
                line = line.strip()
                multiplePatterns.append(line)
    
        arrOfIndexes = occurrencesOfPatternInText(text, multiplePatterns)
    
        for i in range(len(arrOfIndexes)-1):
                output.write(str(arrOfIndexes[i])+ " ")
        output.write(str(arrOfIndexes[-1]))
    
        output.close()
        input.close()

if __name__ == "__main__":
        main()
