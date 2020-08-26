# -*- encoding: utf-8 -*-

'''
@Author  :  leoqin

@Contact :  qcs@stu.ouc.edu.cn

@Software:  Pycharm

@Time    :  May 24,2019

@Desc    :  实现翻译的爬虫功能

'''

import urllib.request
import urllib.parse
import json
import requests  # pip intasll requests
import execjs  # 安装指令：pip install PyExecJS
import random
import hashlib

from googletrans import Translator


class Py4Js():

    def __init__(self):
        self.ctx = execjs.compile(""" 
        function TL(a) { 
        var k = ""; 
        var b = 406644; 
        var b1 = 3293161072; 

        var jd = "."; 
        var $b = "+-a^+6"; 
        var Zb = "+-3^+b+-f"; 

        for (var e = [], f = 0, g = 0; g < a.length; g++) { 
            var m = a.charCodeAt(g); 
            128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023), 
            e[f++] = m >> 18 | 240, 
            e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224, 
            e[f++] = m >> 6 & 63 | 128), 
            e[f++] = m & 63 | 128) 
        } 
        a = b; 
        for (f = 0; f < e.length; f++) a += e[f], 
        a = RL(a, $b); 
        a = RL(a, Zb); 
        a ^= b1 || 0; 
        0 > a && (a = (a & 2147483647) + 2147483648); 
        a %= 1E6; 
        return a.toString() + jd + (a ^ b) 
    }; 

    function RL(a, b) { 
        var t = "a"; 
        var Yb = "+"; 
        for (var c = 0; c < b.length - 2; c += 3) { 
            var d = b.charAt(c + 2), 
            d = d >= t ? d.charCodeAt(0) - 87 : Number(d), 
            d = b.charAt(c + 1) == Yb ? a >>> d: a << d; 
            a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d 
        } 
        return a 
    } 
    """)

    def getTk(self, text):
        return self.ctx.call("TL", text)


# 有道翻译方法，不支持一次翻译一大段文字
def youdao_translate(content):
    '''实现有道翻译的接口'''
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom=https://www.baidu.com/link'
    data = {
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '1500092479607',
        'sign': 'd9f9a3aa0a7b34241b3fe30505e5d436',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CL1CKBUTTON',
        'typoResult': 'true'}
    data['i'] = content.replace('\n', '')
    data = urllib.parse.urlencode(data).encode('utf-8')
    wy = urllib.request.urlopen(url, data)
    html = wy.read().decode('utf-8')
    ta = json.loads(html)
    res = ta['translateResult'][0][0]['tgt']
    return res


# 谷歌翻译方法
def google_translate(content):
    '''实现谷歌的翻译'''
    content = content.replace('\n', '')
    trans = Translator(service_urls=["translate.google.cn"])
    res = trans.translate(content, dest='zh-cn').text

    return res


def is_Chinese(content):  # 判断输入的内容是否是中文
    for ch in content:
        if '\u4e00' <= ch <= '\u9fff':
            return True
        else:
            return False

# 必应翻译方法已废弃
def bing_translate(content): # 尽量保证翻译内容既有中文也有英文的情况，判断没考虑此情况。
    if len(content) > 4891:
        return '输入请不要超过4891个字符！'
    url = 'https://www.bing.com/ttranslatev3?isVertical=1&&IG=0AF741D4794D421EB417BC51A62B9934&IID=translator.5026.4'
    if is_Chinese(content):
        res = requests.post(url, data={'text':content.replace('\n',''), 'from': 'zh-CHS', 'to': "en", 'doctype': 'json'}).json()['translationResponse']
    else:
        res = requests.post(url, data={'text':content.replace('\n',''), 'from': 'en', 'to': "zh-CHS", 'doctype': 'json'}).json()['translationResponse']
    return res

# 百度翻译方法
def baidu_translate(content):
    print(content)
    if len(content) > 4891:
        return '输入请不要超过4891个字符！'
    salt = str(random.randint(0, 50))
    # 申请网站 http://api.fanyi.baidu.com/api/trans
    appid = '20191210000364718' # 这里写你自己申请的
    secretKey = 'e83BXpQFTnXrTy62O9MO'# 这里写你自己申请的
    sign = appid + content + salt + secretKey
    sign = hashlib.md5(sign.encode(encoding='UTF-8')).hexdigest()
    head = {'q': f'{content}',
            'from': 'en',
            'to': 'zh',
            'appid': f'{appid }',
            'salt': f'{salt}',
            'sign': f'{sign}'}
    j = requests.get('http://api.fanyi.baidu.com/api/trans/vip/translate', head)
    print(j.json())
    res = j.json()['trans_result'][0]['dst']
    print(res)
    return str(res)
