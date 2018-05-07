def defaultMask():
	print('Using deafault filter that does nothing.')
	maskSize = 3
	Mask = [[0 for x in range(maskSize)] for y in range(maskSize)]
	Mask[1][1] = 1
	return Mask, maskSize
def checkFilterFile(matrix):
	size = len(matrix[0])
	if size % 2 is not 1 or size is 1:
		return False
	for line in matrix:
		if len(line) is not size:
			return False
		if len(matrix) is not size:
			return False
	return True
def maskChooser(filename):
	try:
		f = open('Filters/'+filename, 'r')
		Mask = [[int(num) for num in line.split(' ')] for line in f]
		if not checkFilterFile(Mask):
			print('Given filter file doesn\'t have correct format. It should be NxN, where N is odd and greater than 1')
			Mask, maskSize = defaultMask()
		else:	
			maskSize = len(Mask) #nn
		f.close()
	except:
		print('Couldn\'t open filter file properly. Check if it exist in directory \"Filters\"...')	
		Mask, maskSize = defaultMask()

	maskWeight = 0
	for i in range(maskSize):
		for j in range(maskSize):
			maskWeight += Mask[i][j]
	maskWeight = 1 if maskWeight is 0 else maskWeight
	return Mask, maskWeight, maskSize
