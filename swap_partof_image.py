import cv2
import matplotlib.pyplot as plt
first=cv2.imread('image_name1.jpg')

cv2.imshow('hi',first)
cv2.waitKey()
cv2.destroyAllWindows()

plt.imshow(first)
#here y1,y2 are columns and x1 and x2 are rows that we want to crop from image first
cfirst=first[y1:y2,x1:x2]
plt.imshow(cfirst)

second=cv2.imread('backg.jpg')
cv2.imshow('hi',second)
cv2.waitKey()
cv2.destroyAllWindows()

plt.imshow(second)
#here a1,a2 are columns and b1,b2 are rows that we want to crop from image first
csecond=second[a1:a2,b1:b2]
plt.imshow(csecond)

copy_first=first.copy()
copy_second=second.copy()

copy_second[a1:a1+cfirst.shape[0],b1:b1+cfirst.shape[1]]=cfirst

cv2.imshow('hi',copy_second)
cv2.waitKey()
cv2.destroyAllWindows()

copy_first[y1:y1+csecond.shape[0],x1:x1+csecond.shape[1]]=csecond

cv2.imshow('hi',copy_first)
cv2.waitKey()
cv2.destroyAllWindows()
