import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# 以下分别为读取nii和npz格式病理图片的方式
# 读取nii格式病理图片
import torchio as tio
t1_path = 'BraTS19_2013_2_1//BraTS19_2013_2_1_flair.nii'
t1_img = tio.ScalarImage(t1_path)
# t1_img.plot()
t2 = np.asarray(t1_img)  # 将图片转化为ndarray对象
# 读取npz格式病理图片（从数组转化为图片）
data = np.load('data/train/BraTS19_vol.npz')
img = Image.fromarray(data['vol_data'][1])
# img.show()
plt.imshow(data['vol_data'][1])  # imshow方法从矩阵中读取图片
plt.show()

# 批量转化nii为npz格式
# import os
#
# import numpy as np
# import SimpleITK as sitk
#
# NII_DIR = 'HGG/BraTS19_2013_2_1/'
#
#
# def get_filelist(dir, Filelist):
#     if os.path.isdir(dir):
#
#         for s in os.listdir(dir):
#             newDir = os.path.join(dir, s)
#             Filelist.append(newDir)
#
#     return Filelist
#
#
# list = get_filelist(NII_DIR, [])
# print(len(list))
#
# for e in list:
#     Refimg = sitk.ReadImage(e)
#     RefimgArray = sitk.GetArrayFromImage(Refimg)
#     fileName = e.split('\\')[-1]
#     fileName = fileName.replace('nii', 'npz')
#     filename = fileName.split('/')[2]
#     outPutDir = 'npz_file/'
#     np.savez(outPutDir + filename, vol_data=RefimgArray)
