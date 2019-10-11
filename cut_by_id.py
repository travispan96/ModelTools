import os
import cv2
import glob

def del_xml():
	xml=glob.glob(r"/DATACENTER6/ph/traffic_model_faster101/in_pic/29-6-ori/*.xml")
	xml_len=int(len(xml))
	count=1
	for i in range(xml_len):
		fp1=open(xml[i])
		#fp2=open(xml[i+1])

		temp1=xml[i].rstrip(".xml")
		#temp2=xml[i+1].rstrip(".xml")
		img_path1=str(temp1+".jpg")
		#img_path2=str(temp2+".jpg")
		ori_img1=cv2.imread(img_path1)
		#ori_img2=cv2.imread(img_path2)
		for n in fp1:
			if '<object>' in n:
				try:
					ob_name=next(fp1).split('>')[1].split('<')[0]
				except StopIteration: 
					pass
			if '<bndbox>' in n:
				try:
					xmin=next(fp1).split('>')[1].split('<')[0]
					ymin=next(fp1).split('>')[1].split('<')[0]
					xmax=next(fp1).split('>')[1].split('<')[0]
					ymax=next(fp1).split('>')[1].split('<')[0]
				except StopIteration:
					pass
				a=int(xmin)
				b=int(ymin)
				c=int(xmax)
				d=int(ymax)
				res=ori_img1[b:d,a:c]
				temp_path="/DATACENTER6/ph/traffic_model_faster101/in_pic/29-6-cut/"+str(ob_name)+"/"
				#print(temp_path)
				cv2.imwrite(temp_path+"29-6-"+str(count)+".jpg",res)
				count +=1
				#print("1")
				#print(ob_name,xmin,ymin,xmax,ymax)


def analyze_xml_class(file_names,class_name = []):
	'''解析xml的所有类别'''
    #for file_name in file_names:
	with open(file_names) as fp1:
		for p in fp1:
			if '<object>' in p:
				class_name.append(next(fp1).split('>')[1].split('<')[0])




if __name__ == '__main__':
	# class_name=[]
	# analyze_xml_class(file_path,class_name)
	# print(class_name)
	del_xml()