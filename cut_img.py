# coding=utf-8
import cv2
import os
import glob
import numpy as np
import re

def CutImg(imgpath,destpath):
	img = glob.glob(r"/DATACENTER6/ph/traffic_model_faster101/in_pic/29-6-ori/*.jpg")
	img_len= int(len(img))
	#get all the images 
	
	for i in range(img_len):
		temp=img[i].rstrip(".jpg")				# get image name to find its' annotation file.
		
		ori_img = cv2.imread(str(img[i]))
		sp = ori_img.shape						#obtain the image shape
		sz1 = sp[0] 							#height(rows) of image
		sz2 = sp[1] 							#width(colums) of image		

		np.set_printoptions(suppress=True)
		txt = np.loadtxt(str(temp)+".txt")		#load the pic's annotation, which is voc-style.
		if txt.shape[0]==0:						#if the annotation is null, drop it.
			continue
		if np.ndim(txt) == 1:					
			txt = txt.reshape(1, 5)

		txt_len=len(txt)
		# print(txt)
		# print(txt_len)
		for n in range(txt_len):				#get every object's coordinates in this image
			x1=txt[n][0]
			y1=txt[n][1]
			x2=txt[n][2]
			y2=txt[n][3]
			a=int(x1) # x start
			b=int(x2) # x end
			c=int(y1) # y start
			d=int(y2) # y end
			#print(a,b,c,d)
			res = ori_img[c:d,a:b]				#use opencv's function to cut the image.
			cv2.imwrite("/DATACENTER6/ph/traffic_model_faster101/in_pic/29-6-cut/"+str(i) +str(n)+ '-29-6.jpg',res) 


if __name__ == '__main__':
	imgpath ='./28-4' # source images
	txtpath ='./28-4-1'	
	destpath='./28-4-cut' # resized images saved here
	CutImg(imgpath,destpath)
