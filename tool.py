from PIL import Image
import os
import numpy as np

mypath=input("将素材文件夹拖到这里(如果有引号要去掉,会覆盖源文件):")
files=os.listdir(mypath)
r,g,b=input("输入纯色颜色rgb(空格隔开):").split(" ")
r=int(r)
g=int(g)
b=int(b)

for i in files:
    try:
        im = Image.open(mypath+"/"+i)
        print("正在处理 "+i)
        img = im.load()
        # img.flags.writeable = True
        # print(im.size)
        # print(img[0,0])
        for x in range(im.size[0]):
            for y in range(im.size[1]):
                myavg=(img[x,y][0]+img[x,y][1]+img[x,y][2])/3
                tr=img[x,y][3]
                img[x,y]=(
                    int(myavg*(r/256)),
                    int(myavg*(g/256)),
                    int(myavg*(b/256)),#整除
                    tr
                )
                # print(img[x,y])
        im.save(mypath+"/"+i)
    except:
        print("处理"+i+"时失败")
print("完成")