# coding=gbk
import xlrd
import time
import json
import configparser
from Base.get_token import *
from Base.read_config import *

'''
1. ���ı�׼�⣺xlrd��requests��json
2. �漰֪ʶ�㣺xlrd��requests��json����д�ļ�
'''


def interface_check():
    # �趨�����õ��ļ�
    workbook = xlrd.open_workbook('../data/interface.xlsx')
    # �ҵ����ñ���е�sheet����
    interface_sheet = workbook.sheet_by_name('interfaces')
    # ��ȡ���������������������ﶼ��ֱ�Ӹ�ֵ�ˣ�û�й���ķ�����
    num_nows = interface_sheet.nrows
    num_cols = interface_sheet.ncols
    # ��������ͷ��Ԥ�����֣�һ�ִ�token��һ�ֲ���token
    headers_without_token = {'Content-Type': 'application/json'}
    headers_token = {'Content-Type': 'application/json', 'token': login()}
    # ��ȡ��config.ini�д�õ�host
    base_url = ReadConfig().get_gonfig("HTTP", "base_url")
    print(base_url)
    # ���Ĵ��룺����excel�еĽӿڲ���
    for i in range(1, num_nows):
        # ��һ�С��ӿ����ơ�
        interface_name = interface_sheet.row_values(i)[0]
        # �����С��ӿ�·����
        path = interface_sheet.row_values(i)[2]
        # ƴ�������ӿ�
        url = base_url + path
        # �����С��ӿڴ��Ρ�
        data = interface_sheet.row_values(i)[3]
        # �ھ��С��ӿ�����ʽ��
        method = interface_sheet.row_values(i)[8]

        # ����get��post����
        if method == "get":
            r = requests.get(url=url, params=data)
        else:
            r = requests.post(url=url, headers=headers_token, data=data)
        # ��������ķ���״ֵ̬�浵
        if json.dumps(r.status_code) == "200":
            with open('../log/log_success.txt', 'a') as f:
                print(i, ".", interface_name, file=f)
                print("�ӿ�����ʱ�䣺", time.ctime(), file=f)
                print("URL------->", url, file=f)
                print("RESPONSE-->", r.status_code, r.text, file=f)

        else:
            with open('../log/log_fail.txt', 'a') as f:
                print(i, ".", interface_name, file=f)
                print("�ӿ�����ʱ�䣺", time.ctime(), file=f)
                print("URL------->", url, file=f)
                print("RESPONSE-->", r.status_code, r.text, file=f)





