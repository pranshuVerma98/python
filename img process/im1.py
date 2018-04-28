import cv2
import glob

image=glob.glob("*.jpg")
for im in image:
	img=cv2.imread(im,0)
	'''print(img)
	print(img.shape)
	print(img.ndim)
	'''
	resize_image=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
	cv2.imshow("cute",resize_image)
	cv2.imwrite("2"+im,resize_image)
	cv2.waitKey(0)    #0 means by click or 2000 means it will close in 2 sec 
	cv2.destroyAllWindows()