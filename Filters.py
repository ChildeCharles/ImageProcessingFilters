# -*- coding: utf-8 -*-
from PIL import Image
import argparse, sys, re


def maskChooser(maskSize, chosenFilter):#PROBABLY REWRITE
	diff = (maskSize-1)/2
	if chosenFilter == 1:
		Mask = [[1 for x in range(maskSize)] for y in range(maskSize)]
		maskWeight = maskSize*maskSize
	elif chosenFilter == 2:
		Mask = [[0 for x in range(maskSize)] for y in range(maskSize)] 
		Mask[1][1] = 4
		Mask[0][1] = -1
		Mask[1][0] = -1
		Mask[2][1] = -1
		Mask[1][2] = -1
		maskWeight = 1
	return Mask, maskWeight
def takeSurroundings(PixelMatrix, Coordinates, maskSize):
	Matrix = [[0 for x in range(maskSize)] for y in range(maskSize)]
	x,y = Coordinates
	diff = int((maskSize-1)/2)
	for i in range(maskSize):
		for j in range(maskSize):
			try:
				Matrix[i][j] = PixelMatrix[i+x-diff, j+y-diff]
			except:
				Matrix[i][j] = (0,0,0) #Out of bounds ;(		
	return Matrix
def countValue(Matrix, Mask, maskSize, maskWeight):
	value = (0,0,0)
	for i in range(maskSize):
		for j in range(maskSize):
			RGB = (x*Mask[i][j] for x in Matrix[i][j]) #Could be 1 liner, but clarity...
			value = tuple(map(lambda x, y: x + y, value, RGB))
	value = tuple(map(lambda x: int(x/(maskWeight)), value))
	return value

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Basic Filters for Image Processing.')
	parser.add_argument('-m', '--maskSize', type=int,  help='Select mask size for current filter. It must be divisible by 2.')
	parser.add_argument('-f', '--filter', type=int, help='Select filter type') #Probably merge these 2
	parser.add_argument('-i', '--imageFile', help='Select image file to process')
	parser.add_argument('-n', '--noshow', action='store_true', help='Don\'t open processed and original image')
	parser.add_argument('-s', '--save', help='Save processed photo to specified filename ')
	args = parser.parse_args()
	if args.maskSize is None or args.maskSize > 9:
		print("Wrong mask or no mask was chosen. Setting default mask...")
		args.maskSize = 3
	if args.filter is None or args.filter > 10:
		print("Wrong filter or no filter was chosen. Setting default filter...")
		args.filter = 1
	try:
		image = Image.open(args.imageFile)
	except:
		print("Cannot open file or file not specified. Opening default - Lenna.png...")
		try:
			image = Image.open("Lenna.png")
		except:
			print("Cannot open default image - Lenna.png. Check if this file is in your directory. If it isn\'t - add it. Otherwise cry...")
			sys.exit(0)
	if image.mode != 'RGB':
		print("Given file isn\'t in RGB... Choose another file.")
		sys.exit(0)
	#Arguments parsed, file opened...
	imageWidth, imageHeight = image.size
	newImage = [[0 for x in range(imageWidth)] for y in range(imageHeight)]
	px = image.load() #pixels
	mask, maskWeight = maskChooser(args.maskSize,args.filter)
	for i in range(imageWidth):
		for j in range(imageHeight):
			Matrix = takeSurroundings(px, (i,j), args.maskSize)
			#px[i,j] = countValue(Matrix, mask, args.maskSize) INTERESTING RESULTS...
			newImage[i][j] = countValue(Matrix, mask, args.maskSize, maskWeight)
	#rewriting image
	for i in range(imageWidth):
		for j in range(imageHeight):
			px[i,j] = newImage[i][j]
	if args.save is not None:
		if not (re.match('.*[.](png|jpg|bmp)', args.save)):
			args.save+=".jpg"
		image.save(args.save)
		print("Processed image saved to file: ", args.save)
	if not args.noshow:
		image.show()
		image = Image.open("Lenna.png")
		image.show()

