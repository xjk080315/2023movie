import requests
import re

f = open('2023必看热片及下载地址.txt', mode='w', encoding='utf-8')

print('正在获取数据...')

url_1 = 'https://dy2018.com/'
resp_1 = requests.get(url_1)
resp_1.encoding = 'gbk'
text_1 = resp_1.text

obj_1 = re.compile(r"2023必看热片.*?<ul>(?P<page_1>.*?)</ul>", re.S)
result_1 = obj_1.search(text_1)
page_1 = result_1.group('page_1')

obj_2 = re.compile(r"<li><a href='(?P<url_2>.*?)' title", re.S)
obj_3 = re.compile(r'<div id="Zoom">.*?片　　名(?P<name>.*?)<br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">', re.S)
result_2 = obj_2.finditer(page_1)

print('获取成功,正在写入数据...')
print('进度:', end='')

for item in result_2:
    url_2 = 'https://dy2018.com' + item.group('url_2')
    resp_2 = requests.get(url_2)
    resp_2.encoding = 'gbk'
    text_2 = resp_2.text
    result_3 = obj_3.search(text_2)
    result_end_1 = result_3.group('name').strip()
    result_end_2 = result_3.group('download')
    # print(result_end_1, '----', result_end_2)
    f.write(f'《{result_end_1}》----{result_end_2}\n')
    print('-', end='')
print('完成！')