def euclideanDist(p1, p2):
        squared = 0 
        for m in range(len(p1)):
                squared = squared + (float(p1[m]) - float(p2[m]))**(2)
        return squared**(0.5)

def invert(distArr, n, m):
	invert = []
	for i in range(m):
		smallArr = []
		for j in range(n):
			smallArr.append(distArr[j][i])
		invert.append(smallArr)
	return invert


def centersToClusters(points, centers, b):
        distArr = []
	e = 2.718
	n = len(centers)
	m = len(points)
        for center in centers:
                distFromCenters = []
                for point in points:
                        distFromCenters.append(euclideanDist(point[1], center[1]))
		distArr.append(distFromCenters)
	#print(distArr)

	distArrInv = invert(distArr, n, m)
	#print(distArrInv)	
	hiddenArr = []
	for i in range(n):
		cluster = []
		for j in range(m):
			val = distArr[i][j]
			#print("Val", val)
			hidNumerator = e**((-b)*(val))
			vals = distArrInv[j]
			#print("Vals",vals)
			hidDenom = 0
			for x in vals:
				hidDenom = hidDenom + e**((-b)*(x))
			hidNum = hidNumerator/hidDenom
			#cluster.append("{:.3f}".format(hidNum))
			#cluster.append(round(hidNum,3))
			cluster.append(hidNum)
		hiddenArr.append(cluster)
	return hiddenArr

def clustersToCenters(hiddenArr, n, m, numPoints, points): 
        centers = []
	#print(hiddenArr)
	#print(n,m)
	for i in range(n):
		#print("\n")
		center = []
		for j in range(m):
			sumNumerator = 0
			sumDenom = 0
			for dim in range(numPoints):
				#print(hiddenArr[i][dim],i,dim)
				#print(points[dim][1][j],dim,j)
				sumNumerator = sumNumerator + (float(hiddenArr[i][dim]))*(float(points[dim][1][j]))
				#print(sumNumerator)
				sumDenom = sumDenom + (float(hiddenArr[i][dim]))
			#print(sumNumerator)
			#print(sumDenom)
			avg = sumNumerator/sumDenom
			#print("avg is",avg)
			#center.append("{:.3f}".format(avg))
			#center.append(round(avg,3))
			center.append(avg)
			#print(center)
		centers.append([i,center])
	return centers

def softLloyd(points, centers, k, m, b):
        count = 0
	n = k
	numPoints = len(points)
	#print(n)
	#print(m)
	#print(k)
        while count < 200:
                hiddenArr = centersToClusters(points, centers, b)
		#print("hidden",hiddenArr)
                centers = clustersToCenters(hiddenArr, n, m, numPoints, points)
		#print(centers)
		count = count + 1
        #print("before alter",centers)
	newCenter = []
	for i in range(len(centers)):
		centerRounded = []
		for j in range(len(centers[i][1])):
			centerRounded.append("{:.3f}".format(centers[i][1][j]))
		newCenter.append([i,centerRounded])
	return newCenter		
			

def main():
	#input = open("small.txt","r")
        input = open("input69.txt","r")
        output = open("output69.txt","w")

        KandM = next(input).strip()
        KandMArr = KandM.split(" ")
        k = int(KandMArr[0])
        m = int(KandMArr[1])
        b = float(next(input).strip())

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

        #print(k)
        #print(m)
        #print(b)
        #print(points)
        centersSmall = [[0,['-2.5', '0.0']], [1, ['2.5', '0.0']]]
        #print(centers)
        #print(centersSmall)
	#print("\n")
	#hiddenArr = centersToClusters(points, centersSmall, b)
	
	#clustersToCenters(hiddenArr, len(centersSmall), len(points), m, points)
	finalCenters = softLloyd(points, centers, k, m, b)
        
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
