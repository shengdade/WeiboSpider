# -*-coding:gbk-*-
import codecs
import os
import re
import traceback

import requests
from lxml import etree


class Weibo:
    with open('cookie') as f:
        c = f.read()
    cookie = {"Cookie": c}  # ��your cookie�滻���Լ���cookie

    # weibo���ʼ��
    def __init__(self, weibo_id, weibo_filter=0):
        self.user_id = weibo_id  # �û�id������Ҫ������������֣����ǳ�Ϊ��Dear-�����Ȱ͡���idΪ1669879400
        self.filter = weibo_filter  # ȡֵ��ΧΪ0��1������Ĭ��ֵΪ0������Ҫ��ȡ�û���ȫ��΢����1����ֻ��ȡ�û���ԭ��΢��
        self.userName = ""  # �û������硰Dear-�����Ȱ͡�
        self.weiboNum = 0  # �û�ȫ��΢����
        self.weiboNum2 = 0  # ��ȡ����΢����
        self.following = 0  # �û���ע��
        self.followers = 0  # �û���˿��
        self.weibos = []  # ΢������
        self.num_zan = []  # ΢����Ӧ�ĵ�����
        self.num_forwarding = []  # ΢����Ӧ��ת����
        self.num_comment = []  # ΢����Ӧ��������

    # ��ȡ�û��ǳ�
    def get_user_name(self):
        try:
            url = 'http://weibo.cn/%d/info' % self.user_id
            html = requests.get(url, cookies=Weibo.cookie).content
            selector = etree.HTML(html)
            user_name = selector.xpath("//title/text()")[0]
            self.userName = user_name[:-3]
        # print '�û��ǳƣ�' + self.userName
        except Exception as e:
            print("Error: ", e)
            traceback.print_exc()

    # ��ȡ�û�΢��������ע������˿��
    def get_user_info(self):
        try:
            url = 'http://weibo.cn/u/%d?filter=%d&page=1' % (self.user_id, self.filter)
            html = requests.get(url, cookies=Weibo.cookie).content
            selector = etree.HTML(html)
            pattern = r"\d+\.?\d*"

            # ΢����
            num_wb = 0
            str_wb = selector.xpath("//div[@class='tip2']/span[@class='tc']/text()")[0]
            guid = re.findall(pattern, str_wb, re.S | re.M)
            for value in guid:
                num_wb = int(value)
                break
            self.weiboNum = num_wb
            # print '΢����: ' + str(self.weiboNum)

            # ��ע��
            str_gz = selector.xpath("//div[@class='tip2']/a/text()")[0]
            guid = re.findall(pattern, str_gz, re.M)
            self.following = int(guid[0])
            # print '��ע��: ' + str(self.following)

            # ��˿��
            str_fs = selector.xpath("//div[@class='tip2']/a/text()")[1]
            guid = re.findall(pattern, str_fs, re.M)
            self.followers = int(guid[0])
        # print '��˿��: ' + str(self.followers)
        except Exception as e:
            print("Error: ", e)
            traceback.print_exc()

    # ��ȡ�û�΢�����ݼ���Ӧ�ĵ�������ת������������
    def get_weibo_info(self):
        try:
            url = 'http://weibo.cn/u/%d?filter=%d&page=1' % (self.user_id, self.filter)
            html = requests.get(url, cookies=Weibo.cookie).content
            selector = etree.HTML(html)
            if not selector.xpath('//input[@name="mp"]'):
                page_num = 1
            else:
                page_num = int(selector.xpath('//input[@name="mp"]')[0].attrib['value'])
            pattern = r"\d+\.?\d*"
            for page in range(1, page_num + 1):
                url2 = 'http://weibo.cn/u/%d?filter=%d&page=%d' % (self.user_id, self.filter, page)
                html2 = requests.get(url2, cookies=Weibo.cookie).content
                selector2 = etree.HTML(html2)
                info = selector2.xpath("//div[@class='c']")
                # print len(info)
                if len(info) > 3:
                    for i in range(0, len(info) - 2):
                        self.weiboNum2 += 1
                        # ΢������
                        str_t = info[i].xpath("div/span[@class='ctt']")
                        weibos = str_t[0].xpath('string(.)').encode('gbk', 'ignore')
                        weibos = str(weibos.decode('gbk', 'ignore'))
                        self.weibos.append(weibos)
                        # print '΢�����ݣ�'+ weibos
                        # ������
                        str_zan = info[i].xpath("div/a/text()")[-4]
                        guid = re.findall(pattern, str_zan, re.M)
                        num_zan = int(guid[0])
                        self.num_zan.append(num_zan)
                        # print '������: ' + str(num_zan)
                        # ת����
                        forwarding = info[i].xpath("div/a/text()")[-3]
                        guid = re.findall(pattern, forwarding, re.M)
                        num_forwarding = int(guid[0])
                        self.num_forwarding.append(num_forwarding)
                        # print 'ת����: ' + str(num_forwarding)
                        # ������
                        comment = info[i].xpath("div/a/text()")[-2]
                        guid = re.findall(pattern, comment, re.M)
                        num_comment = int(guid[0])
                        self.num_comment.append(num_comment)
                        # print '������: ' + str(num_comment)
            if self.filter == 0:
                print('��' + str(self.weiboNum2) + '��΢��')
            else:
                print('��' + str(self.weiboNum) + '��΢��������' + str(self.weiboNum2) + '��Ϊԭ��΢��')
        except Exception as e:
            print("Error: ", e)
            traceback.print_exc()

    # ������
    def start(self):
        try:
            Weibo.get_user_name(self)
            Weibo.get_user_info(self)
            Weibo.get_weibo_info(self)
            print('��Ϣץȡ���')
            print('===========================================================================')
        except Exception as e:
            print("Error: ", e)

            # ����ȡ����Ϣд���ļ�

    def write_txt(self):
        try:
            if self.filter == 1:
                result_header = '\n\nԭ��΢�����ݣ�\n'
            else:
                result_header = '\n\n΢�����ݣ�\n'
            result = '�û���Ϣ\n�û��ǳƣ�' + self.userName + '\n�û�id��' + str(self.user_id) + '\n΢������' + str(
                self.weiboNum) + '\n��ע����' + str(self.following) + '\n��˿����' + str(self.followers) + result_header
            for i in range(1, self.weiboNum2 + 1):
                text = str(i) + ':' + self.weibos[i - 1] + '\n' + '��������' + str(self.num_zan[i - 1]) + '	 ת������' + str(
                    self.num_forwarding[i - 1]) + '	 ��������' + str(self.num_comment[i - 1]) + '\n\n'
                result += text
            if not os.path.isdir('weibo'):
                os.mkdir('weibo')
            f = codecs.open("weibo/%s.txt" % self.user_id, "w", 'gbk')
            f.write(result)
            f.close()
            file_path = os.getcwd() + "\weibo" + "\%d" % self.user_id + ".txt"
            print('΢��д���ļ���ϣ�����·��%s' % file_path)
        except Exception as e:
            print("Error: ", e)
            traceback.print_exc()


# ʹ��ʵ��,����һ���û�id��������Ϣ����洢��wbʵ����
user_id = 1729370543  # ���Ըĳ�����Ϸ����û�id�������΢��id���⣩
user_filter = 1  # ֵΪ0��ʾ��ȡȫ����΢����Ϣ��ԭ��΢��+ת��΢������ֵΪ1��ʾֻ��ȡԭ��΢��
wb = Weibo(user_id, user_filter)  # ����weibo�࣬����΢��ʵ��wb
wb.start()  # ��ȡ΢����Ϣ
print('�û�����' + wb.userName)
print('ȫ��΢������' + str(wb.weiboNum))
print('��ע����' + str(wb.following))
print('��˿����' + str(wb.followers))
print('����һ��΢��Ϊ��' + wb.weibos[0])  # ��filter=1��Ϊ���µ�ԭ��΢����������û�΢����Ϊ0����len(wb.weibos)==0,��ӡ�������ͬ
print('����һ��΢����õĵ�������' + str(wb.num_zan[0]))
print('����һ��΢����õ�ת������' + str(wb.num_forwarding[0]))
print('����һ��΢����õ���������' + str(wb.num_comment[0]))
wb.write_txt()  # wb.writeTxt()ֻ�ǰ���Ϣд���ļ����ҿ��Ը����Լ�����Ҫ���±�дwriteTxt()����
