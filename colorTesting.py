import cv2, numpy as np, os

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
    img = cv2.imread(nutsPath + "\\" + pic)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    img[:, :, 0] = cv2.equalizeHist(img[:, :, 0])
    img[:, :, 1] = cv2.equalizeHist(img[:, :, 1])
    img = cv2.cvtColor(cv2.cvtColor(img, cv2.COLOR_LAB2BGR), cv2.COLOR_BGR2HSV)


    scale_percent = 25
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    down = (width, height)

    img = cv2.resize(img, down)
    
    cv2.imshow("t", img)
    cv2.waitKey(0)
    break

    lower = np.array([30, 100, 0])
    upper = np.array([90, 255, 255])

    mask = cv2.inRange(img, lower, upper)

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
    keypoints = detector.detect(mask)

    small = cv2.drawKeypoints(img, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    cv2.imwrite("s" + pic, small)

    img = cv2.imread(nutsPath + "\\" + pic)
    
    for point in keypoints:
        point.pt = (point.pt[0] * 4, point.pt[1] * 4)
        point.size *= 4

    # Draw detected blobs as blue circles.
    big = cv2.drawKeypoints(img, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    cv2.imwrite("b" + pic, big)
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