import cv2, numpy as np, os

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



for pic in pics:
    if pic[-4:] == ".JPG":
        original = cv2.imread(nutsPath + "\\" + pic)
        for ang in range(angLower, angUpper, angIncrement):
            for spw in range(spwLower, spwUpper, spwIncrement):
                for sph in range(sphLower, sphUpper, sphIncrement):
                    if spw != sph or spw == 100:
                        img = original.copy()
                        
                        width = int(img.shape[1] * spw / 100)
                        height = int(img.shape[0] * sph / 100)
                        
                        img = cv2.resize(img, (width, height))
                        mat = cv2.getRotationMatrix2D((width/2,height/2), ang, 1.0)
                        img = cv2.warpAffine(img, mat, (width, height))

                        print("C:\\Users\\colin\\Desktop\\transformed\\" + pic[:-4] + "_A-" + str(ang) + "_W-" + str(spw) + "_H-" + str(sph) + ".jpg")
                        cv2.imwrite("C:\\Users\\colin\\Desktop\\transformed\\" + pic[:-4] + "_A-" + str(ang) + "_W-" + str(spw) + "_H-" + str(sph) + ".jpg", img)
        