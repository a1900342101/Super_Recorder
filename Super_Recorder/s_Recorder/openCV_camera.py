# coding:utf8
# 参考链接 http://lib.csdn.net/article/opencv/26790
import cv2


def capture():
    cap = cv2.VideoCapture(0)  # 0为摄像头id
    if not cap.isOpened():
        raise RuntimeError('Could not start camera.')
    ret, frame = cap.read()
    cv2.imwrite('s_Recorder/static/result.jpg', frame)
    # frames = open('/home/test-user/PycharmProjects/Screen_Recorder/s_Recorder/static/result.jpg', 'rb').read()
    # yield (b'frame\r\n' b'Content-Type: video/*\r\n\r\n'+frames + b'\r\n')
