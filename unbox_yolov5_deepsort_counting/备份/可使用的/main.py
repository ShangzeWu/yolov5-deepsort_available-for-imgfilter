import numpy as np

import tracker
from detector import Detector
import cv2
import time
import os

if __name__ == '__main__':

    # 初始化 yolov5
    detector = Detector()

    # 打开视频
    capture = cv2.VideoCapture('./video/FD_20211117.mp4')
    # capture = cv2.VideoCapture('/mnt/datasets/datasets/towncentre/TownCentreXVID.avi')

    while True:
        # 读取每帧图片
        _, im = capture.read()
        if im is None:
            break

        # 缩小尺寸，1920x1080->960x540
        im = cv2.resize(im, (960, 540))

        list_bboxs = []
        bboxes = detector.detect(im)

        # 如果画面中 有bbox
        if len(bboxes) > 0:
            list_bboxs = tracker.update(bboxes, im)
            for (x1, y1, x2, y2, cls_id, pos_id) in list_bboxs:
                if str(cls_id) == 'person':
                    t=time.time()
                    t=int(round(t*1000))
                    savepath = './results/'+str(cls_id)+'/'+str(pos_id)
                    if  not os.path.exists(savepath):
                        os.makedirs(savepath)
                    cropped = im[y1:y2,x1:x2]

                    #cv2.imshow('demo1',cropped)
                    #if cropped != None:
                    cv2.imwrite(savepath+'/'+str(t)+'.jpg' ,cropped )

            # 画框
            output_image_frame = tracker.draw_bboxes(im, list_bboxs, line_thickness=None)
            pass
        else:
            # 如果画面中 没有bbox
            output_image_frame = im
        pass

        cv2.imshow('demo', output_image_frame)
        cv2.waitKey(1)

        pass
    pass

    capture.release()
    cv2.destroyAllWindows()
