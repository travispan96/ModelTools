# coding=utf-8
import cv2
import json
import glob
import numpy as np


xml=glob.glob(r"/DATACENTER1/hao.pan/video_data/cut_pic/4-6-4/*.xml")
#xml=glob.glob(r"/DATACENTER1/hao.pan/tools/*.xml")
xml_len=int(len(xml))
w=1920
h=1080


for i in range(xml_len):
	open_xml =open(xml[i])
	#print(xml[i])
	temp     =xml[i].rstrip(".xml")
	ori_json = {"boxes":[],"scores":[],"labels":[]}
	for n in open_xml:
		if '<object>' in n:
			try:
				type_MOT=next(open_xml).split('>')[1].split('<')[0]
			except StopIteration: 
				pass
			#type_json = [type_MOT]
			if type_MOT =='car':
				label=1
			if type_MOT =='person':
				label=8
			if type_MOT =='SUV':
				label=3
			if type_MOT =='truck':
				label=5
			if type_MOT =='bus':
				label=2
			if type_MOT =='tricycle':
				label=9
			if type_MOT =='engineeringvan':
				label=12
			if type_MOT =='tractor':
				label=6
			if type_MOT =='tanker':
				label=11
			if type_MOT =='pickup':
				label=7
			if type_MOT =='microbus':
				label=4
			if type_MOT =='motorbike':
				label=10
			labels=list(ori_json["labels"])
			labels.append(label)
			ori_json["labels"]=labels
		if '<bndbox>' in n:
			try:
				xmin=next(open_xml).split('>')[1].split('<')[0]
				ymin=next(open_xml).split('>')[1].split('<')[0]
				xmax=next(open_xml).split('>')[1].split('<')[0]
				ymax=next(open_xml).split('>')[1].split('<')[0]
			except StopIteration:
				pass
			xmin=float(xmin)/w
			ymin=float(ymin)/h
			xmax=float(xmax)/w
			ymax=float(ymax)/h
			box_json = [ymin,xmin,ymax,xmax]
			#print(box_json)
			boxes=list(ori_json["boxes"])
			boxes.append(box_json)
			ori_json["boxes"]=boxes
		if '</bndbox>' in n:
			try:
				get_score=next(open_xml).split('>')[1].split('<')[0]
			except StopIteration:
				pass
			split_score=get_score.split(' ',13)
			c1=float(split_score[1])
			c2=float(split_score[2])
			c3=float(split_score[3])
			c4=float(split_score[4])
			c5=float(split_score[5])
			c6=float(split_score[6])
			c7=float(split_score[7])
			c8=float(split_score[8])
			c9=float(split_score[9])
			c10=float(split_score[10])
			c11=float(split_score[11])
			c12=float(split_score[12])
			score_json = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12]
			scores=list(ori_json["scores"])
			scores.append(score_json)
			ori_json["scores"]=scores
			#test
	path=temp+'.json'
	res_json=json.dumps(ori_json,indent=2)
	#res_json=bytes(res_json,encoding="utf8")
	with open(path,'wb') as f:
		f.write(res_json)



