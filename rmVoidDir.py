# -*- coding: utf-8 -*-

import os # 引入文件操作库

def deldir(path):
	print ('*'*30)
	try:
		files = os.listdir(path) # 获取路径下的子文件(夹)列表
		print (files)
		for file in files:
			print ('遍历路径：'+os.fspath(path +'/'+ file))
			if os.path.isdir(os.fspath(path+'/'+file)): # 如果是文件夹
				print (file+'是文件夹')
				if not os.listdir(os.fspath(path+'/'+file)): # 如果子文件为空
					print (file+'是空文件夹,即将执行删除操作')
					os.rmdir(os.fspath(path+'/'+file)) # 删除这个空文件夹
			else:
				print (file+'不是空文件夹')
				deldir(os.fspath(path+'/'+file)) # 遍历子文件
				if not os.listdir(os.fspath(path+'/'+file)): # 如果子文件为空
					print (file+'是空文件夹,即将执行删除操作')
					os.rmdir(os.fspath(path+'/'+file)) # 删除这个空文件夹
		return
	except FileNotFoundError:
		print ("文件夹路径错误")

if __name__ == "__main__":
	path_list = '20210531','20210605','20210610','20210615','20210625','20210630','20210705','20210710','20210715','20210720','20210725','20210730','20210805','20210810','20210815','20210820','20210825','20210830','20210905','20210910','20210915','20210920','20210925','20210930','20211005','20211010','20211015','20211020','20211025','20211030','20211105','20211110','20211115','20211120','20211125','20211130','20211205','20211210','20211215','20211220','20220320','20220325'
	for path in path_list: # 输入路径
		deldir("/mnt/n/"+path)
