def euclideanDist(p1, p2):
	squared = 0
	for m in range(len(p1)):
		squared = squared + (float(p1[m]) - float(p2[m]))**(2)
	return squared**(0.5)

def maxDistIdx(points, centers):
	minDistArr = []
	for point in points:
		distFromCenters = []
		for center in centers:
			distFromCenters.append(euclideanDist(point, center))
		minDistArr.append(min(distFromCenters))
	
	maxVal = max(minDistArr)
	maxIdx = minDistArr.index(maxVal)
	return maxIdx


def farthestFirstTraversal(points, k):
	centers = [points[0]]
	del points[0]
	while len(centers) < k:
		dataPointIdx = maxDistIdx(points, centers)
		centers.append(points[dataPointIdx])
		del points[dataPointIdx]
	return centers

def main():
	input = open("input66.txt","r")
	output = open("output66.txt","w")

	KandM= next(input).strip()
	KandMArr = KandM.split(" ")
	k = KandMArr[0]
	m = KandMArr[1]

	points = []
	for line in input:
		line = line.strip()
		dimArr = line.split(" ")
		coordinates = []
		for dim in range(int(m)):
			coordinates.append(dimArr[dim])
		points.append(coordinates)
	
	centers = farthestFirstTraversal(points, int(k))
	
	for center in centers:
		for i in range(int(m)-1):
			output.write(center[i])
			output.write(" ")
		output.write(center[int(m)-1])
		output.write("\n")

	output.close()
	input.close()

if __name__ == "__main__":
	main()
