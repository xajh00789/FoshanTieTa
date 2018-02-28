import shutil
import os
import random
#    lujing = r'C:\Users\xiaoxiong\Desktop\oracle\下载图片\下载图片\下载的图片\站点' + str(zhandian)

def move_Photo(lujing):
    old=r'E:\迅雷下载\铁塔图片\临时图片3'
    new=lujing+'\\图片'
    if os.path.exists(new):
        num=random.randint(1,100)
        new=new+str(num)
    os.renames(old,new)

