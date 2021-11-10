def enumerateRepeat(list):
        organizedList = []
        countOfA = 0
        countOfT = 0
        countOfG = 0
        countOfC = 0
        countOfS = 0
        for letter in list:
                if letter == "A":
                        organizedList.append((letter, countOfA))
                        countOfA = countOfA + 1
                elif letter == "T":
                        organizedList.append((letter, countOfT))
                        countOfT = countOfT + 1
                elif letter == "G":
                        organizedList.append((letter, countOfG))
                        countOfG = countOfG + 1
                elif letter == "C":
                        organizedList.append((letter, countOfC))
                        countOfC = countOfC + 1
                elif letter == "$":
                        organizedList.append((letter, countOfS))
                        coungOfS = countOfS + 1
        return organizedList

def lastToFirst(first, last, index):
        indexNow = -1
        letterFinding = last[int(index)][0]
        indexFinding = last[int(index)][1]
        for idx, tuple  in enumerate(first):
                if tuple[0] == letterFinding and tuple[1] == indexFinding:
                        indexNow = idx
                        break
        return indexNow

def BWMatchingNew(first, last, pattern):
        patternArr = [i for i in pattern]
        top = 0
        bottom = len(last)-1
        lastLetterArr = [i[0] for i in last]
        while top <= bottom:
                if len(patternArr) != 0:
                        symbol = patternArr[-1]
                        del patternArr[-1]

                        if symbol in lastLetterArr[top:bottom+1]:
                                symbolIndex = []
                                for i in range(top, top + (bottom-top)+1):
                                        if symbol == last[i][0]:
                                                symbolIndex.append(i)

                                topIdx = symbolIndex[0]
                                bottomIdx = symbolIndex[-1]
                                top = lastToFirst(first, last, topIdx)
                                bottom = lastToFirst(first, last, bottomIdx)
                        else:
                                return 0
                else:
                        return bottom - top + 1


def main():
        input = open("input63.txt", "r")
        output = open("output63.txt", "w")

        lastColStrForm = next(input).strip()
        patternsInLine = next(input).strip()
        patternsInArr = patternsInLine.split(" ")
        lastColBWT = [i for i in lastColStrForm]
        firstColBWT = lastColBWT[:]
        firstColBWT.sort()

        organizedLastColBWT = enumerateRepeat(lastColBWT)
        organizedFirstColBWT = enumerateRepeat(firstColBWT)

        numberOfMatches = []
        for pattern in patternsInArr:
                numberOfMatches.append(BWMatchingNew(organizedFirstColBWT, organizedLastColBWT, pattern))
    
        count = 0 
        for i in range(len(numberOfMatches)-1):
                output.write(str(numberOfMatches[i]))
                output.write(" ")
                count = count + 1 
        output.write(str(numberOfMatches[count]))

        output.close()
        input.close()


if __name__ == "__main__":
        main()
