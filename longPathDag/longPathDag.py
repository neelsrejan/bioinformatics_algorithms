def topSortDag(graph, start, end):
        stack = []
        visitedNodes = []

	def recursiveTop(graph, start, end):
        	for i in sorted(graph[start]):
                	if i not in visitedNodes:
                        	visitedNodes.append(i)
               			recursiveTop(graph, i, end)
        	stack.insert(0,start)

	recursiveTop(graph, start, end)
	return stack

def longPathDag(graph, source, sink):
	inf = float("-inf")
	distDict = {}
	pathList = []
	for i in graph.keys():
		distDict[i] = inf
	distDict[source] = 0
	
	topOrder = topSortDag(graph, source, sink)
	
	for i in range(len(topOrder)):
		for j in graph[topOrder[i]]:
			potentialVal = int(distDict[topOrder[i]]) + int(graph[topOrder[i]][j])
			prevVal = distDict[j]
			
			if potentialVal > prevVal:
				distDict[j] = potentialVal
				pathList.append([topOrder[i],j,potentialVal])

	path = [sink]
	currNode = sink
	pathLen = distDict[currNode]
	
	while path[0] != source:
		for edge in pathList:
			if edge[1] == currNode and edge[2] == pathLen:
				currNode= edge[0]
				path.insert(0,currNode)
				pathLen = distDict[currNode]
	
	pathFormat = "->".join([i for i in path])			
	lenToSink = str(distDict[sink])

	return lenToSink, pathFormat

def main():
	input = open("input74.txt","r")
	output = open("output74.txt","w")

	startNodeNum = str.strip(next(input))
	endNodeNum = str.strip(next(input))

	graph = {}
	for line in input:
		splitNode = line.split("->")
		splitWeight = splitNode[1].strip().split(":")
		
		if splitNode[0] not in graph:
			graph[splitNode[0]] = {}
			graph[splitNode[0]][splitWeight[0]] = splitWeight[1]
		
		else:	
			graph[splitNode[0]][splitWeight[0]] = splitWeight[1]
		
		if splitWeight[0] not in graph:
                        graph[splitWeight[0]] = {}
	
	longLen, path = longPathDag(graph, startNodeNum, endNodeNum)
	
	output.write(longLen)
	output.write("\n")
	output.write(path)

	output.close()
	input.close()
	
if __name__ == "__main__":
	main()
	
