# coding:utf-8
'''
功能：表格抠格子
'''
# 横竖线都去，向下多取8像素
import cv2
import numpy as np
import os
file_dir = '../data/rotate_image/'
pixel_map = [[  # ['id', 0, 0, 0, 0],         # 登记表编号 = 文件名
    # 2011大部分
    ['sex', 600, 670, 50, 85],                # 性别
    ['nation', 765, 860, 50, 85],             # 民族
    ['weight', 600, 670, 85, 120],            # 体重
    ['blood', 765, 860, 85, 120],             # 血型
    ['hometown', 765, 860, 125, 170],         # 籍贯
    ['high_school_name', 270, 550, 765, 805],    # 高中学校名称
    ['high_school_major', 555, 690, 765, 805],   # 高中专业
    ['high_school_degree', 695, 775, 765, 805],  # 高中学位
    ['high_school_time', 780, 895, 765, 805],    # 高中起止时间
    ['high_school_pass', 925, 1045, 765, 805],   # 高中是否毕业
    ['junior_college_name', 270, 550, 805, 845],      # 大专
    ['junior_college_major', 555, 690, 805, 845],
    ['junior_college_degree', 695, 775, 805, 845],
    ['junior_college_time', 780, 895, 805, 845],
    ['junior_college_pass', 925, 1045, 805, 845],
    ['undergraduate_name', 270, 550, 845, 890],       # 本科
    ['undergraduate_major', 555, 690, 845, 890],
    ['undergraduate_degree', 695, 775, 845, 890],
    ['undergraduate_time', 780, 895, 845, 890],
    ['undergraduate_pass', 925, 1045, 845, 890],
    ['graduate_name', 270, 550, 890, 935],            # 研究生
    ['graduate_major', 555, 690, 890, 935],
    ['graduate_degree', 695, 775, 890, 935],
    ['graduate_time', 780, 895, 890, 935],
    ['graduate_pass', 925, 1045, 890, 935]],
    # ['other_name', 270, 550, 0, 0],               # 其他学历
    # ['other_major', 555, 690, 0, 0],
    # ['other_degree', 695, 775, 0, 0],
    # ['other_time', 780, 895, 0, 0],
    # ['other_pass', 925, 1045, 0, 0]],

    # 2011小部分+其余年份
    [['sex', 570, 690, 50, 95],                # 性别
     ['nation', 805, 925, 50, 95],             # 民族
     ['weight', 570, 690, 95, 140],            # 体重
     ['blood', 805, 925, 95, 140],             # 血型
     ['hometown', 805, 925, 140, 190],         # 籍贯
     ['high_school_name', 105, 455, 830, 880],    # 高中学校名称
     ['high_school_major', 460, 650, 830, 880],   # 高中专业
     ['high_school_degree', 650, 755, 830, 880],  # 高中学位
     ['high_school_time', 760, 920, 830, 880],    # 高中起止时间
     ['high_school_pass', 925, 1095, 830, 880],   # 高中是否毕业
     ['junior_college_name', 105, 455, 880, 925],      # 大专
     ['junior_college_major', 460, 650, 880, 925],
     ['junior_college_degree', 650, 755, 880, 925],
     ['junior_college_time', 760, 920, 880, 925],
     ['junior_college_pass', 925, 1095, 880, 925],
     ['undergraduate_name', 105, 455, 925, 970],       # 本科
     ['undergraduate_major', 460, 650, 925, 970],
     ['undergraduate_degree', 650, 755, 925, 970],
     ['undergraduate_time', 760, 920, 925, 970],
     ['undergraduate_pass', 925, 1095, 925, 970],
     ['graduate_name', 105, 455, 970, 1015],            # 研究生
     ['graduate_major', 460, 650, 970, 1015],
     ['graduate_degree', 650, 755, 970, 1015],
     ['graduate_time', 760, 920, 970, 1015],
     ['graduate_pass', 925, 1095, 970, 1015]],

    # 2011中部分
    [['sex', 600, 670, 50, 85],                # 性别
     ['nation', 765, 860, 50, 85],             # 民族
     ['weight', 600, 670, 85, 120],            # 体重
     ['blood', 765, 860, 85, 120],             # 血型
     ['hometown', 765, 860, 125, 170],         # 籍贯
     ['high_school_name', 205, 490, 765, 805],    # 高中学校名称
     ['high_school_major', 490, 665, 765, 805],   # 高中专业
     ['high_school_degree', 665, 745, 765, 805],  # 高中学位
     ['high_school_time', 750, 925, 765, 805],    # 高中起止时间
     ['high_school_pass', 925, 1080, 765, 805],   # 高中是否毕业
     ['junior_college_name', 205, 490, 805, 845],      # 大专
     ['junior_college_major', 490, 665, 805, 845],
     ['junior_college_degree', 665, 745, 805, 845],
     ['junior_college_time', 750, 925, 805, 845],
     ['junior_college_pass', 925, 1080, 805, 845],
     ['undergraduate_name', 205, 490, 845, 890],       # 本科
     ['undergraduate_major', 490, 665, 845, 890],
     ['undergraduate_degree', 665, 745, 845, 890],
     ['undergraduate_time', 750, 925, 845, 890],
     ['undergraduate_pass', 925, 1080, 845, 890],
     ['graduate_name', 205, 490, 890, 935],            # 研究生
     ['graduate_major', 490, 665, 890, 935],
     ['graduate_degree', 665, 745, 890, 935],
     ['graduate_time', 750, 925, 890, 935],
     ['graduate_pass', 925, 1080, 890, 935]]]

file_name = []
for root, dirs, files in os.walk(file_dir):
    file_name = files
for fi in file_name:
    img1 = cv2.imread('../data/rotate_image/{}'.format(fi))
    print("read {}{}".format(file_dir, fi))
    gray_img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    thresh_img = cv2.adaptiveThreshold(
        ~gray_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, -2)  # 二值图

    h_img = thresh_img.copy()
    v_img = thresh_img.copy()
    h_structure = cv2.getStructuringElement(cv2.MORPH_RECT, (50, 1))  # 横向
    h_erode_img = cv2.erode(h_img, h_structure, 1)  # 腐蚀
    h_dilate_img = cv2.dilate(h_erode_img, h_structure, 1)  # 膨胀图像

    v_structure = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 10))  # 纵向
    v_erode_img = cv2.erode(v_img, v_structure, 1)  # 腐蚀
    v_dilate_img = cv2.dilate(v_erode_img, v_structure, 1)  # 膨胀图像

    mask_img = h_dilate_img+v_dilate_img  # 纵横线交叉
    joints_img = cv2.bitwise_and(h_dilate_img, v_dilate_img)  # 交点图

    a = np.nonzero(joints_img)  # 找最靠左上角的交点做参照点
    t = (a[0]-250)**2+(a[1]-40)**2
    min_loc = t.argmin()
    x = a[1][min_loc]
    y = a[0][min_loc]

    ''' 重新画匹配用竖线 '''
    v_structure1 = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 50))
    v_erode_img1 = cv2.erode(v_img, v_structure1, 1)
    v_dilate_img1 = cv2.dilate(v_erode_img1, v_structure1, 1)
    mask_img1 = h_dilate_img+v_dilate_img1  # 纵横线交叉
    joints_img1 = cv2.bitwise_and(h_dilate_img, v_dilate_img1)  # 交点图
    b = np.nonzero(joints_img1)  # b中保存膨胀腐蚀得到的交点坐标

    ''' 重新画白线用网格 '''
    h_structure2 = cv2.getStructuringElement(cv2.MORPH_RECT, (100, 1))  # 形态学因子
    h_erode_img2 = cv2.erode(h_img, h_structure2, 1)
    h_dilate_img2 = cv2.dilate(h_erode_img2, h_structure2, 1)
    v_structure2 = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 100))
    v_erode_img2 = cv2.erode(v_img, v_structure2, 1)
    v_dilate_img2 = cv2.dilate(v_erode_img2, v_structure2, 1)
    mask_img2 = h_dilate_img2 + v_dilate_img2  # 纵横线交叉
    joints_img2 = cv2.bitwise_and(h_dilate_img2, v_dilate_img2)  # 交点图

    ''' 画白线遮盖住表格 '''
    binary, contours, hierarchy = cv2.findContours(
        mask_img2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img1, contours, -1, (255, 255, 255), 2)

    if(fi.find('2011') == 0):  # 判断表格类型
        TYPE = 0  # 2011年版大部分
        x3 = int(x+20)
        y3 = int(y+750)
        x4 = int(x+70)
        y4 = int(y+770)
        cropImg1 = thresh_img[y3:y4, x3:x4]  # 挑选指定区域，通过有无黑像素来分类
        x3 = int(x+485)
        y3 = int(y+740)
        x4 = int(x+520)
        y4 = int(y+745)
        cropImg2 = mask_img1[y3:y4, x3:x4]
        if(len(np.nonzero(cropImg1)[0]) == 0):
            TYPE = 1  # 2011年小部分
        elif(len(np.nonzero(cropImg2)[0]) != 0):
            TYPE = 2
    else:
        TYPE = 1  # 其余年份
    for i in range(len(pixel_map[TYPE])):
        column, x1, x2, y1, y2 = pixel_map[TYPE][i]  # 读取预置坐标偏移
        x3 = int(x+x1)
        y3 = int(y+y1)
        x4 = int(x+x2)
        y4 = int(y+y2)

        ''' 校正，预制模板和实际每张图的交点坐标匹配，从而得到精准的格子坐标 '''
        t1 = (b[0]-y3)**2+(b[1]-x3)**2  # 左上角点
        min_loc = t1.argmin()
        x3 = b[1][min_loc]
        y3 = b[0][min_loc]
        t2 = (b[0]-y4)**2+(b[1]-x4)**2  # 右下角点
        min_loc = t2.argmin()
        print(t1.min(), t2.min())
        x4 = b[1][min_loc]
        y4 = b[0][min_loc]
        if((x4-x3) < 60 or (y4-y3) < 10 or (y4-y3) > 60 or ((i < 5) & ((x4-x3) > 150))):
            x3 = int(x+x1)
            y3 = int(y+y1)
            x4 = int(x+x2)
            y4 = int(y+y2)
            print('!!!!!!!!!!!!!!!!!')

        print(x, y)
        print(x3, y3)
        print(x4, y4)

        cropImg = img1[y3:(y4+8), x3:x4]  # 裁剪格子，并向下多取8像素

        print(fi)
        folder = os.path.exists('../data/cut_image/{}'.format(column))
        if not folder:
            os.makedirs('../data/cut_image/{}'.format(column))
        cv2.imwrite('../data/cut_image/{}/{}'.format(column, fi), cropImg)
