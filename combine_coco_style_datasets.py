# coding = utf-8
import json
from tqdm import tqdm

def get_max_img_id(rec_json):
	img_json=rec_json['images']
	img_len=len(img_json)
	count=0
	for i in range(img_len):
		temp=img_json[i]['id']
		if temp > count:
			count = temp
	return count

def get_max_anno_id(rec_json):
	anno_json=rec_json['annotations']
	anno_len=len(anno_json)
	count=0
	for i in range(anno_len):
		temp=anno_json[i]['id']
		if temp > count:
			count=temp
	return count
def main():
	f_in_obj=open(obj365_path)
	f_in_coco=open(coco_path)

	obj_json=json.load(f_in_obj)
	coco_json= json.load(f_in_coco)
	
	print("obj img's len = ")
	print(len(obj_json['images']))
	print("obj anno's len = ")
	print(len(obj_json['annotations']))
	
	print("coco img's len = ")
	print(len(coco_json['images']))
	print("coco anno's len = ")
	print(len(coco_json['annotations']))
	
	
	#获取原数据集中最大的img_id 和 anno_id
	max_img_id=get_max_img_id(obj_json)
	max_anno_id=get_max_anno_id(obj_json)
	
	
	new_imgs= obj_json['images']
	new_annos=obj_json['annotations']
	
	coco_img_len=len(coco_json['images'])
	coco_anno_len=len(coco_json['annotations'])
	
	ori_img=coco_json['images']
	# print(ori_img[0])
	# exit()
	ori_anno=coco_json['annotations']
	
	for i in tqdm(range(coco_img_len)):
		max_img_id=max_img_id+1
		
		one_ori_img=ori_img[i]
		cur_img_id=one_ori_img['id']
		
		#获取一个图片的id后根据这个id轮询annotation列表，
		#找到对应的anno，更改img_id和id，将改完的一个anno加入new_annos
		for n in range(coco_anno_len):
			anno_img_id=ori_anno[n]['image_id']
			if anno_img_id != cur_img_id:
				continue
			if anno_img_id == cur_img_id:
				max_anno_id=max_anno_id+1
				one_ori_anno=ori_anno[n]
				one_ori_anno['image_id']=max_img_id
				one_ori_anno['id']=max_anno_id
				#print(one_ori_anno)
				new_annos.append(one_ori_anno)
		
		#更改当前img的id，加入new_imgs
		one_ori_img['id']=max_img_id
		# print(one_ori_img)
		# print(new_imgs[3])
		# exit()
		new_imgs.append(one_ori_img)
	
		
	obj_json['images']=new_imgs
	obj_json['annotations']=new_annos
	
	print("result img's len = ")
	print(len(obj_json['images']))
	print("result anno's len = ")
	print(len(obj_json['annotations']))
	
	fq=open('combine_traffic_coco_train.json',"w")
	json.dump(obj_json,fq)
	


if __name__ == "__main__":
	max_img_id=0
	max_anno_id=0
	obj365_path='/DATACENTER6/hao.pan/datasets/traffic_5w/ImageSets/trainval.json'
	coco_path='/DATACENTER6/hao.pan/datasets/COCO/annotations/extract_person_vehicle_train.json'
	main()
	
