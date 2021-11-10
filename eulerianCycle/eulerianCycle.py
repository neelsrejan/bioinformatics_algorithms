import random

def eulerianCycle(adjListDict):
	currCycleWithUnexplored = {}
	#currCyclePath = []
	#startKey = random.choice(adjListDict.keys())
        #currCyclePath.append(startKey)
	
	while(len(adjListDict) != 0):
		currCyclePath = []
	        startKey = random.choice(adjListDict.keys())
       		currCyclePath.append(startKey)

		if len(adjListDict[startKey]) > 1:
			nextNode = random.choice(adjListDict[startKey])
			adjListDict[startKey].remove[nextNode]
			currCycleWithUnexplored[startKey] = adjListDict[startKey]
		elif len(adjListDict[startIdx] == 1:
			nextNode = random.choice(adjListDict[startKey])
                        currCyclePath.append(nextNode)
			adjListDict[startKey].remove[nextNode]
			del adjListDict[startKey]




input = open("exampleInput3f.txt","r")
output = open("exampleOutput3f.txt","w")
sourceNode = []
sinkNode = []
for line in input:
	line = line.strip()
	splitLine = line.split(" -> ")
	sourceNode.append(splitLine[0])
#	splitLine[1].split(",")
	sinkNode.append(splitLine[1])
#sinkNode.split(",")
valueSet = []
for i in range(len(sinkNode)):
	multipleNeighbor = sinkNode[i].split(",")
	valueSet.append(multipleNeighbor)

graph = {}
for i in range(len(sourceNode)):
		graph[sourceNode[i]] = valueSet[i]
#print(graph)
eulerianCycle(graph)

