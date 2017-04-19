# -*- coding:UTF-8 -*-

import requests
import re
import codecs
import csv
import time
from lxml import html

import sys
reload(sys)
sys.setdefaultencoding('utf8')



# 获取大量ip地址，保存本地
def get_iplist(fname):
    ip_url = 'http://proxydb.net/?offset='
    headers = {
        'Host': 'proxydb.net',
        'Referer': 'http://proxydb.net/?',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'
    }
    for i in range(1, 100):

        url = ip_url + str(i*50)
        res = requests.get(url, headers=headers)
        print res.url, res.status_code

        for ip in re.findall(r'<a href=.*?>(\d+.\d+.\d+.\d+\:\d+)</a>', res.text, re.S):

            with open(fname+'.txt', 'a') as f:
                f.write(ip + '\n')
            print u'抓到一个ip:', ip

        time.sleep(2)


# 获取个人信息
def get_contents(proxy):
    per_list = []
    url = 'http://www.haoweichi.com/Index/random'
    headers = {
        'Host': 'www.haoweichi.com',
        'Referer': 'http://www.haoweichi.com/Index/random',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'
    }
    pagehtml = requests.get(url, proxies=proxy, headers =headers, timeout=3)
    tree = html.fromstring(pagehtml.text)
    tb = tree.xpath('//div[@class="row no-margin"]//input')
    for p in tb:
        p = re.sub('\n', '',p.value).strip()
        per_list.append(p)
    return per_list


# 将信息写入本地文件csv
def write_data(contents):
        with open('contents.csv', 'ab') as csvfile :
            csvfile.write(codecs.BOM_UTF8)
            spamwriter = csv.writer(csvfile, dialect='excel')
            spamwriter.writerow(contents)


# 遍历本地文件的ip地址，代理去访问url抓取信息
def fetch(ip_file):
    list_head = [u'全名', u'性别', 'Firstname', 'Lastname', 'Middle name', u'称呼', u'生日', u'州', u'街道地址', u'城市', u'电话', u'邮编', u'州全称', u'SSN社会保险号', u'网络用户名', u'随机密码', u'信用卡类型', u'信用卡号', 'CVV2', u'有效期', u'职位（职称）', u'所属公司', u'身高', u'体重']
    write_data(list_head)
    f = open(ip_file + '.txt', 'r')
    

    for ip in iter(f):
        proxy = {'http': ip.strip()}
        while True:
            try:
                contents = get_contents(proxy)
                print ip,'\n', u'正在保存第个人的信息:', contents
                if contents == []:
                    break
                write_data(contents)
            except Exception as e:
                print u'无效的ip：', ip, e
                break


def start():
    fname = 'iplist2'
    get_iplist(fname)
    fetch(fname)
    print u'成功保存数据到contents.csv'

if __name__ == '__main__':
    start()