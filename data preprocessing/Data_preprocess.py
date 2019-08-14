#!/usr/bin/env python
# coding: utf-8

# In[1]:


import imageio
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from resizeimage import resizeimage


# In[2]:


os.chdir('/Users/yunbaizhang/Desktop')


# In[ ]:


### Reduce the noise and Remove "hat" class

for k in range(152):
    seg  = imageio.imread('resized_video_results/'+str(k)+'.png')
    seg = np.array(seg)
    for i in range(512):
        for j in range(512):
            if seg[i,j] == 14:
                seg[i,j] = 0
            if (i >= 430 and j >= 220 and j <= 400):
                if seg[i,j] == 1:
                    seg[i,j] = 17
            if (i>= 450 and j >=210 and j <= 420):
                if seg[i,j] == 0:
                    seg[i,j] = 17
    seg = Image.fromarray(seg)
    seg.save('updated_segmentation/'+str(k)+'.png') 
    
    
## Detect the misclassification skin
#im = np.array(im)
#print("The classification is skin \n")
#for i in range(512):
    #for j in range(512):
        #if im[i,j] == 1:
            #print('It is in the position %d, %d.'% (i,j))
            
### Slightly change some of the noise

for k in range(7):
    seg  = imageio.imread('updated_segmentation/'+str(k)+'.png')
    seg = np.array(seg)
    for i in range(512):
        for j in range(512):
            if (i>= 410 and i <= 450 and j >=200 and j <= 400):
                if seg[i,j] == 1:
                    seg[i,j] = 17
    seg = Image.fromarray(seg)
    seg.save('updated_segmentation/'+str(k)+'.png') 

    


# In[12]:


### Change the background in snow-white
for i in range(152):
    origin  = imageio.imread('video_stuff_3/'+str(i)+'.jpg') 
    seg  = imageio.imread('updated_segmentation/'+str(i)+'.png')
    seg,origin = np.array(seg), np.array(origin)
    for j in range(512):
        for k in range(512):
            ## Check every pixel, if the label of it is 0, then color the original image in black
            if seg[j,k] == 0:
                origin[j,k] = [255,250,250]
    origin = Image.fromarray(origin)
    origin.save('updated_original_image/'+str(i)+'.jpg')
                
    


# In[4]:


## Remove hair noise at right-buttom corner 
for k in range(152):
    seg = imageio.imread('SPADE_image_0813/'+str(k)+'.png')
    seg = np.array(seg)
    for i in range(150,256):
        for j in range(200,256):
            if seg[i,j] == 13:
                seg[i,j] = 0
    seg = Image.fromarray(seg)            
    seg.save('SPADE_image_0813/'+str(k)+'.png')


# In[5]:


## Remove hair noise at left-buttom corner
for k in range(50,132):
    seg = imageio.imread('SPADE_image_0813/'+str(k)+'.png')
    seg = np.array(seg)
    for i in range(130,256):
        for j in range(0,80):
            if seg[i,j] == 13:
                seg[i,j] = 0
    seg = Image.fromarray(seg)
    seg.save('SPADE_image_0813/'+str(k)+'.png')
    
      
    


# In[8]:


### Change the background in snow-white
for i in range(152):
    origin  = imageio.imread('Spade_image_256/'+str(i)+'.png') 
    seg = imageio.imread('SPADE_image_0813/'+str(i)+'.png')
    seg,origin = np.array(seg), np.array(origin)
    for j in range(256):
        for k in range(256):
            ## Check every pixel, if the label of it is 0, then color the original image in black
            if seg[j,k] == 0:
                origin[j,k] = [255,250,250]
    origin = Image.fromarray(origin)
    origin.save('cleaned_spade_image/'+str(i)+'.jpg')
                
    


# In[ ]:




