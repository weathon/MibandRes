from PIL import Image
import os
import numpy as np

mypath=input("将素材文件夹拖到这里(如果有引号要去掉):")
files=os.listdir(mypath)
r,g,b=input("输入纯色颜色rgb(空格隔开):").split(" ")
r=int(r)
g=int(g)
b=int(b)

for i in files:
    im = Image.open(mypath+"/"+i)
    print("正在处理 "+i)
    img = im.load()
    # img.flags.writeable = True
    print(im.size)
    print(img[0,0])
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            myavg=(img[x,y][0]+img[x,y][1]+img[x,y][2])//3
            tr=img[x,y][3]
            img[x,y]=(
                myavg*(r//256),
                myavg*(g//256),
                myavg*(b//256),#整除
                tr
            )
    im.save(mypath+"/"+i)
