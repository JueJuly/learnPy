# coding=utf-8
import sys 
sys.path.insert(0,"..")
import os
import numpy as np
# import cv2
import matplotlib.pyplot as plt
import scipy 
import PIL
import torch
import torchvision
# import test
from test import * 




# 为了证明opencv中是颜色顺序是BGR
img = np.array([
    [[255, 0, 0],[0, 255, 0],[0, 0, 255]],
    [[255, 255, 0],[255, 0, 255],[0, 255, 255]],
    [[255, 255, 255],[128, 128, 128],[0, 0, 0]],],dtype=np.uint8)
# 用matplotlib存储
plt.imsave('img_pyplot.jpg',img)
x = np.arange(0 , 360)  
y = np.sin( x * np.pi / 180.0)  
plt.plot(x,y)  
plt.xlim(0,360)  
plt.ylim(-1.2,1.2)  
plt.title("SIN function")  
plt.show() 


print('=================')

print(fun1(9,10))



# 用opencv存储
# cv2.imwrite('img_cv2.jpg',img)

# colorImg = cv2.imread('img_cv2.jpg')

# print(colorImg.shape)