import cv2
import glob

img_array = []
for i in range(len(glob.glob('/Users/qilong/Desktop/AFRAID_1372/vis/*.png'))):
    filename = '/Users/qilong/Desktop/AFRAID_1372/vis/' + str(i) + '.png'
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)

out = cv2.VideoWriter('AFRAID_1372.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 21, size)


for i in range(len(img_array)):
    out.write(img_array[i])
out.release()