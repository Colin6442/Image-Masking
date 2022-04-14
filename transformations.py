import cv2, numpy as np, os, math

# Rotation - A&B: point - X&Y: origin
# x = A*cos(a) - B*sin(a) + X - X*cos(a) + Y*sin(a)
# y = A*sin(a) + B*cos(a) + Y - X*sin(a) - Y*cos(a)

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


# angles
angUpper = 360
angLower = 0
angIncrement = 90

# scale percent width
spwUpper = 151
spwLower = 100
spwIncrement = 50

# scale percent height
sphUpper = 151
sphLower = 100
sphIncrement = 50

# paths
nutsPath = "C:\\Users\\colin\\Desktop\\Sky_BG\\"
pics = os.listdir(nutsPath)


#			TL  ,  TR  ,  BL  ,  BR
corners = [[0,0], [0,0], [0,0], [0,0]]

pic = cv2.imread(nutsPath + "IMG_10.JPG")
annotate = open(nutsPath + "IMG_10.txt", "r").read()

# [originX, originY, width, height]
annotateNums = getNumFromAnnotation(annotate)

origin = [(annotateNums[0] * pic.shape[1]), (annotateNums[1] * pic.shape[0])]


corners[0][1] = int(origin[1] - round(annotateNums[2]/2 * pic.shape[1]))
corners[1][1] = int(origin[1] + round(annotateNums[2]/2 * pic.shape[1]))
corners[2][1] = int(origin[1] - round(annotateNums[2]/2 * pic.shape[1]))
corners[3][1] = int(origin[1] + round(annotateNums[2]/2 * pic.shape[1]))

corners[0][0] = int(origin[0] - round(annotateNums[3]/2 * pic.shape[0]))
corners[1][0] = int(origin[0] - round(annotateNums[3]/2 * pic.shape[0]))
corners[2][0] = int(origin[0] + round(annotateNums[3]/2 * pic.shape[0]))
corners[3][0] = int(origin[0] + round(annotateNums[3]/2 * pic.shape[0]))

print(corners)

for i, x in enumerate(corners):
	corners[i] = rotate(x, [pic.shape[1]/2, pic.shape[0]/2], 60)


# cv2.imshow("corners", cv2.resize(pic, (800,800)))
# cv2.waitKey(0)

# for x in corners:
# 	pic[x[0], x[1]] = [255,0,255]

# cv2.imshow("corners", cv2.resize(pic, (800,800)))
# cv2.waitKey(0)

newX = 0
newY = 0
for corner in corners:
	if corner[0] > newX:
		newX = corner[0]
	if corner[1] > newY:
		newY = corner[1]

corners[0][0] = int(2*origin[0] - newX)
corners[1][0] = int(newX)
corners[2][0] = int(2*origin[0] - newX)
corners[3][0] = int(newX)

corners[0][1] = int(newY)
corners[1][1] = int(newY)
corners[2][1] = int(2*origin[1] - newY)
corners[3][1] = int(2*origin[1] - newY)


mat = cv2.getRotationMatrix2D((200/2,200/2), 60, 1.0)
img = cv2.warpAffine(pic, mat, (200, 200))

for x in corners:
	img[x[0], x[1]] = [255,0,0]

cv2.imshow("corners", cv2.resize(img, (800,800)))
cv2.waitKey(0)

newAnnotations = []

# for pic in pics:
	# if pic[-4:] == ".JPG":
	# 	original = cv2.imread(nutsPath + "\\" + pic)
	# 	for ang in range(angLower, angUpper, angIncrement):
	# 		for spw in range(spwLower, spwUpper, spwIncrement):
	# 			for sph in range(sphLower, sphUpper, sphIncrement):
	# 				if spw != sph or spw == 100:
	# 					img = original.copy()
				


	# 					width = int(img.shape[1] * spw / 100)
	# 					height = int(img.shape[0] * sph / 100)
				


	# 					img = cv2.resize(img, (width, height))
	# 					mat = cv2.getRotationMatrix2D((width/2,height/2), ang, 1.0)
	# 					img = cv2.warpAffine(img, mat, (width, height))

	# 					print("C:\\Users\\colin\\Desktop\\transformed\\" + pic[:-4] + "_A-" + str(ang) + "_W-" + str(spw) + "_H-" + str(sph) + ".jpg")
	# 					cv2.imwrite("C:\\Users\\colin\\Desktop\\transformed\\" + pic[:-4] + "_A-" + str(ang) + "_W-" + str(spw) + "_H-" + str(sph) + ".jpg", img)
        