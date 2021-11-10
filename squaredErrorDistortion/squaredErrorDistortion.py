def euclideanDist(p1, p2):
        squared = 0 
        for m in range(len(p1)):
                squared = squared + (float(p1[m]) - float(p2[m]))**(2)
        return squared**(0.5)

def squaredErrorDistortion(points, centers):
        minDistArr = []
        for point in points:
                distFromCenters = []
                for center in centers:
                        distFromCenters.append(euclideanDist(point, center))
                minDistArr.append(min(distFromCenters))

	squaredMinDistArr = []
	for i in minDistArr:
		squaredMinDistArr.append(i**(2))

	sum = 0
	for i in squaredMinDistArr:
		sum = sum + i
	dist = sum/len(squaredMinDistArr)
	return round(dist,3)


def main():
	input = open("input67.txt","r")
	output = open("output67.txt","w")

	KandM = next(input).strip()
	KandMArr = KandM.split(" ")
	k = KandMArr[0]
	m = KandMArr[1]

	centers = []
	for i in range(int(k)):
		line = next(input).strip()
		splitCenter = line.split(" ")
		center = []
		for j in range(int(m)):
			center.append(splitCenter[j])
		centers.append(center)
	next(input)
	points = []
	for line in input:
		line = line.strip()
		point = []
		splitPoint = line.split(" ")
		for i in range(int(m)):
			point.append(splitPoint[i])
		points.append(point)

	dist = squaredErrorDistortion(points, centers)

	output.write(str(dist))

	output.close()
	input.close()

if __name__ == "__main__":
	main()

