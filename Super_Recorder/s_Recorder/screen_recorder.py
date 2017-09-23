# coding:utf8
import pyscreenshot as ImageGrab


def recoder():
    image = ImageGrab.grab()
    image.save('/home/test-user/PycharmProjects/Screen_Recorder/s_Recorder/static/result.jpg')
    # frames = open('/home/test-user/PycharmProjects/Screen_Recorder/s_Recorder/static/result.jpg', 'rb').read()
    # yield (b'frame\r\n' b'Content-Type: video/*\r\n\r\n' + frames + b'\r\n')
