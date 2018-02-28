import os

def  check_whether_all_download(path):
    unDownload_exist = True
    while (unDownload_exist == True):
        unDownload_exist = False
        for filename in os.listdir(path):
            if os.path.splitext(filename)[1] == '.crdownload':
                print(filename)
                unDownload_exist = True


path = 'E:\迅雷下载\铁塔图片\临时图片3\\'

check_whether_all_download(path)
