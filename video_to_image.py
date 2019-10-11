# coding=utf-8
import cv2
from tqdm import tqdm
def extra_frames(videoPath,outPath,imgInfo,interval):
	catcher= cv2.VideoCapture(videoPath) #读入视频文件
	count=0
	flag=catcher.isOpened()
	img_id=0
	while flag:   #循环读取视频帧
	    count = count + 1
	    flag, frame = catcher.read()
	    if flag and (count%interval== 0):
	    	img_id = img_id + 1
	    	cv2.imwrite(outPath+imgInfo+str('%06d'%img_id) + '.jpg', frame) #存储为图像
	    	cv2.waitKey(1)
	catcher.release()

if __name__=="__main__":
	#--------------------------------------config
		videoPath="/DATACENTER3/hao.pan/datasets/project_datasets/oil/oil_shanxi_finetune/unload/video/9-25_pipeline/3.mp4"
		outPath="/DATACENTER3/hao.pan/datasets/project_datasets/oil/oil_shanxi_finetune/unload/images/9-25_pipeline/"
		imgInfo="oil_shanxi_unload_day_190925_pipeFinetune_3_"
		interval=120
	#--------------------------------------
		extra_frames(videoPath,outPath,imgInfo,interval)