def suffixArr(text):
	suffixes = []
        for i in range(len(text)):
		suffixes.append((text[i:],i))
        suffixes.sort()
	#print(suffixes)

	order = []
	for i in suffixes:
		order.append(i[1])
	return order

def main():
	input = open("input57.txt","r")
	output = open("output57.txt","w")

	text = next(input).strip()
	order = suffixArr(text)

	maxOrder = 0
	for i in range(len(order)-1):
		output.write(str(order[i]) + ", ")
		maxOrder = i
	output.write(str(order[maxOrder+1]))

	output.close()
	input.close()

if __name__ == "__main__":
	main()
