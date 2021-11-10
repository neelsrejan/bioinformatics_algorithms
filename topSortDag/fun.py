def fun():
	dict = { 1: ['1', '2'], 2: ['2','3']}
	print(dict)
	val = dict[1]
	print(val)
	valNew = [val[-1]]
	print(valNew)
	dict.update({1: valNew})
	print(dict)
	list = [1, 2, 3, 4, 5]
	for i in range(len(list)-1, -1, -1):
		b = list[-1]
		print(b)
		list = list[0:len(list)-1]
	print(list)
fun()
