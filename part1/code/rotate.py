# 功能：旋转原始图片，使之摆正

import numpy as np
import cv2
import math
from scipy import misc, ndimage
import os

file_dir = '../data/real_image'
file_name = []
for root, dirs, files in os.walk(file_dir):
    file_name = files
for i in file_name:
    src = cv2.imread("../data/real_image/{}".format(i))
    rgbsrc = src.copy()
    graysrc = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 转为灰度图
    blurimg = cv2.GaussianBlur(graysrc, (3, 3), 0)  # 对灰度图做高斯滤波
    Cannyimg = cv2.Canny(blurimg, 35, 189)
    lines = cv2.HoughLines(Cannyimg, 1, np.pi/360, 500)  # 霍夫变换
    list_a = lines[:, :, 1]
    rotate_angle = np.median(list_a)*(180/np.pi)  # 弧度转角度

    ''' 计算旋转角度'''
    if rotate_angle > 45:
        rotate_angle = -90 + rotate_angle
    elif rotate_angle < -45:
        rotate_angle = 90 + rotate_angle

    h, w, depth = src.shape
    img_change = cv2.getRotationMatrix2D((w / 2, h / 2), rotate_angle, 1)
    rotate_img = cv2.warpAffine(
        src, img_change, (w, h), borderValue=(255, 255, 255))  # 去除黑边，填充白色
    folder = os.path.exists('../data/rotate_image')
    if not folder:
        os.makedirs('../data/rotate_image')
    cv2.imwrite('../data/rotate_image/{}'.format(i), rotate_img)
