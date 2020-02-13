#coding:utf-8

import os

def GetFileList(dir, fileList):
    '''

    传入路径:param dir:
    传入数组用于存储路径下的所以文件路径:param fileList:
    返回该路径下所有文件的路径:return:
    '''
    if os.path.isfile(dir):
        fileList.append(dir)
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir = os.path.join(dir, s)
            GetFileList(newDir, fileList)
        return fileList

