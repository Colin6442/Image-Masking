import cv2, numpy as np
from matplotlib import pyplot as plt
#from sklearn.cluster import KMeans

# pic = plt.imread('img1.jpg')/255
# pic_n = pic.reshape(pic.shape[0]*pic.shape[1], pic.shape[2])
# kmeans = KMeans(n_clusters=5, random_state=0).fit(pic_n)
# pic2show = kmeans.cluster_centers_[kmeans.labels_]
# cluster_pic = pic2show.reshape(pic.shape[0], pic.shape[1], pic.shape[2])
# plt.imshow(cluster_pic)
# plt.imsave("filter.jpg", cluster_pic)

grey = cv2.imread('img3.jpg', 0)
color = cv2.imread('img3.jpg')
ycrcb = cv2.imread('img3.jpg')
equalize = cv2.cvtColor(color, cv2.COLOR_BGR2YCrCb)

for x in range(3):
    equalize[:, :, 0] = 0
    equalize[:, :, 1] = 0
    equalize[:, :, 2] = cv2.equalizeHist(equalize[:, :, 2])
    cv2.imwrite("hsv_"+ x +"_no12.jpg", equalize)

# clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
# imgClahe = clahe.apply(grey)
# # cv.imwrite('clahe_2.jpg', imgClahe)

# lab = cv2.cvtColor(color, cv2.COLOR_BGR2LAB)

# l, a, b = cv2.split(lab)
# clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
# cl = clahe.apply(l)

# limg = cv2.merge((cl,a,b))

# final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
# final = cv2.cvtColor(final, cv2.COLOR_BGR2GRAY)
# #cv2.imwrite('img0.jpg', final)

# constant = 6
# pixSize = 899

# thresh1 = cv2.adaptiveThreshold(grey, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, pixSize, constant)
# # thresh2 = cv2.adaptiveThreshold(grey, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, pixSize, constant)
# thresh3 = cv2.adaptiveThreshold(ycrcb, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, pixSize, constant)
# # thresh4 = cv2.adaptiveThreshold(ycrcb, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, pixSize, constant)

# out1 = cv2.bitwise_and(color, color, mask= 255 - thresh1)
# # out2 = cv2.bitwise_and(color, color, mask= 255 - thresh2)
# out3 = cv2.bitwise_and(color, color, mask= thresh3)
# # out4 = cv2.bitwise_and(color, color, mask= 255 - thresh4)

# cv2.imwrite("mean.png", out1)
# # cv2.imwrite("gaus.png", out2)
# cv2.imwrite("mean2.png", out3)
# # cv2.imwrite("gaus2.png", out4)

# ycrcb = cv2.cvtColor(ycrcb, cv2.COLOR_BGR2YCrCb)
# ycrcb[:, :, 0] = cv2.equalizeHist(ycrcb[:, :, 0])
# # ycrcsb[:, :, 1] = cv2.equalizeHist(ycrcb[:, :, 1])
# ycrcb[:, :, 2] = cv2.equalizeHist(ycrcb[:, :, 2])
# lower = np.array([0, 0, 100])
# upper = np.array([120, 255, 255])
# mask = cv2.inRange(ycrcb, lower, upper)
# out2 = cv2.bitwise_and(color, color, mask= mask)
# cv2.imwrite("mask.jpg", mask)
# cv2.imwrite("masked.jpg", out2)

# scale_percent = 25
# width = int(grey.shape[1] * scale_percent / 100)
# height = int(grey.shape[0] * scale_percent / 100)
# dim = (width, height)



# params = cv2.SimpleBlobDetector_Params()

# # Filter by how oval shapped it can be
# params.filterByInertia = True
# params.minInertiaRatio = 0.1    # >= 0
# params.maxInertiaRatio = 1.0    # <= 1

# # Filter by Area.
# params.filterByArea = True
# params.minArea = 20            # >= 0
# params.maxArea= 5000             # big number

# # Filter by Circularity
# params.filterByCircularity = True
# params.minCircularity = 0.5     # >= 0
# params.maxCircularity = 1.0     # <= 1

# # Filter by Convexity
# params.filterByConvexity = True
# params.minConvexity = 0.6       # >= 0
# params.maxConvexity = 1.0       # <= 1

# # Apply parameters
# detector = cv2.SimpleBlobDetector_create(params)
# # Apply detection to mask

# keypoints = detector.detect(mask)

# # Draw detected blobs as red circles.
# im_with_keypoints = cv2.drawKeypoints(ycrcb, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# mask_with_keypoints = cv2.drawKeypoints(mask, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


# mask_with_keypoints = cv2.resize(mask_with_keypoints, dim)
# cv2.imshow("detection", mask_with_keypoints)

# # thresh1 = cv2.resize(thresh1, dim)
# # thresh2 = cv2.resize(thresh2, dim)
# mask = cv2.resize(mask, dim)
# out2 = cv2.resize(out2, dim)



# # cv2.imshow('Adaptive Mean', thresh1)
# # cv2.imshow('Adaptive Gaussian', thresh2)
# cv2.imshow("mask", mask)
# cv2.imshow("masked", out2)

# b = cv2.calcHist([grey], [0], None, [256], [0,256])
# g = cv2.calcHist([grey], [1], None, [256], [0,256])
# r = cv2.calcHist([grey], [2], None, [256], [0,256])

# plt.plot(b)
# plt.plot(g)
# plt.plot(r)
# plt.show()

cv2.waitKey(0)