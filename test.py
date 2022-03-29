# import os
# files = os.listdir('/mnt/save_raw_files/')
# for file in files:
#  print(file, os.path.isdir(file))

import os
rootdir = '/mnt/save_raw_files/a/'
# for root,dirs,files in os.walk(rootdir):
#      for dir in dirs:
#          print(os.path.join(root,dir))
#     for file in files:
#         print(os.path.join(root,file))
i=0
for root,dirs,files in os.walk(rootdir):
	for file in files:
		print(os.path.join(root,file))
		i=i+1
print(i)