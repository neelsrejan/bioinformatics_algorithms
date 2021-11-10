def topSortDag(graph, noIncoming, incoming):
	topOrder = []
	
	while len(noIncoming) != 0:
		a =noIncoming[0]
		noIncoming = noIncoming[1:]
		topOrder.append(a)
		if a in graph:
			edges = graph[a]
			for i in range(len(edges)-1,-1,-1):
				b = edges[-1]
				edges = edges[0:len(edges)-1]
				graph.update({a: edges})
				if b not in noIncoming:
					incoming.remove(b)
					if b not in incoming:
						noIncoming.append(b)
	return topOrder 
	

def main():
	input = open("input41.txt","r")
	output = open("output41.txt","w")
	
	graph = {}
	noIncoming = []
	incoming = []
	for line in input:
		line = line.strip()
		splitStartNode = line.split(" -> ")
		#print(splitStartNode[0])
		
		splitEndNodes = splitStartNode[1].split(",")
				
		if splitStartNode[0] not in incoming:
			if splitStartNode[0] not in noIncoming:
				noIncoming.append(splitStartNode[0])
			#print("noIncoming")
			#print(noIncoming)
			for i in splitEndNodes:
				incoming.append(i)
			#print("incoming")
			#print(incoming)
			#print("\n")
		else:
			for i in splitEndNodes:
				incoming.append(i)
			#print("noIncoming")
			#print(noIncoming)
			#print("incoming")
			#print(incoming)
			#print("\n")
		
		if splitStartNode[0] not in graph:
			graph[splitStartNode[0]] = splitEndNodes	
	
	#print(graph)
	#print("\n")
	#print(noIncoming)
	#print(incoming)
	#print("\n")
	topOrder = topSortDag(graph, noIncoming, incoming)
	output.write(', '.join(i for i in topOrder))
	
	output.close()
	input.close()

if __name__ == "__main__":
	main()
