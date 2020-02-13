# coding:utf-8

from hdfs import *

def put_file(node_name,hdfs_path,txt_path):

    timeout = 100

    url = 'http://%s:50070' % node_name

    client = Client(url,timeout=timeout)

    client.upload(hdfs_path,txt_path,overwrite=True)

    print('==============上传成功===============')