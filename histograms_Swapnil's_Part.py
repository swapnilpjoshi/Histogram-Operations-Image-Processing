# import cv2, numpy, matplotlib 
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. function to obtain histogram of an image 
def hist_plot_myimg(img): 
	m,n = img.shape 
	# empty list to store the count 
	# of each intensity value 
	count =[] 
	
	# empty list to store intensity 
	# value conda install -c conda-forge opencv
	r = [] 
	
	# loop to traverse each intensity 
	
	for k in range(0, 256): 
		r.append(k) 
		count1 = 0
		
		# loops to traverse each pixel in 
		# the image 
		for i in range(m): 
			for j in range(n): 
				if img[i, j]== k: 
					count1+= 1
		count.append(count1) 
		
	return (r, count) 

def hist_plot_refimg(img): 
	m,n = img.shape 
	# empty list to store the count 
	# of each intensity value 
	countx =[] 
	
	# empty list to store intensity 
	# value conda install -c conda-forge opencv
	r = [] 
	
	# loop to traverse each intensity 
	
	for k in range(0, 256): 
		r.append(k) 
		count2 = 0
		
		# loops to traverse each pixel in 
		# the image 
		for i in range(m): 
			for j in range(n): 
				if img[i, j]== k: 
					count2+= 1
		countx.append(count2) 
		
	return (r, countx) 

# x1= cv2.imread('D:\\GNR Academics\\GNR607 - SIP\\SIP Project\\misc\\7.2.01.tiff', 0)
# myimg = cv2.resize(x1, (15, 20))
# x2 = cv2.imread('D:\\GNR Academics\\GNR607 - SIP\\SIP Project\\reference_image_good.jpeg', 0)
# refimg = cv2.resize(x2, (15, 20))

myimg=cv2.imread('D:\\GNR Academics\\GNR607 - SIP\\SIP Project\\misc\\7.2.01.tiff', 0)
refimg=cv2.imread('D:\\GNR Academics\\GNR607 - SIP\\SIP Project\\reference_image_good.jpeg', 0)

# To ascertain total numbers of rows and 
# columns of the image, size of the image 

r1, count1 = hist_plot_myimg(myimg) 
r2, count2 = hist_plot_refimg(refimg)
# l1,b1 = myimg.shape
l1 = myimg.shape[0]
b1 = myimg.shape[1]
l2,b2 = refimg.shape
type(l1)
cdf = []
refcdf = []
out_freq = []

def cum_freq_myimg(myimg):
	cdf =[]
	cfk=0
	for i in range(0,256):
		cfk = (cfk + count1[i])
		x=cfk/(l1*b1)
		cdf.append(x)
	return(cdf)

def cum_freq_refimg(refimg):
	cdf =[]
	cfx=0
	for i in range(0,256):
		cfx = (cfx + count2[i])
		y=cfx/(l2*b2)
		cdf.append(y)
	return(cdf)

# cummutlative opf input image

cdf = cum_freq_myimg(myimg)
refcdf = cum_freq_refimg(refimg)

# Histogram Specification
outgl = []
for i in range(len(r1)-1):
	if cdf[i]<= refcdf[0]:
		x=0
		outgl.append(x)
#print(outgl)
for i in range(len(r1)-1):
	for a in range(len(r1)):
		if refcdf[i] < cdf[a] <= refcdf[i+1]:
			outgl.append(i+1)

# print(outgl)

# output_image = [ [ 0 for i in range(l1) ] for j in range(b1) ]

# for k in range(0, 256):
# 	for i in range(l1):
# 		for j in range(b1):
# 			if myimg[i,j] == k:
# 				output_image[j][i] = outgl[k]
# 			else: continue

# output_image = [ [ 0 for i in range(l1) ] for j in range(b1) ]

for k in range(0, 256):
	for i in range(l1):
		for j in range(b1):
			if myimg[i,j] == k:
				myimg[i,j] = outgl[k]
			else: continue
print(myimg)
# print(output_image)

cv2.imshow('OutputImage',myimg)
cv2.imshow('RefImage',refimg)

cv2.waitKey(0)
cv2.destroyAllWindows()

# print(outgl)
# print(myimg)
# r3, count3 = hist_plot_myimg(myimg) 
# print(r3,count3)

'''
# plotting the histogram 
plt.stem(r1, count1) 
plt.xlabel('intensity value') 
plt.ylabel('number of pixels') 
plt.title('Histogram of the original image')
plt.show()

plt.stem(r2, count2) 
plt.xlabel('intensity value') 
plt.ylabel('number of pixels') 
plt.title('Histogram of the reference image')
plt.show()

plt.stem(r3, count3) 
plt.xlabel('intensity value') 
plt.ylabel('number of pixels') 
plt.title('Histogram of the output image')
plt.show()
'''