#coding=utf-8
from tqdm import tqdm
import glob
xml=glob.glob(r"/DATACENTER5/hao.pan/datasets/traffic_sign/Annotations/*.xml")

txt_file=open('trainval.txt','w')
train_file=open('train.txt','w')
val_file=open('val.txt','w')

xml_len=len(xml)
for i in tqdm(range(xml_len)):
	pic_name= xml[i].rstrip(".xml").split('Annotations/')[1]
	pic_name=pic_name+'\n'
	txt_file.write(pic_name)
	if i < (xml_len/2):
		pic_name= xml[i].rstrip(".xml").split('Annotations/')[1]
		pic_name=pic_name+'\n'
		train_file.write(pic_name)
	else:
		pic_name= xml[i].rstrip(".xml").split('Annotations/')[1]
		pic_name=pic_name+'\n'
		val_file.write(pic_name)