def graphToGenome(edges):
	path = []
	appended = 1
	for i in range(len(edges)):
		path.append("(")
		for j in range(0, len(edges[i]), 2):
			if edges[i][j] % 2 == 0:
				if path[-1] == "(":
					path.append("+" + str(appended))
					appended = appended + 1
				else:
					path.append(" +" + str(appended))
					appended = appended + 1
			else:
				if path[-1] == "(":
					path.append("-" + str(appended))
					appended = appended + 1
				else:
					path.append(" -" + str(appended))
					appended = appended + 1
		path.append(")")
	return ''.join([i for i in path])

def main():
	input = open("exampleInput50.txt","r")
	output = open("exampleOutput50.txt","w")

	edgesTogether = next(input).strip()
	edgesIndividual = edgesTogether.replace(",","").replace("(","").replace(")","")
	edgesSetStr = edgesIndividual.split(" ")
	edgesSetInt = [int(i) for i in edgesSetStr]
	#print(edgesSetInt)
	
	edgesWithCycle = []
	start = 0
	for i in range(0, len(edgesSetInt)-1,2):
		if edgesSetInt[i] > edgesSetInt[i+1]:
			cycle = edgesSetInt[start:i+2]
			start = i+2
			edgesWithCycle.append(cycle)
	print(edgesWithCycle)

	path = graphToGenome(edgesWithCycle)
	
	output.write(path)

	output.close()
	input.close()

if __name__ == "__main__":
	main()
