import numpy as np
import tifffile as tiff
print("hello")
FILE_cadastral2015 = './20170907_hint/cadastral2015.tif'
FILE_tinysample = './20170907_hint/tinysample.tif'

im_tiny = tiff.imread(FILE_tinysample)
im_cada = tiff.imread(FILE_cadastral2015)

im_tiny.shape
im_cada.shape

result_temp = np.zeros(im_cada.shape, dtype=np.uint8)
result_temp.shape
for i in range(len(im_tiny)):
  for j in range(len(im_tiny[0])):
    if im_tiny[i][j][0] > 0:
      result_temp[i][j] = 1
print(result_temp)
print(sum([sum(item) for item in result_temp]))
tiff.imsave('./result/result_temp.tiff', result_temp)
