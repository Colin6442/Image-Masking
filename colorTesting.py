import cv2, numpy as np, os

def resize(img, dim):
    return(cv2.resize(img, dim, interpolation=cv2.INTER_AREA))

# grey = cv2.imread("lab_01.jpg", 0)
# color = cv2.imread("lab_01.jpg")

# clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
# imgClahe = clahe.apply(grey)

# constant = 26
# pixSize = 299

# thresh1 = cv2.adaptiveThreshold(grey, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, pixSize, constant)
# # thresh2 = cv2.adaptiveThreshold(grey, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, pixSize, constant)
# # thresh3 = cv2.adaptiveThreshold(ycrcb, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, pixSize, constant)
# # thresh4 = cv2.adaptiveThreshold(ycrcb, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, pixSize, constant)

# out1 = cv2.bitwise_and(color, color, mask= 255 - thresh1)
# # out2 = cv2.bitwise_and(color, color, mask= 255 - thresh2)
# # out3 = cv2.bitwise_and(color, color, mask= thresh3)
# # out4 = cv2.bitwise_and(color, color, mask= 255 - thresh4)

# cv2.imwrite("mean.png", out1)
# # cv2.imwrite("gaus.png", out2)
# # cv2.imwrite("mean2.png", out3)
# # cv2.imwrite("gaus2.png", out4)


nutsPath = "C:\\Users\\colin\\Desktop\\MommyNuts"
pics = os.listdir(nutsPath)

for pic in pics:
    pic = "IMG_4624.JPG"
    img = cv2.imread(nutsPath + "\\" + pic)
    # img = cv2.GaussianBlur(img,(25,25),cv2.BORDER_DEFAULT)
    # Rectangular Kernel
    
    kernel = np.ones((2,2),np.uint8)
    noChange = img.copy()

    scale_percent = 25
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    down = (width, height)
    
    img = cv2.resize(img, down)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    img[:, :, 0] = cv2.equalizeHist(img[:, :, 0])
    img[:, :, 1] = cv2.equalizeHist(img[:, :, 1])
    img = cv2.cvtColor(img, cv2.COLOR_LAB2BGR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    noSky = cv2.cvtColor(cv2.resize(noChange.copy(), down), cv2.COLOR_BGR2HSV)
    lower = np.array([0, 0, 170])
    upper = np.array([180, 255, 255])
    noSky = cv2.inRange(noSky, lower, upper)

    lower = np.array([35, 110, 40])
    upper = np.array([90, 255, 255])
    noGrass = cv2.inRange(img, lower, upper)

    mask = cv2.bitwise_and(255-noGrass, 255-noGrass, mask=255-noSky)
    mask = cv2.bitwise_or(mask, mask, mask= 255-noGrass)

    small = resize(noChange.copy(), down)
    cv2.imshow("test", cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel))
    cv2.waitKey(0)
    break
    continue

    # cv2.imshow("noSky mask", 255-noSky)
    # cv2.imshow("noGrass mask", 255-noGrass)

    params = cv2.SimpleBlobDetector_Params()

    # Filter by how oval shapped it can be
    params.filterByInertia = True
    params.minInertiaRatio = 0.1    # >= 0
    params.maxInertiaRatio = 1.0    # <= 1

    # Filter by Area.
    params.filterByArea = True
    params.minArea = 20            # >= 0
    params.maxArea= 5000             # big number

    # Filter by Circularity
    params.filterByCircularity = True
    params.minCircularity = 0.5     # >= 0
    params.maxCircularity = 1.0     # <= 1

    # Filter by Convexity
    params.filterByConvexity = True
    params.minConvexity = 0.6       # >= 0
    params.maxConvexity = 1.0       # <= 1

    # Apply parameters
    detector = cv2.SimpleBlobDetector_create(params)

    # Apply detection to mask
    keypoints = detector.detect(255-mask)

    img = noChange.copy()
    img = resize(img, down)

    small = cv2.drawKeypoints(img, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    cv2.imwrite("C:\\Users\\colin\\Desktop\\Image-Masking-using-HSV-values\\detection_small\\" + pic, small)

    img = noChange.copy()

    for point in keypoints:
        point.pt = (point.pt[0] * 4, point.pt[1] * 4)
        point.size *= 4

    # Draw detected blobs as blue circles.
    large = cv2.drawKeypoints(img, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    cv2.imwrite("C:\\Users\\colin\\Desktop\\Image-Masking-using-HSV-values\\detection_large\\" + pic, large)
    cv2.waitKey(0)
    print("wrote " + pic)

    # mask_with_keypoints = cv2.drawKeypoints(out1, keypoints, np.array([]), (255, 0, 0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


# mask_with_keypoints = cv2.resize(mask_with_keypoints, dim)
# cv2.imshow("mask", mask_with_keypoints)
# im_with_keypoints = cv2.resize(im_with_keypoints, dim)
# cv2.imshow("detection", im_with_keypoints)

# thresh1 = cv2.resize(thresh1, dim)
# thresh2 = cv2.resize(thresh2, dim)
# mask = cv2.resize(mask, dim)
# out2 = cv2.resize(out2, dim)


# cv2.waitKey(0)