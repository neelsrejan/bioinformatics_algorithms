def chromosomeToCycle(chromosome):
        inf = float("-inf")
        nodes = [inf for i in range(2*len(chromosome))]
        for j in range(len(chromosome)):
                i = chromosome[j]
                if i[0] == "+":
                        nodes[2*j] = 2 * int(i[1:]) -1
                        nodes[2*j+1] = 2 * int(i[1:])
                else:
                        nodes[2*j] = 2 * int(i[1:])
                        nodes[2*j+1] = 2 * int(i[1:]) -1
        return nodes

def coloredEdges(genome):
	edges = []
	for i in genome:
		nodes = chromosomeToCycle(i)
		#print(nodes)
		
		for i in range(1,len(i)):
			edge = "("
			edge = edge + str(nodes[2*i-1])
			edge = edge + ", "
			edge = edge + str(nodes[2*i])
			edge = edge + ")"
			edges.append(edge)
	return edges
			
def main():
	input = open("exampleInput49.txt","r")
	output = open("exampleOutput49.txt","w")
	
	genome = next(input).strip()
	chromosome = genome.strip("()")
	chromosomeStr = chromosome.split(")(")	
	chromosome = [chromosomeStr[i].split(" ") for i in range(len(chromosomeStr))]

	print(chromosome)
	for i in range(len(chromosome)):
		chromosome[i].append(chromosome[i][0])
	print(chromosome)
	edges = coloredEdges(chromosome)
	
	secondToLast = 0
	for i in range(len(edges)-1):
		output.write(edges[i])
		output.write(", ")
		secondToLast = i
	output.write(edges[secondToLast+1])
	output.write("\n")
	
	output.close()
	input.close()

if __name__ == "__main__":
	main()
