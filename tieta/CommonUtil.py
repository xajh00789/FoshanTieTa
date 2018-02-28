#coding:utf8
# uncompyle6 version 2.14.3
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.5.4 (v3.5.4:3f56838, Aug  8 2017, 02:17:05) [MSC v.1900 64 bit (AMD64)]
# Embedded file name: D:\cppy\code\CommonUtil.py
# Compiled at: 2017-09-11 13:20:57
# Size of source mod 2**32: 986 bytes
import time
from io import BytesIO
import pytesseract, base64, xlrd, time, os

def waitDownAndRename(原文件, 重命名文件, timeout=600):
    for i in range(timeout):
        if os.path.exists(原文件):
            time.sleep(1)
            os.rename(原文件, 重命名文件)
            time.sleep(1)
            print('重命名成功！\n')
            try:
                data = xlrd.open_workbook(重命名文件)
                break
            except xlrd.biffh.XLRDError:
                print('Excel文件读取出错！')
                os.rename(重命名文件, 原文件 + '.Error')
                break

        else:
            print('文件或目录不存在！\n')
            time.sleep(1)
# okay decompiling CommonUtil.pyc
