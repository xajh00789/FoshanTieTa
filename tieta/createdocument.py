import os

def create_document(zhandian):
    lujing = r'E:\迅雷下载\铁塔图片\下载的图片3\站点' + str(zhandian)
    if os.path.exists(lujing): #如果创建的文件路径存在
        if not os.listdir(lujing): #创建文件夹路径前路径已经存在且不含有任何文件
            return lujing
    else:                    #如果创建的文件夹路径不存在创建文件夹
        os.mkdir(lujing)

    return lujing