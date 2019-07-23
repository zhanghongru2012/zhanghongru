import configparser
import os

'''
1. ����ļ���������ȡconfig.ini�ļ��Ĺ�����
2. ������ReadConfig
3. ���ı�׼�⣺configparser
4. �漰����/������os��configparser��join
'''

# ���ȶ�ȡ��ǰ·����Ȼ�����õ�ǰ·��ȥƴ��config.ini�����·�����Ժ��Լ�д�ű�ʱ�򶼾���ʹ�����·��
now_dir = os.path.split(os.path.realpath(__file__))[0]
config_path = os.path.join(now_dir, "config.ini")


class ReadConfig:
    def __init__(self):
        # ��ʼ��configparser.ConfigParser()--->�ض���Ϊ cf������ʹ��
        self.cf = configparser.ConfigParser()
        self.cf.read(config_path)

    # ��ȡconfig.ini�ļ�
    def get_gonfig(self, section, key):
        '''
        :param section:config.ini�ļ�[]�еĲ���
        :param key: ��ѡsection�е��ֶ���
        :return: ����key��Ӧ���ֶ�ֵ
        '''
        values = self.cf.get(section, key)
        return values

    # д��config.ini�ļ��ķ���
    def set_config(self, section, key, value):
        '''

        :param section:ͬ�ϸ�����
        :param key: ͬ�ϸ�����
        :param value: ͬ�ϸ�����
        '''
        fb = open(config_path, 'w')
        self.cf.set(section, key, value)
        self.cf.write(fb)