# coding:utf-8
# /usr/bin/env python

'''
Author: Wei Lu
date: 2019/5/10  14:23
desc:
'''

from super_json_for_mx_v_0_1_1.default.json_analysis import run
from super_json_for_mx_v_0_1_1.get_json_filepath import GetFileList

json_path = r'/json_data/mxCarrierData/'

all_info = []
with open('p_d.txt','r',encoding='utf-8')as f:
    lines = f.readlines()
    for i in lines:
        all_info.append(i.replace('\n','').split(','))

## mx_calls_info
#vk = ['time,,1','location,,1','fee,,1','details_id,,1','peer_number,,1','location_type,,1','duration,,1','dial_type,,1']
#tk = ['calls']

## mx_recharges_info
#vk = ['amount,,1','recharge_time,,1','type,,1']
#tk = ['recharges']

## mx_nets_info
#vk = ['time,,1','location,,1','fee,,1','subflow,,1','net_type,,1','service_name,,1']
#tk = ['nets']

## mx_smses_info
vk = ['time,,1','location,,1','fee,,1','peer_number,,1','send_type,,1','msg_type,,1','service_name,,1']
tk = ['smses']

for i in range(len(all_info)):
    info_path = json_path + all_info[i][0] + '/' + all_info[i][1]
    # print(info_path)
    try:
        data = GetFileList(info_path,[])
        for j in data:
            run(js_path=j,s=all_info[i][1]+'\t',g_t=all_info[i][0],vk=vk,c_o=1,txt_path='test.txt',tk=tk)
    except:
        print(info_path + '不存在')


# run函数改为super_json函数就可以不用那个s参数了 方便一点