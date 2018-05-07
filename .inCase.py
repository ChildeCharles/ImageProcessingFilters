def maskChooser(chosenFilter):
	#low-pass filters
	if chosenFilter is '1' or chosenFilter is 'mean':
		maskSize = 3
		Mask = [[1 for x in range(maskSize)] for y in range(maskSize)]
	elif chosenFilter is '2' or chosenFilter is 'square':
		maskSize = 5
		Mask = [[1 for x in range(maskSize)] for y in range(maskSize)]
	elif chosenFilter is '3' or chosenFilter is 'round':
		maskSize = 5
		Mask = [[1 for x in range(maskSize)] for y in range(maskSize)]
		Mask[0][0] = 0; Mask[4][0] = 0; Mask[0][4] = 0; Mask[4][4] = 0
	elif chosenFilter is '4' or chosenFilter is 'lp1':
		maskSize = 3
		Mask = [[1 for x in range(maskSize)] for y in range(maskSize)]
		Mask[1][1] = 2
	elif chosenFilter is '5' or chosenFilter is 'lp2':
		Mask = [[1 for x in range(maskSize)] for y in range(maskSize)]
		Mask[1][1] = 4
	elif chosenFilter is '6' or chosenFilter is 'lp3':
		maskSize = 3
		Mask = [[1 for x in range(maskSize)] for y in range(maskSize)]
		Mask[1][1] = 12
	#high-pass filters
	elif chosenFilter is '7' or chosenFilter is 'rmmean':
		maskSize = 3
		Mask = [[-1 for x in range(maskSize)] for y in range(maskSize)]
		Mask[1][1] = 9
	elif chosenFilter is '8' or chosenFilter is 'hp1':
		maskSize = 3
		Mask = [[-1 for x in range(maskSize)] for y in range(maskSize)]
		Mask[0][0] = 0; Mask[2][0] = 0; Mask[0][2] = 0; Mask[2][2] = 0
		Mask[1][1] = 5
	elif chosenFilter is '9' or chosenFilter is 'hp2':
		maskSize = 3
		Mask = [[-2 for x in range(maskSize)] for y in range(maskSize)]
		Mask[0][0] = 1; Mask[2][0] = 1; Mask[0][2] = 1; Mask[2][2] = 1
		Mask[1][1] = 5
	elif chosenFilter is '10' or chosenFilter is 'hp3':
		maskSize = 3
		Mask = [[-1 for x in range(maskSize)] for y in range(maskSize)]
		Mask[0][0] = 0; Mask[2][0] = 0; Mask[0][2] = 0; Mask[2][2] = 0
		Mask[1][1] = 20
	#move filters
	elif chosenFilter is '11' or chosenFilter is 'horizontal':
		maskSize = 3
		Mask = [[0 for x in range(maskSize)] for y in range(maskSize)]
		Mask[0][1] = -1
		Mask[1][1] = 1
	elif chosenFilter is '12' or chosenFilter is 'vertical':
		maskSize = 3
		Mask = [[0 for x in range(maskSize)] for y in range(maskSize)]
		Mask[1][0] = -1
		Mask[1][1] = 1
	#gradient direction filters
	elif chosenFilter is '13' or chosenFilter is 'north':
		maskSize = 3
		Mask = [[1 for x in range(maskSize)] for y in range(maskSize)]
		Mask[2][0] = -1; Mask[2][1] = -1; Mask[2][2] = -1
		Mask[1][1] = -2
	elif chosenFilter is '14' or chosenFilter is 'south':
		maskSize = 3
		Mask = [[1 for x in range(maskSize)] for y in range(maskSize)]
		Mask[0][0] = -1; Mask[0][1] = -1; Mask[0][2] = -1
		Mask[1][1] = -2
	elif chosenFilter is '15' or chosenFilter is 'east':
		maskSize = 3
		Mask = [[1 for x in range(maskSize)] for y in range(maskSize)]
		Mask[0][0] = -1; Mask[1][0] = -1; Mask[2][0] = -1
		Mask[1][1] = -2
	elif chosenFilter is '16' or chosenFilter is 'west':
		maskSize = 3
		Mask = [[1 for x in range(maskSize)] for y in range(maskSize)]
		Mask[0][2] = -1; Mask[1][2] = -1; Mask[2][2] = -1
		Mask[1][1] = -2
	#Laplace filters
	elif chosenFilter is '17' or chosenFilter is 'lapl1':
		maskSize = 3
		Mask = [[0 for x in range(maskSize)] for y in range(maskSize)]
		Mask[1][1] = 4
		Mask[0][1] = -1; Mask[1][0] = -1; Mask[2][1] = -1; Mask[1][2] = -1
	elif chosenFilter is '18' or chosenFilter is 'lapl2':
		maskSize = 3
		Mask = [[-1 for x in range(maskSize)] for y in range(maskSize)]
		Mask[1][1] = 8
	elif chosenFilter is '19' or chosenFilter is 'lapl3':
		maskSize = 3
		Mask = [[1 for x in range(maskSize)] for y in range(maskSize)]
		Mask[1][1] = 4
		Mask[0][1] = -2; Mask[1][0] = -2; Mask[2][1] = -2; Mask[1][2] = -2
	#Do nothing filter
	else:
		maskSize = 3
		Mask = [[0 for x in range(maskSize)] for y in range(maskSize)]
		Mask[1][1] = 1
	maskWeight = 0
	for i in range(maskSize):
		for j in range(maskSize):
			maskWeight += Mask[i][j]
	maskWeight = 1 if maskWeight is 0 else maskWeight
	return Mask, maskWeight, maskSize

