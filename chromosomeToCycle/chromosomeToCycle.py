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

def main():
	input = open("input47.txt","r")
	output = open("output47.txt","w")

	numsStr = next(input).strip()
	numsStr = numsStr.strip("()")
	numsStrArr = numsStr.split(" ")
	#print(numsStrArr)
	#fun = ['+1', '-3', '-6', '-5']
	nodes = chromosomeToCycle(numsStrArr)
	
	output.write("(")
	secondToLast = 0
	for i in range(len(nodes)-1):
		output.write(str(nodes[i]))
		output.write(" ")
		secondToLast = i
	output.write(str(nodes[secondToLast+1]))
	output.write(")")

	output.close()
	input.close()

if __name__ == "__main__":
	main()
