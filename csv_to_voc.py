# coding= utf-8
from tqdm import tqdm
from lxml import etree, objectify

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
	
csv_path='/DATACENTER5/hao.pan/datasets/traffic_sign/train_label_fix.csv'
result_path='/DATACENTER5/hao.pan/datasets/traffic_sign/annotations/'

f_csv=open(csv_path)
count = 0
for i in tqdm(f_csv):
	if count==0:
		count=count+1
		continue
	one_obj=i.rstrip("\n").split(",",10)
	pic_name=one_obj[0].rstrip(".jpg")
	x1=one_obj[1]
	y1=one_obj[2]
	x2=one_obj[3]
	y2=one_obj[6]
	label=one_obj[9]
	tree=create_new_anno(pic_name,3200,1800)
	tree.append(create_new_obj(label,x1,y1,x2,y2))
	etree.ElementTree(tree).write(result_path+pic_name+".xml", pretty_print=True)
	