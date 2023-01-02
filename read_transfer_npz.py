# import numpy as np
# from PIL import Image
# import matplotlib.pyplot as plt
#
# # 以下分别为读取nii和npz格式病理图片的方式
# # 读取nii格式病理图片
# import torchio as tio
# t1_path = 'MICCAI_BraTS2020_TrainingData/BraTS20_Training_001/BraTS20_Training_001_t1ce.nii'
# t1_img = tio.ScalarImage(t1_path)
# t1_img.plot()
# t2 = np.asarray(t1_img)  # 将图片转化为ndarray对象
# # 读取npz格式病理图片（从数组转化为图片）
# data = np.load('data/train/atlas_vol.npz')
# # img = Image.fromarray(data['vol_data'][154])  # fromarray方法从矩阵中读取图片
# # img.show()
# plt.imshow(data['vol_data'][66])
# plt.show()

import skimage.transform as skTrans
import nibabel as nib
im = nib.load('MICCAI_BraTS2020_TrainingData/BraTS20_Training_001/BraTS20_Training_001_t1ce.nii').get_fdata()
result1 = skTrans.resize(im, (160,160,130), order=1, preserve_range=True)

# 批量转化nii为npz格式
# 此方法可以直接读取文件夹中的所有flair t1 t1_ce t2 seg等nii文件然后直接转换为npz文件
import os
import sys
import numpy as np
import SimpleITK as sitk
import skimage.transform as skTrans
import nibabel as nib

NII_DIR = 'MICCAI_BraTS2020_TrainingData/BraTS20_Training_001'
outPutDir = 'npz_file/'


def get_filelist(dir, Filelist):
    if os.path.isdir(dir):
        for s in os.listdir(dir):
            new = os.path.join(dir, s)
            Filelist.append(new)

    return Filelist


nii_list = get_filelist(NII_DIR, [])
print(len(nii_list))

for e in nii_list:
    Refimg = sitk.ReadImage(e)
    RefimgArray = sitk.GetArrayFromImage(Refimg)
    fileName = e.split('\\')[-1].replace('nii', 'npz')
    filename = fileName.split('.')[0]
    short = filename.split('_')[3]
    if short != 'seg':
        # 若要reshape医学图像的体素大小 退注释下面的语句 并将vol_data设置为reshaped
        # im = nib.load(e).get_fdata()
        # reshaped = skTrans.resize(im, (160, 192, 224), order=1, preserve_range=True)
        np.savez(outPutDir + filename + '_vol.npz', vol_data=RefimgArray)
    else:
        # 为每个模态的切片单独创建对应的_seg.npz标签【因四个模态的标签分割标签一致】
        for file in nii_list:
            # 因_seg.npz文件需要对应每个模态生成 故单独的_seg.nii暂无意义 无需生成.npz文件
            if not file.endswith('_seg.nii'):
                file_name = file.split('\\')[-1].replace('nii', 'npz')
                file_name = file_name.split('.')[0]
                np.savez(outPutDir + file_name + '_seg.npz', seg_data=RefimgArray)


