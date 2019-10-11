# coding=utf-8
import json
import glob
from tqdm import tqdm
from lxml import etree, objectify

def get_cate_name(cate_info,cate_id):
	cate_num=len(cate_info)
	id=cate_id
	for i in range(cate_num):
		if id == cate_info[i]['id']:
			cate_name=cate_info[i]['name']
			break
	return cate_name

def create_new_anno(file_name, width,height):
	w=width
	h=height
	name=str(file_name)
	
	E = objectify.ElementMaker(annotate=False)
	anno_tree = E.annotation(
		E.folder('a'),
		E.filename(name),
		E.source(
			E.database('traffic'),
		),
		E.size(
			E.width(w),
			E.height(h),
			E.depth(3)
		),
		E.segmented(0)
	)
	
	return anno_tree
	
	
def create_new_obj(obj_name,x1,y1,x2,y2):
	rec_name= str(obj_name)
	E2 = objectify.ElementMaker(annotate=False)
	anno_tree2 = E2.object(
		E2.name(rec_name),
		E2.bndbox(
			E2.xmin(x1),
			E2.ymin(y1),
			E2.xmax(x2),
			E2.ymax(y2)
		),
		E2.difficult(0)
	)
	return anno_tree2

coco_path='/DATACENTER6/hao.pan/datasets/COCO/annotations/extract_person_vehicle_train.json'
result_path='/DATACENTER6/hao.pan/datasets/COCO/annotations/voc_style/'

f=open(coco_path)
ori_json=json.load(f)

img_info=ori_json['images']
anno_info=ori_json['annotations']
cate_info=ori_json['categories']
img_len=len(img_info)
anno_len=len(anno_info)

for i in tqdm(range(img_len)):
	id=img_info[i]['id']
	file_name=img_info[i]['file_name'].rstrip(".jpg")
	w=img_info[i]['width']
	h=img_info[i]['height']
	tree=create_new_anno(file_name,w,h)
	for n in range(anno_len):
		img_id=anno_info[n]['image_id']
		if id != img_id:
			continue
		elif id == img_id:
			x1=anno_info[n]['bbox'][0]
			y1=anno_info[n]['bbox'][1]
			w=anno_info[n]['bbox'][2]
			h=anno_info[n]['bbox'][3]
			x2=x1+w
			y2=y1+h
			cate_id=anno_info[n]['category_id']
			cate_name=get_cate_name(cate_info,cate_id)
			obj_tree=create_new_obj(cate_name,x1,y1,x2,y2)
			tree.append(obj_tree)
		else:
			print("error")
			exit()
	etree.ElementTree(tree).write(result_path+file_name+".xml", pretty_print=True)






























