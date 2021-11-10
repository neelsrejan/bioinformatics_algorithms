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
                        edge = [nodes[2*i-1], nodes[2*i]]
                        edges.append(edge)
        return edges

def findBlue(val, blue):
	for edge in blue:
		if val == edge[0]:
			val = edge[1]
			blue.remove(edge)
		elif val == edge[1]:
			val = edge[0]
			blue.remove(edge)
	return val, blue

def findRed(val, red):
	for edge in red:
		if val == edge[0]:
                        val = edge[1]
                        red.remove(edge)
		elif val == edge[1]:
                        val = edge[0]
                        red.remove(edge)
        return val, red

def breakDistance(red, blue):
	cycle = 0
	while len(red) != 0:
		start = red[0][1]
 	      	end = red[0][0]
       		del red[0]
		while start != end:
			start, blue = findBlue(start, blue)
			#print("start is:")
			#print(start)
			#print("blue is:")
			#print(len(blue))
			start, red = findRed(start, red)
			#print("start is:")
                        #print(start)
                        #print("red is:")
                        #print(len(red)) 
		cycle = cycle + 1
	return cycle

def main():
	input = open("input44.txt","r")
	output = open("output44.txt","w")

	genome1 = next(input).strip()
	genome2 = next(input).strip()
	
	genome1Split = genome1.split(")(")
	genome1Arr = []
	maxSynteny = 0
	for i in genome1Split:	
		i = i.strip("()")
		synteny = i.split(" ")
		for x in synteny:
			if int(x) > maxSynteny:
				maxSynteny = int(x)
		synteny.append(synteny[0])
		genome1Arr.append(synteny)
		
	
	genome2Split = genome2.split(")(")
	genome2Arr = []
	for i in genome2Split:
		i = i.strip("()")
		synteny = i.split(" ")
		for x in synteny:
                       	if int(x) > maxSynteny:
                               	maxSynteny = int(x)
		synteny.append(synteny[0])
		genome2Arr.append(synteny)
	
	#print(len(genome1Arr)-1)
	#print(genome2Arr)

	red = coloredEdges(genome1Arr)
	blue = coloredEdges(genome2Arr)

	#print(red)
	#print(blue)

	numCycle = breakDistance(red, blue)
	#val, blue = findBlue(3, blue)
	#print(val)
	#print(blue)
	
	#print(maxSynteny)
	#print(numCycle)
	dist = maxSynteny - numCycle
	#print(dist)
	
	output.write(str(dist))

	output.close()
	input.close()

if __name__ == "__main__":
	main()
