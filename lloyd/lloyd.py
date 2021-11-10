def euclideanDist(p1, p2):
        squared = 0 
        for m in range(len(p1)):
                squared = squared + (float(p1[m]) - float(p2[m]))**(2)
        return squared**(0.5)

def centersToClusters(points, centers):
        minDistArr = []
        for point in points:
                distFromCenters = []
                for center in centers:
			distFromCenters.append(euclideanDist(point[1], center[1]))
		minDistInArr = min(distFromCenters)
		indexMin = distFromCenters.index(minDistInArr)
		point[0] = indexMin
                minDistArr.append(minDistInArr)

        squaredMinDistArr = []
        for i in minDistArr:
                squaredMinDistArr.append(i**(2))

        sum = 0 
        for i in squaredMinDistArr:
                sum = sum + i 
        dist = sum/len(squaredMinDistArr)
        formatted = "{:.3f}".format(dist)
	return formatted, points, centers


def clustersToCenters(points, k, m):
	centers = []
	for dim in range(k):
		partialPoints = []
		for point in points:
			if dim == point[0]:
				partialPoints.append(point)
		newCenter = []
		for dimension in range(m):
			sum = 0.0
			for dimPoint in partialPoints:
				sum = sum + float(dimPoint[1][dimension])
			formatted = "{:.3f}".format(sum/len(partialPoints))
			newCenter.append(formatted)
		centers.append([dim, newCenter])
	return centers

def lloyd(points, centers, k, m):
	error = -1
	diffError = True
	while(diffError):
		newError, points, centers = centersToClusters(points, centers)
		centers = clustersToCenters(points, k, m)
		if error == newError:
			diffError = False
		error = newError
	return centers

def main():
	input = open("input68.txt","r")
	output = open("output68.txt","w")

	KandM = next(input).strip()
	KandMArr = KandM.split(" ")
	k = KandMArr[0]
	m = KandMArr[1]

	points = []
	for line in input:
		line = line.strip()
		location = line.split(" ")
		pointAndCluster = []
		point = []
		for i in range(int(m)):
			point.append(location[i])
		pointAndCluster = [-1, point]
		points.append(pointAndCluster)
	
	centers = []
	for i in range(int(k)):
		centers.append([i, points[i][1]])
	
	finalCenters = lloyd(points, centers, int(k), int(m))

	count = 0
	justCenters = []
	for i in finalCenters:
		justCenters.append(i[1])

	for i in range(len(justCenters)-1):
		for dim in range(int(m)-1):
			output.write(justCenters[i][dim])
			output.write(" ")
		output.write(justCenters[i][int(m)-1])
		output.write("\n")
	for idx in range(int(m)-1):
		output.write(justCenters[-1][idx])
		output.write(" ")
	output.write(justCenters[-1][int(m)-1])

	output.close()
	input.close()
		

if __name__ == "__main__":
	main()
