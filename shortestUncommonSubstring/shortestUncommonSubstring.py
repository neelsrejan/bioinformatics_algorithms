def shortestUncommonSubstring(str1, str2):
	lenStr1 = len(str1)
	longToShortSet = set()
	for i in range(lenStr1):
		sub1 = set()
		sub2 = set()
		substringLen = lenStr1-i
		for j in range(i+1):
			sub1.add(str1[j:substringLen+j])
			sub2.add(str2[j:substringLen+j])
			'''
			for x in sub1:
				if x not in sub2:
					longToShortSet.add(x)
					'''
		#print(sub1)
		#print(sub2)
		#print("\n")
		sub = sub1 - sub2
		#print(sub)
		longToShortSet.update(sub)
	listLongToShort = list(longToShortSet)
	listLongToShort.sort(key = len)
	listLongToShort.reverse()
	return listLongToShort[-1]

def main():
	input = open("input56.txt","r")
	output = open("output56.txt","w")

	str1 = next(input).strip()
	str2 = next(input).strip()

	A = set()
	A.add('A')
	A.add('C')
	B = set()
	B.add('C')
	B.add('T')
	C = A-B
	#print(C)
	D = set()
	D.add('G')
	#print(D.union(C))
	#print(D)
	uncommon = shortestUncommonSubstring(str1, str2)

	output.write(str(uncommon))

	output.close()
	input.close()

if __name__ == "__main__":
	main()
