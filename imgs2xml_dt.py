#coding: utf-8
from basicFun import modelTool
import cv2
# import cv2.cv
import detectron.utils.vis as vis_utils
import os
import sys
import shutil
from PIL import Image,ImageDraw,ImageFont
import numpy
from basicFun import XML,FILES,COCO
import time
try: 
    import xml.etree.cElementTree as ET 
except ImportError: 
    import xml.etree.ElementTree as ET
def drawImg(img,top_labels,top_xmin,top_ymin,top_xmax,top_ymax,top_scores):
    name_font = ImageFont.truetype('/DATACENTER4/hao.yang/common/heiti.TTF',10)
    score_font = ImageFont.truetype('/DATACENTER4/hao.yang/common/heiti.TTF',10)
    labels=[]
    xmins=[]
    ymins=[]
    xmaxs=[]
    ymaxs=[]
    for i in range(len(top_labels)):
        xmin = int(round(top_xmin[i] * img.shape[1]))
        ymin = int(round(top_ymin[i] * img.shape[0]))
        xmax = int(round(top_xmax[i] * img.shape[1]))
        ymax = int(round(top_ymax[i] * img.shape[0]))
        if xmax-xmin>0 and ymax-ymin>0 :
            # if not showNames or top_labels[i] in showNames:
                # cv2.rectangle(img, (xmin,ymin), (xmax, ymax), palette[top_labels[i]], thickness=3)
                # img_PIL = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB)) # cv2==>PIL
                # draw = ImageDraw.Draw(img_PIL)
                # draw.text((xmin+5,ymin+5),str(top_labels[i]),palette[top_labels[i]][::-1],font=name_font)
                # draw.text((xmin+5,ymin+15),'{:.2f}'.format(top_scores[i]),palette[top_labels[i]][::-1],font=name_font)        
                # img = cv2.cvtColor(numpy.asarray(img_PIL),cv2.COLOR_RGB2BGR) # PIL==>cv2
            labels.append(top_labels[i])
            xmins.append(xmin)
            ymins.append(ymin)
            xmaxs.append(xmax)
            ymaxs.append(ymax)
    return img,labels,xmins,ymins,xmaxs,ymaxs
if __name__=="__main__":
    task='safe'
    showType='all'
    WTS_PATH =getattr(COCO,'model_{}'.format(task))
    CFG_PATH=WTS_PATH.replace('.pkl','.yaml')
    modelName=WTS_PATH.split('/')[-1].split('.')[0]
    labelmap=getattr(COCO,'labelmap_{}'.format(task))
    inImg = '/DATACENTER4/hao.yang/project/Qin/data/imgs/safe/safe_FMXX_img/'
    tarXmlDir='/DATACENTER4/hao.yang/project/Qin/data/xmls/safe/modelXml_safe_FMXX'
    FILES.rm_mkdir(tarXmlDir)
    referXml="/DATACENTER4/hao.yang/common/refer.xml"
    if hasattr(COCO,'showNames_{}'.format(task)):
        showNames=getattr(COCO,'showNames_{}'.format(task))[showType]
    else:
        showNames=[]
    countNothing=0
    font = cv2.FONT_HERSHEY_SIMPLEX
    testModel = modelTool.modelTool()
    testModel.initModel(CFG_PATH,WTS_PATH,labelmap)
    paletteSet=[(247,79,223),(0,255,255),(255,247,0),(200,130,2),(255,255,255),(30,170,180),(102,0,204),
    (44,125,222),(0,255,0),(1,208,169),(130,232,255),(204,153,255),(0,0,192),(134,225,1),(142,208,169),(115,160,110)]
    palette={}
    for i in labelmap.keys():
        palette[labelmap[i]]=paletteSet[i]
    fileList = [x for x in os.listdir(inImg) if '.jpg' in x]
    start=0
    for file in fileList:
        image = cv2.imread(os.path.join(inImg,file))
        height=image.shape[0]
        width=image.shape[1]
        detectBgn=time.time()
        top_labels,top_xmin,top_ymin,top_xmax,top_ymax,top_scores = testModel.getInfoByModel(image,0.7)
        if top_labels:
            #outImg
            image,labels,xmins,ymins,xmaxs,ymaxs =drawImg(image,top_labels,top_xmin,top_ymin,top_xmax,top_ymax,top_scores)
            # desImg = os.path.join(outImg,file)
            # cv2.imwrite(desImg,image)
            # # outXml
            if len(labels)>0:
                tarXml=os.path.join(tarXmlDir,file.split('.')[0]+'.xml')
                shutil.copy(referXml,tarXml)
                tree = ET.ElementTree(file=tarXml)
                root = tree.getroot()
                for i in range(len(labels)):
                    # if labels[i] not in ["close","open","cover"]:
                    if 1>0:
                        xmin = str(xmins[i])
                        ymin = str(ymins[i])
                        xmax = str(xmaxs[i])
                        ymax = str(ymaxs[i])
                        # print(labels[i],xmin,ymin,xmax,ymax)
                        obj={'name':labels[i],'xmin':xmin,'ymin':ymin,'xmax':xmax,'ymax':ymax}
                        XML.add_tag(root,obj)
                        XML.write_xml(tree,tarXml)      









   
