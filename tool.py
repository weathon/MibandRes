from PIL import Image
import os
import numpy as np

mypath=input("将素材文件夹拖到这里(如果有引号要去掉):")
files=os.listdir(mypath)
r,g,b=input("输入纯色颜色rgb(空格隔开):").split(" ")

for i in files:
    im = Image.open(mypath+"/"+i)
    print("正在处理"+i)
    img = np.asarray(im)
    for x in img.shape[0]:
        for y in img.shape[1]:
            myavg=(img[x,y,0]+img[x,y,1]+img[x,y,2])/3
            img[x,y]=(
                myavg*(r/256),
                myavg*(g/256),
                myavg*(b/256),
                img[x,y,3]
            )
    Image.fromarray(np.uint8(img)).save(mypath+"/"+i)
