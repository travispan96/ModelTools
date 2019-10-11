import os
import cv2
import numpy as np

path = '/DATACENTER8/hjy/tmp/output_image/video_demo/5393_d/'
file_len = len(os.listdir(path))
fps = 24 #视频每秒24帧
#size = (1024, 576) #需要转为视频的图片的尺寸
size = (568, 320)
#size = (1920, 1080)
#可以使用cv2.resize()进行修改

video = cv2.VideoWriter("3.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
#视频保存在当前目录下
item=1
while item != file_len+1:
	temp = path + str(item) + '.jpg'
	img = cv2.imread(temp)
	video.write(img)
	item=item+1

video.release()
cv2.destroyAllWindows()
