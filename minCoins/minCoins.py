def minCoins(price, coins):

	coins.sort()
	inf = float("inf")
	dpArr = [inf] * int(int(price)+1)
		

	#There are 0 coins needed to make 0 coins
	dpArr[0] = 0	
	for i in coins:
		for j in range(1,int(price)+1):
			if j-i < 0:
				continue
			else:
				dpArr[j] = min(dpArr[j-i]+1,dpArr[j])				
	return dpArr[int(price)]

input = open("input71.txt","r")
output = open("output71.txt","w")

price = next(input)
price = price.strip()

for line in input:
	line = line.strip()
	coinStr = line.split(",")

coins = [int(i) for i in coinStr]

minCoinsNeeded = minCoins(price, coins)

output.write(str(minCoinsNeeded))

input.close()
output.close()

