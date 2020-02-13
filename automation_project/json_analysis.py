#coding:utf-8

import jsonpath
import json
import time
import uuid

def run(js_path, s, g_t, vk, tk, c_o, txt_path):
    '''
    传入json路径:param js_path:
    传入idcard和phone_no:param s:
    传入查询日期:param g_t:
    传入需要输出的value对应的key,当输入方式为'key,'，将key作为单独的一列输出,当输入方式为'key,,x'，当解析的key没有value时，用多少个''来表示:param vk:
    传入按行输出还是按列输出(0：按行；1：按列):param c_o:
    输出文件路径:param txt_path:
    传入需要解析的类(默认为None):param tk:
    '''
    data = []  # 用于装载需要获取的value
    with open(js_path, 'r', encoding='utf-8')as r:
        json_str = r.read()  # 根据json_path将json数据读取出来type(str)

    json_ = json.loads(json_str)  # 将str类型的json数据转化为dict类型
    # print(type(tk))

    #进行绝对路径解析Json
    '''
    strs : 待解析的绝对路径
    
    '''
    for i in range(len(tk)):
        strs = '$.'
        for k in tk[i]:
            kt = k.split(',')
            if kt[-1] == '[':
                strs += '%s[*].' % kt[0]
            else:
                strs += '%s.' % kt[0]
        for j in vk[i]:
            s_j = j.split(',')
            jp = strs+s_j[0]
            if len(s_j) == 1:
                v_l = jsonpath.jsonpath(json_, jp)
                for i in range(len(v_l)):
                    if v_l[i] == '':
                        v_l[i] = r'\N'
                data.append(v_l)
            elif len(s_j) == 2:
                k_l = []
                v_l = jsonpath.jsonpath(json_, jp)
                for i in range(len(v_l)):
                    if v_l[i] == '':
                        v_l[i] = r'\N'
                for v in v_l:
                    k_l.append(s_j[0])
                data.append(k_l)
                data.append(v_l)
            else:
                v_l = jsonpath.jsonpath(json_, jp)
                if v_l == False:
                    lost_l = []
                    for k in range(int(s_j[-1])):
                        lost_l.append(r'\N')
                    data.append(lost_l)
                else:
                    for i in range(len(v_l)):
                        if v_l[i] == '':
                            v_l[i] = r'\N'
                    data.append(v_l)

    # ===========测试区域==============
    # 将数据输出
    # for j in data:
    #     print(j)
    # ================================

    '''
    准备将获取到的写入txt

    strs : 将数据以csv格式存储为str方便后面写入文件
    data_size : 在0.0.2之后被取消(没有考虑一个key对应多个v的情况)
    data_max_size : 数据长度最长(解决了当一个key对应多个v的情况)
    '''
    id_card = jsonpath.jsonpath(json_, '$..user_id')
    if id_card == False:
        id_card = r'\N'
    else:
        id_card = id_card[0]

    if c_o == 1:
        # data_size = len(data[0])
        data_max_size = -1
        for i in data:
            if len(i) > data_max_size:
                data_max_size = len(i)

        for i in range(data_max_size):
            strs = str(uuid.uuid1()).replace('-', '') + '\t' + id_card + '\t' + s
            for j in data:
                if i > len(j)-1:
                    strs += str(j[len(j)-1]).replace('\t', ' ') + '\t'
                else:
                    strs += str(j[i]).replace('\t', ' ') + '\t'

            strs += str(g_t + '\t' + str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
            #将读取好的一条数据追加到txt文件中
            with open(txt_path,'a+',encoding='utf-8')as f:
                f.write(strs + '\n')
            # 输出测试
            print(strs)
    else:
        for i in data:
            strs = str(uuid.uuid1()).replace('-', '') + '\t' + id_card + '\t' + s
            for j in i:
                strs += str(j).replace('\t', ' ') + '\t'
            strs += str(g_t + '\t' + str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
            #将读取好的一条数据追加到txt文件中
            with open(txt_path,'a+',encoding='utf-8')as f:
                f.write(strs + '\n')
            # 输出测试
            print(strs)

