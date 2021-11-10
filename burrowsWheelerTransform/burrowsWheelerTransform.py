def bwt(text):
	permutations = [text]
	for i in range(len(text)-1):
		text = text[-1] + text[0:len(text)-1]
		permutations.append(text)
	permutations.sort()
	
	order = []
	for i in permutations:
		order.append(i[-1])
	return ''.join([i for i in  order])

def main():
	input = open("input59.txt","r")
	output = open("output59.txt", "w")

	text = next(input).strip()
	str = bwt(text)
	output.write(str)

	output.close()
	input.close()
	

if __name__ == "__main__":
	main()
