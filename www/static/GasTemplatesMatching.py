#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os
import numpy as np
import PIL
from PIL import Image
import matplotlib.pyplot as plt
#import necesseray lib

def TM(img,template,stepsize):           ## Template matching(Image, Template, stepsize)
    v = np.zeros((10,1))
    for i in range(0,10):
        tmp2 = template[:,:,i]
        u = -1000
        for j in range(0,20,stepsize):    ## Move the picture Horiz and Verticle to do match
            for k in range(0,20,stepsize):
                tmp1 = img[j:j+160,k:k+64]
                u = max(u,sum(sum(tmp1*tmp2)))
        v[i] = u
    pos = np.argmax(v)
    return pos

def read_gas_meter(image_arr,template_dir):

    img=Image.open(image_arr)
    ##plt.imshow(img)   #plot the origin image
    result=np.array(img)    
    #transfer img to numpy array
    ##result.shape      #show the origin image size((720, 1280, 3))

    r,g,b=img.split()   #split r g b channel
    r_arr = np.array(r)
    g_arr = np.array(g)
    b_arr = np.array(b)
    ##plt.imshow(r_arr,cmap='gray')  #plot the r channel img with 'cmap=gray'

    r_X,r_Y=np.where(r_arr==255)     #r_X,r_Y shows the white point on r channel img to locate the monitor with orange label
    r_xmin=min(r_X)
    r_xmax=max(r_X)
    if r_xmin<140:
        p11=r_X>140
        p12=r_X*p11
        p13=p12[p12!=0]
        r_xmin=min(p13)
    if r_xmax>390:
        p21=r_X<390
        p22=r_X*p21
        p23=p22[p22!=0]
        r_xmax=max(p23)

    r_ymin=min(r_Y)
    r_ymax=max(r_Y)
    r_new=r_arr[r_xmin:r_xmax,r_ymin:r_ymax]
    g_new=g_arr[r_xmin:r_xmax,r_ymin:r_ymax]
    b_new=b_arr[r_xmin:r_xmax,r_ymin:r_ymax]
    img_new=result[r_xmin:r_xmax,r_ymin:r_ymax,:]
    # plt.imshow(img_new)

    i = 1
    j = 1
    red_point_x=np.array([],int)
    red_point_y=np.array([],int)
    width = len(img_new[:,1,1])#长度
    height = len(img_new[1,:,1])#宽度
    for i in range(0,width):#遍历所有长度的点
        for j in range(0,height):#遍历所有宽度的点
            #每个像素点的颜色RGB的值(r,g,b)
            data_r = r_new[i,j]#打印该图片的所有点
            data_g = g_new[i,j]
            data_b = b_new[i,j]
            # 判断RGBA的值
            if (data_r>=200 and data_g<=100 and data_b<=100):
                red_point_x = np.r_[red_point_x,i]
                red_point_y = np.r_[red_point_y,j]

    Red_xmin=np.min(red_point_x)
    po=np.where(red_point_x==Red_xmin)
    Red_ymin=red_point_y[po[0]]

    # the digits templates
    # 193 29
    # 55-68  85-98 114-127 143-156 172-185 202-215 231-244 266-279
    # 27-48  28-49 28-49   28-49   29-50   30-51   31-52   32-53
    digit1=img_new[Red_xmin-1:Red_xmin-1+21,Red_ymin[0]-(193-53):Red_ymin[0]-(193-53)+13,:]
    digit2=img_new[Red_xmin-1:Red_xmin-1+21,Red_ymin[0]-(193-83):Red_ymin[0]-(193-83)+13,:]
    digit3=img_new[Red_xmin-1:Red_xmin-1+21,Red_ymin[0]-(193-113):Red_ymin[0]-(193-113)+13,:]
    digit4=img_new[Red_xmin-1:Red_xmin-1+21,Red_ymin[0]-(193-142):Red_ymin[0]-(193-142)+13,:]
    digit5=img_new[Red_xmin:Red_xmin+21,Red_ymin[0]-(193-171):Red_ymin[0]-(193-171)+13,:]
    digit6=img_new[Red_xmin+1:Red_xmin+1+21,Red_ymin[0]-(193-201):Red_ymin[0]-(193-201)+13,:]
    digit7=img_new[Red_xmin+2:Red_xmin+2+21,Red_ymin[0]-(193-230):Red_ymin[0]-(193-230)+13,:]
    digit8=img_new[Red_xmin+3:Red_xmin+3+21,Red_ymin[0]-(193-264):Red_ymin[0]-(193-264)+13,:]

    ## Initialize the digit picture to RGB (160,64) and binarization.
    d1 = Image.fromarray(digit1)
    d1 = d1.resize((64, 160), PIL.Image.ANTIALIAS)
    d1 = d1.convert("L")
    d1 = d1.point(lambda x: 255 if x > 125 else 0)
    d1 = d1.convert("RGB")


    d2 = Image.fromarray(digit2)
    d2 = d2.resize((64, 160), PIL.Image.ANTIALIAS)
    d2 = d2.convert("L")
    d2 = d2.point(lambda x: 255 if x > 125 else 0)
    d2 = d2.convert("RGB")

    d3 = Image.fromarray(digit3)
    d3 = d3.resize((64, 160), PIL.Image.ANTIALIAS)
    d3 = d3.convert("L")
    d3 = d3.point(lambda x: 255 if x > 125 else 0)
    d3 = d3.convert("RGB")

    d4 = Image.fromarray(digit4)
    d4 = d4.resize((64, 160), PIL.Image.ANTIALIAS)
    d4 = d4.convert("L")
    d4 = d4.point(lambda x: 255 if x > 125 else 0)
    d4 = d4.convert("RGB")

    d5 = Image.fromarray(digit5)
    d5 = d5.resize((64, 160), PIL.Image.ANTIALIAS)
    d5 = d5.convert("L")
    d5 = d5.point(lambda x: 255 if x > 125 else 0)
    d5 = d5.convert("RGB")

    d6 = Image.fromarray(digit6)
    d6 = d6.resize((64, 160), PIL.Image.ANTIALIAS)
    d6 = d6.convert("L")
    d6 = d6.point(lambda x: 255 if x > 125 else 0)
    d6 = d6.convert("RGB")

    d7 = Image.fromarray(digit7)
    d7 = d7.resize((64, 160), PIL.Image.ANTIALIAS)
    d7 = d7.convert("L")
    d7 = d7.point(lambda x: 255 if x > 125 else 0)
    d7 = d7.convert("RGB")

    d8 = Image.fromarray(digit8)
    d8 = d8.resize((64, 160), PIL.Image.ANTIALIAS)
    d8 = d8.convert("L")
    d8 = d8.point(lambda x: 255 if x > 125 else 0)
    d8 = d8.convert("RGB")

    #plt.subplot(241);plt.imshow(d1)
    #plt.subplot(242);plt.imshow(d2)
    #plt.subplot(243);plt.imshow(d3)
    #plt.subplot(244);plt.imshow(d4)
    #plt.subplot(245);plt.imshow(d5)
    #plt.subplot(246);plt.imshow(d6)
    #plt.subplot(247);plt.imshow(d7)
    #plt.subplot(248);plt.imshow(d8)

    template = np.load(template_dir)
    GasNum = [d1,d2,d3,d4,d5,d6,d7]
    padded = np.zeros((180,84))             ## Initialize the Pad for digit picture
    PredictNumber = 0.5*np.ones(7)
    for i in range(7):
        padded[10:170,10:74] = np.array(GasNum[i])[:,:,0]
        PredictNumber[i] = TM(padded,template,3)
        
    return PredictNumber    
# print(PredictNumber.astype(int))


# In[ ]:




