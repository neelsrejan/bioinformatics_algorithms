def cycleToChromosome(nodes):
	inf = float("-inf")
	chromosome = [inf for i in range(len(nodes)/2)]
	for i in range(len(nodes)/2):
		if nodes[2*i] < nodes[2*i+1]:
			#print(nodes[2*i])
			#print(nodes[2*i+1])
			intChrome = int(nodes[2*i+1])/2
			chromosome[i] = "+" + str(intChrome)
		else:
			intChrome = int(nodes[2*i])/2
			chromosome[i] = "-" + str(intChrome)
	return chromosome

	
def main():
        input = open("input48.txt","r")
        output = open("output48.txt","w")

        numsStr = next(input).strip()
        numsStr = numsStr.strip("()")
        numsStrArr = numsStr.split(" ")
        #print(numsStrArr)
	nums = [int(i) for i in numsStrArr]
	#print(nums)
	
        chromosome = cycleToChromosome(nums)
	
        output.write("(")
        secondToLast = 0
        for i in range(len(chromosome)-1):
                output.write(str(chromosome[i]))
                output.write(" ")
                secondToLast = i
        output.write(str(chromosome[secondToLast+1]))
        output.write(")")

        output.close()
        input.close()
	
if __name__ == "__main__":
        main()
