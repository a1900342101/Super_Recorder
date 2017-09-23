# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import HttpResponse
from django.shortcuts import render_to_response

from screen_recorder import recoder
from s_Recorder import openCV_camera


def index(req):
    return render_to_response('index.html', {'title': 'Running success'})


def video(req):
    # response = HttpResponse(recoder(), content_type='multipart/x-mixed-replace; boundary=frame')
    # response = HttpResponse(get_frame(), content_type='multipart/x-mixed-replace; boundary=frame')  # 'text/html') #'
    # response = HttpResponse(openCV_camera.capture(), content_type='multipart/x-mixed-replace; boundary=frame')
    # return response
    recoder()
    return render_to_response('index.html', {'title': 'Screenshot success'})


def camera(req):
    openCV_camera.capture()
    return render_to_response('index.html', {'title': 'Camera success'})


def not_found(req):
    return render_to_response('404.html', {'title': 'NotFound'})
