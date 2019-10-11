# encoding=utf-8
# author:hao.pan
# 2019/08/05
import os
import shutil #高级文件操作模块
import random

def get_all_file(dir):
	for pwd,folders,files in os.walk(dir):
		if pwd==dir:
			return sorted(files)
	return []

dir='/DATACENTER3/hao.pan/datasets/project_datasets/oil/oil_shanxi_finetune/unload/images/8-3'
print(get_all_file(dir))