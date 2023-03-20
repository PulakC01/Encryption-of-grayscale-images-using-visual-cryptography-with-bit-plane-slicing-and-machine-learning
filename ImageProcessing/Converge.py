import cv2
import numpy as np
# Function to convert unit8 image to bitstream array
def int2bitarray(img):
    arr = []
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            arr.append(np.binary_repr(img[i][j], width=8))
    return arr
# read image convert to bit stream
img0 = cv2.imread('./output_1.png',0)//255
img1 = cv2.imread('./output_2.png',0)//255
img2 = cv2.imread('./output_3.png',0)//255
img3 = cv2.imread('./output_4.png',0)//255
img4 = cv2.imread('./output_5.png',0)//255
img5 = cv2.imread('./output_6.png',0)//255
img6 = cv2.imread('./output_7.png',0)//255
img7 = cv2.imread('./output_8.png',0)//255
res67 = np.zeros((img0.shape))
res567 = np.zeros((img0.shape))
res4567 = np.zeros((img0.shape))
res34567 = np.zeros((img0.shape))
res234567 = np.zeros((img0.shape))
res1234567 = np.zeros((img0.shape))
res01234567 = np.zeros((img0.shape))
# save grayscale
for i in range(img0.shape[0]):
    for j in range(img0.shape[1]):
        res67[i,j] = img6[i,j]<<6|img7[i,j]<<7
        res567[i,j] = img5[i,j]<<5|img6[i,j]<<6|img7[i,j]<<7
        res4567[i,j] = img4[i,j]<<4|img5[i,j]<<5|img6[i,j]<<6|img7[i,j]<<7
        res34567[i,j] = img3[i,j]<<3|img4[i,j]<<4|img5[i,j]<<5|img6[i,j]<<6|img7[i,j]<<7
        res234567[i,j] = img2[i,j]<<2|img3[i,j]<<3|img4[i,j]<<4|img5[i,j]<<5|img6[i,j]<<6|img7[i,j]<<7
        res1234567[i,j] = img1[i,j]<<1|img2[i,j]<<2|img3[i,j]<<3|img4[i,j]<<4|img5[i,j]<<5|img6[i,j]<<6|img7[i,j]<<7
        res01234567[i,j] = img0[i,j]|img1[i,j]<<1|img2[i,j]<<2|img3[i,j]<<3|img4[i,j]<<4|img5[i,j]<<5|img6[i,j]<<6|img7[i,j]<<7

cv2.imwrite('./Output_Image.png',res01234567)
print('done!')
