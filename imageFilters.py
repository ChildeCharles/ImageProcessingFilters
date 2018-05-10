# -*- coding: utf-8 -*-
from PIL import Image
import argparse, sys, re
import maskReader

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
			RGB = (x*Mask[i][j] for x in Matrix[i][j]) #nn - 2 lines.
			value = tuple(map(lambda x, y: x + y, value, RGB))
	value = tuple(map(lambda x: int(x/(maskWeight)), value))
	return value

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Basic Filters for Image Processing.')
	parser.add_argument('-f', '--filter', help='Select filter from filters existing in directory \"Filters\". For more information about filters and what they do - read \"filters.txt\"')
	parser.add_argument('-i', '--imageFile', help='Select image file to process by specifying filename')
	parser.add_argument('-n', '--noshow', action='store_true', help='Don\'t open processed and original image')
	parser.add_argument('-s', '--save', help='Save processed photo to specified filename ')
	args = parser.parse_args()
	if args.filter is None:
		print("Wrong filter or no filter was chosen. Setting default filter that does nothing...")
		args.filter = 'nothing'
	try:
		image = Image.open(args.imageFile)
	except:
		print("Cannot open image file or file not specified. Opening default - \"Lenna.png\"...")
		try:
			args.imageFile = "Lenna.png"
			image = Image.open(args.imageFile)
		except:
			print("Cannot open default image - \"Lenna.png\". Check if this file is in your directory. If it isn\'t - add it. Otherwise cry...")
			sys.exit(0)
	if image.mode != 'RGB':
		print("Given file isn\'t in RGB... Choose another file.")
		sys.exit(0)
	#Arguments parsed, file opened...
	imageWidth, imageHeight = image.size
	newImage = [[0 for x in range(imageWidth)] for y in range(imageHeight)]
	px = image.load() #pixels
	mask, maskWeight, maskSize = maskReader.maskChooser(args.filter) #Getting mask
	for i in range(imageWidth):
		for j in range(imageHeight):
			Matrix = takeSurroundings(px, (i,j), maskSize)
			#px[i,j] = countValue(Matrix, mask, maskSize) INTERESTING RESULTS...
			newImage[i][j] = countValue(Matrix, mask, maskSize, maskWeight)
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
		image = Image.open(args.imageFile)
		image.show()
	sys.exit(0)
