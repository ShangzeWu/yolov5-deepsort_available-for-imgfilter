import numpy as np

import tracker
from detector import Detector
import cv2
import time
import os
i=0
if __name__ == '__main__':

    # 初始化 yolov5
    detector = Detector()
    rootdir = '/mnt/save_raw_files' #视频根目录
    for root,dirs,files in os.walk(rootdir):
        for file in files:
            VideoPath = os.path.join(root,file) #获得每一个视频的路径
            i=i+1
            # 打开视频
            capture = cv2.VideoCapture(str(VideoPath))
            count = -1
            print(VideoPath)
            print(i)
            FPS_C=int(capture.get(5))
            while True:
                # 读取每帧图片
                _, im = capture.read()
                count = count +1
                if  count%FPS_C  != 0:#if  count%(2*FPS_C)!=0:
                    continue
                if im is None:
                    break
                # 缩小尺寸，1920x1080->960x540
                im1 = cv2.resize(im, (960, 540))

                list_bboxs = []
                bboxes = detector.detect(im1)

                # 如果画面中 有bbox
                if len(bboxes) > 0:
                    list_bboxs = tracker.update(bboxes, im1)
                    for (x1, y1, x2, y2, cls_id, pos_id) in list_bboxs:
                        if str(cls_id) == 'person':
                            t=time.time()
                            t=int(round(t*1000))
                            savepath = root+'/'+os.path.splitext(file)[0]# +'/'+str(pos_id)
                            if  not os.path.exists(savepath):
                                os.makedirs(savepath)
                            im_shape = im.shape
                            #print(im_shape[0],im_shape[1])
                            #print(y1,y2,x1,x2)
                            o_y1 = int(y1*im_shape[0]/540)
                            o_y2 = int(y2*im_shape[0]/540)
                            o_x1 = int(x1*im_shape[1]/960)
                            o_x2 = int(x2*im_shape[1]/960)
                            #print(o_y1,o_y2,o_x1,o_x2)
                            #cropped = im1[y1:y2,x1:x2]
                            cropped = im[o_y1:o_y2,o_x1:o_x2]
                            if cropped .size != 0:
                                cv2.imwrite(savepath+'/'+str(t)+'.jpg' ,cropped )
                    # 画框
                    #output_image_frame = tracker.draw_bboxes(im, list_bboxs, line_thickness=None)
                    pass
                else:
                    # 如果画面中 没有bbox
                    #output_image_frame = im
                    pass

                #cv2.imshow('demo', output_image_frame)
                cv2.waitKey(1)

                pass
            pass
            if os.path.splitext(file)[1] =='.mp4':
                os.remove(str(VideoPath))
                print("已经删除：",str(VideoPath))

            capture.release()
            cv2.destroyAllWindows()
