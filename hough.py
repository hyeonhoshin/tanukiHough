import cv2
import numpy as np
import argparse

# Terminal data parsing
parser = argparse.ArgumentParser(description='Hough transform an image')
parser.add_argument('-i',default='stuff.jpg', type=str ,help='The path of file to transform')
args = parser.parse_args()

# Image read
img = cv2.imread(args.i)
img_original = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,30,100,apertureSize=3)

cv2.imshow('Cannied',edges)


# Extract Lines and Circles
lines = cv2.HoughLinesP(edges,1,np.pi/180,60,minLineLength=15,maxLineGap=15)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20,param1=60,param2=30,minRadius=0, maxRadius=100)

# Draw Lines and Circles
for i in range(len(lines)):
    for x1,y1,x2,y2 in lines[i]:
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),3)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

res = np.vstack((img_original,img))
cv2.imwrite('output.png', img)
cv2.imshow('Original img vs Transformed img',res)
cv2.waitKey(0)
cv2.destroyAllWindows()