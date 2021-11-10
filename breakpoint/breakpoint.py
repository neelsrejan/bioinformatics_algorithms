def breakpoint(nums):
	numBreaks = 0
	for i in range(len(nums)-1):
		if nums[i] + 1 != nums[i+1]:
			numBreaks = numBreaks + 1
	return numBreaks

def main():
	input = open("input43.txt","r")
	output = open("output43.txt","w")
	
	set = next(input).strip()
	set = set.strip("()")
	#print(set)

	numsStr = set.split(" ")
	numsStr.insert(0,"+" + str(0))
	numsStr.insert(len(numsStr), "+" + str(len(numsStr)))
	#print(numsStr)
	nums = [int(i) for i in numsStr]
	#print(nums)
	
	numBreaks = breakpoint(nums)
	output.write(str(numBreaks))
	
	output.close()
	input.close()

if __name__ == "__main__":
	main()



