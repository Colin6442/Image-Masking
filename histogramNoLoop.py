colorSpace = "hsv"
colorCode = cv2.COLOR_BGR2HSV
undoCode = cv2.COLOR_HSV2BGR

grey = cv2.imread('original.jpg', 0)
color = cv2.imread('original.jpg')
equalize = cv2.cvtColor(color, colorCode)

equalize[:, :, 0] = cv2.equalizeHist(equalize[:, :, 0])
equalize[:, :, 1] = cv2.equalizeHist(equalize[:, :, 1])
equalize[:, :, 2] = cv2.equalizeHist(equalize[:, :, 2])
cv2.imwrite(colorSpace + "_012.jpg", cv2.cvtColor(equalize, undoCode))
equalize = cv2.cvtColor(color, colorCode)

equalize[:, :, 0] = cv2.equalizeHist(equalize[:, :, 0])
cv2.imwrite(colorSpace + "_0.jpg", cv2.cvtColor(equalize, undoCode))
equalize = cv2.cvtColor(color, colorCode)

equalize[:, :, 0] = cv2.equalizeHist(equalize[:, :, 0])
equalize[:, :, 1] = cv2.equalizeHist(equalize[:, :, 1])
cv2.imwrite(colorSpace + "_01.jpg", cv2.cvtColor(equalize, undoCode))
equalize = cv2.cvtColor(color, colorCode)

equalize[:, :, 0] = cv2.equalizeHist(equalize[:, :, 0])
equalize[:, :, 2] = cv2.equalizeHist(equalize[:, :, 2])
cv2.imwrite(colorSpace + "_02.jpg", cv2.cvtColor(equalize, undoCode))
equalize = cv2.cvtColor(color, colorCode)

equalize[:, :, 0] = cv2.equalizeHist(equalize[:, :, 0])
equalize[:, :, 1] = 0
cv2.imwrite(colorSpace + "_0_no1.jpg", cv2.cvtColor(equalize, undoCode))
equalize = cv2.cvtColor(color, colorCode)

equalize[:, :, 0] = cv2.equalizeHist(equalize[:, :, 0])
equalize[:, :, 2] = 0
cv2.imwrite(colorSpace + "_0_no2.jpg", cv2.cvtColor(equalize, undoCode))
equalize = cv2.cvtColor(color, colorCode)

equalize[:, :, 0] = cv2.equalizeHist(equalize[:, :, 0])
equalize[:, :, 1] = 0
equalize[:, :, 2] = 0
cv2.imwrite(colorSpace + "_0_no12.jpg", cv2.cvtColor(equalize, undoCode))
equalize = cv2.cvtColor(color, colorCode)

equalize[:, :, 0] = cv2.equalizeHist(equalize[:, :, 0])
equalize[:, :, 1] = cv2.equalizeHist(equalize[:, :, 1])
equalize[:, :, 2] = 0
cv2.imwrite(colorSpace + "_01_no2.jpg", cv2.cvtColor(equalize, undoCode))
equalize = cv2.cvtColor(color, colorCode)

equalize[:, :, 0] = cv2.equalizeHist(equalize[:, :, 0])
equalize[:, :, 1] = 0
equalize[:, :, 2] = cv2.equalizeHist(equalize[:, :, 2])
cv2.imwrite(colorSpace + "_02_no1.jpg", cv2.cvtColor(equalize, undoCode))
equalize = cv2.cvtColor(color, colorCode)

equalize[:, :, 1] = cv2.equalizeHist(equalize[:, :, 1])
cv2.imwrite(colorSpace + "_1.jpg", cv2.cvtColor(equalize, undoCode))
equalize = cv2.cvtColor(color, colorCode)

equalize[:, :, 1] = cv2.equalizeHist(equalize[:, :, 1])
equalize[:, :, 2] = cv2.equalizeHist(equalize[:, :, 2])
cv2.imwrite(colorSpace + "_12.jpg", cv2.cvtColor(equalize, undoCode))
equalize = cv2.cvtColor(color, colorCode)

equalize[:, :, 0] = 0
equalize[:, :, 1] = cv2.equalizeHist(equalize[:, :, 1])
equalize[:, :, 2] = cv2.equalizeHist(equalize[:, :, 2])
cv2.imwrite(colorSpace + "_12_no0.jpg", cv2.cvtColor(equalize, undoCode))
equalize = cv2.cvtColor(color, colorCode)

equalize[:, :, 0] = 0
equalize[:, :, 1] = cv2.equalizeHist(equalize[:, :, 1])
cv2.imwrite(colorSpace + "_1_no0.jpg", cv2.cvtColor(equalize, undoCode))
equalize = cv2.cvtColor(color, colorCode)

equalize[:, :, 1] = cv2.equalizeHist(equalize[:, :, 1])
equalize[:, :, 2] = 0
cv2.imwrite(colorSpace + "_1_no2.jpg", cv2.cvtColor(equalize, undoCode))
equalize = cv2.cvtColor(color, colorCode)

equalize[:, :, 0] = 0
equalize[:, :, 1] = cv2.equalizeHist(equalize[:, :, 1])
equalize[:, :, 2] = 0
cv2.imwrite(colorSpace + "_1_no02.jpg", cv2.cvtColor(equalize, undoCode))
equalize = cv2.cvtColor(color, colorCode)

equalize[:, :, 2] = cv2.equalizeHist(equalize[:, :, 2])
cv2.imwrite(colorSpace + "_2.jpg", cv2.cvtColor(equalize, undoCode))
equalize = cv2.cvtColor(color, colorCode)

equalize[:, :, 0] = 0
equalize[:, :, 2] = cv2.equalizeHist(equalize[:, :, 2])
cv2.imwrite(colorSpace + "_2_no0.jpg", cv2.cvtColor(equalize, undoCode))
equalize = cv2.cvtColor(color, colorCode)

equalize[:, :, 1] = 0
equalize[:, :, 2] = cv2.equalizeHist(equalize[:, :, 2])
cv2.imwrite(colorSpace + "_2_no1.jpg", cv2.cvtColor(equalize, undoCode))
equalize = cv2.cvtColor(color, colorCode)

equalize[:, :, 0] = 0
equalize[:, :, 1] = 0
equalize[:, :, 2] = cv2.equalizeHist(equalize[:, :, 2])
cv2.imwrite(colorSpace + "_2_no01.jpg", cv2.cvtColor(equalize, undoCode))
equalize = cv2.cvtColor(color, colorCode)