import cv2, numpy as np

def resize(img, dim):
    return(cv2.resize(img, dim, interpolation=cv2.INTER_AREA))

def runImage(varIn):
    flip = varIn[0]
    min_H = varIn[1]
    min_S = varIn[2]
    min_V = varIn[3]
    max_H = varIn[4]
    max_S = varIn[5]
    max_V = varIn[6]
    img_path = varIn[7]

    # CV2 uses bgr instead of rgb
    frame = cv2.imread(img_path)

    # Change if image is too small/big (100 for no change)
    scale_percent = 20

    # Print color at this point
    printColor = False
    x = 377
    y = 1915

    # Resize if needed
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)

    frame = resize(frame, dim)

    # Convert BGR to     H     S      V
    # range =         0/180; 0/255; 0/255
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Print color at point
    if printColor:
        x = int(x * scale_percent / 100)
        y = int(y * scale_percent / 100)
        print(hsv[y, x])

    # Define range of color in HSV
    lower = np.array([int(min_H),int(min_S),int(min_V)])
    upper = np.array([int(max_H),int(max_S),int(max_V)])

    # Create mask
    mask = cv2.inRange(hsv, lower, upper)
    if flip=="normal":
        mask = cv2.inRange(hsv, lower, upper)
    elif flip=="flip":
        mask = 255-mask

    # Apply mask to original image
    res = cv2.bitwise_and(frame,frame, mask= 255-mask)

    # Detection
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

    # Draw detected blobs as red circles.
    im_with_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    mask_with_keypoints = cv2.drawKeypoints(mask, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow('Detection', im_with_keypoints)
    cv2.imshow('Original', frame)
    cv2.imshow('With Mask', res)
    cv2.imshow('Mask Detect', mask_with_keypoints)

# Tkinter documentation
# http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html
# https://web.archive.org/web/20190427180831/http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html

# nuts |
# hsv  V
# 25/150; 0/255; 0/255  (block hue)
# 0/180; 0/60; 0/150    (block high sat & val)


