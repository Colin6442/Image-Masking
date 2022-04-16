import cv2, numpy as np, os, math

# angles
angUpper = 360 		# upper bounds of rotation angle
angLower = 0		# lower bounds of rotation angle
angIncrement = 45	# increment of rotation angle
					# same below v
# scale percent width
spwUpper = 151		# set 1 higher to make sure it is included
spwLower = 100
spwIncrement = 50

# scale percent height
sphUpper = 151
sphLower = 100
sphIncrement = 50

# paths
nutsPath = "C:\\Users\\colin\\Desktop\\Sky_BG\\"
outputPath = "C:\\Users\\colin\\Desktop\\transformed\\"
pics = os.listdir(nutsPath)


def rotate(XY, origin, angle):
	x = XY[0] * math.cos(math.radians(angle)) - XY[1] * math.sin(math.radians(angle)) + origin[0] - origin[0] * math.cos(math.radians(angle)) + origin[1] * math.sin(math.radians(angle))
	y = XY[0] * math.sin(math.radians(angle)) + XY[1] * math.cos(math.radians(angle)) + origin[1] - origin[0] * math.sin(math.radians(angle)) - origin[1] * math.cos(math.radians(angle))
	x = round(x)
	y = round(y)
	return [x,y]

def getNumFromAnnotation(annotate):
	index = 2
	prev = 2
	numOut = []

	while index < len(annotate):
		index = annotate.find(' ', index)
		if index == -1:
			numOut.append(float(annotate[prev:]))
			break
		numOut.append(float(annotate[prev:index]))
		prev = index
		index += 1

	return numOut


for pic in pics:
	if pic[-4:] == ".JPG":
		original = cv2.imread(nutsPath + "\\" + pic)
		annotate = open(nutsPath + pic[:-4] + ".txt", "r").read()
		for ang in range(angLower, angUpper, angIncrement):
			for spw in range(spwLower, spwUpper, spwIncrement):
				for sph in range(sphLower, sphUpper, sphIncrement):
					if spw != sph or spw == 100:
						img = original.copy()

						#			TL  ,  TR  ,  BL  ,  BR
						corners = [[0,0], [0,0], [0,0], [0,0]]

						# Set new width
						width = int(img.shape[1] * spw / 100)
						height = int(img.shape[0] * sph / 100)

						# Start with resize


						# Setup annotation array and corners array
						# [originX, originY, width, height]
						annotateNums = getNumFromAnnotation(annotate)
						origin = [(annotateNums[0] * width), (annotateNums[1] * height)]
						corners[0][1] = int(origin[1] - round(annotateNums[2]/2 * width))
						corners[1][1] = int(origin[1] + round(annotateNums[2]/2 * width))
						corners[2][1] = int(origin[1] - round(annotateNums[2]/2 * width))
						corners[3][1] = int(origin[1] + round(annotateNums[2]/2 * width))
						corners[0][0] = int(origin[0] - round(annotateNums[3]/2 * height))
						corners[1][0] = int(origin[0] - round(annotateNums[3]/2 * height))
						corners[2][0] = int(origin[0] + round(annotateNums[3]/2 * height))
						corners[3][0] = int(origin[0] + round(annotateNums[3]/2 * height))
						print(corners)


						# Rotate corners for annotation
						for i, x in enumerate(corners):
							corners[i] = rotate(x, [width/2, height/2], ang)

						# Fix corners to be parallel with respictive axis
						newX = 0
						newY = 0
						for corner in corners:
							if corner[0] > newX:
								newX = corner[0]
							if corner[1] > newY:
								newY = corner[1]

						# Apply corner fixes
						corners[0][0] = int(2*origin[0] - newX)
						corners[1][0] = int(newX)
						corners[2][0] = int(2*origin[0] - newX)
						corners[3][0] = int(newX)

						corners[0][1] = int(newY)
						corners[1][1] = int(newY)
						corners[2][1] = int(2*origin[1] - newY)
						corners[3][1] = int(2*origin[1] - newY)

						# Stretch / Rotate image
						img = cv2.resize(img, (width, height))
						mat = cv2.getRotationMatrix2D((width/2,height/2), ang, 1.0)
						img = cv2.warpAffine(img, mat, (width, height))

						# Write image
						cv2.imwrite(outputPath + pic[:-4] + "_A-" + str(ang) + "_W-" + str(spw) + "_H-" + str(sph) + ".jpg", img)

						# Write annotations
						newAnnotations = ["0 "]
						newAnnotations.append(str(origin[0]/width) + " ")
						newAnnotations.append(str(origin[1]/height) + " ")
						newAnnotations.append(str(2*(newY-origin[1])/height) + " ")
						newAnnotations.append(str(2*(newX-origin[0])/width))

						createAnnotation = open(outputPath + pic[:-4] + "_A-" + str(ang) + "_W-" + str(spw) + "_H-" + str(sph) + ".txt", "w+")
						createAnnotation.write(newAnnotations[0] + newAnnotations[1] + newAnnotations[2] + newAnnotations[3] + newAnnotations[4])
						createAnnotation.close()
						cv2.imshow("something", cv2.resize(img, (width*2, height*2)))
						cv2.waitKey(0)