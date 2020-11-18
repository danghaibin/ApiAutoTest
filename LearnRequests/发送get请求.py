'''
发送get请求
1. get请求带参数
   方法1：拼接到URL后面
   方法2：使用params传参数
2. get请求带请求头，比如设置User-Agent伪装成浏览器发送的请求，避免服务器屏蔽自动化发的请求。
'''

import requests

# 接口地址："http://www.baidu.com"
# 发送一个get请求，r是收到的响应
r = requests.get("http://www.baidu.com")
# 文本格式的响应内容
print(r.text)
# 响应码
print(r.status_code)
assert r.status_code == 200
# OK
print(r.reason)
assert r.reason == 'OK'

# 金融项目：获取用户列表
# 发送请求
url = "http://jy001:8081/futureloan/mvc/api/member/list"
r = requests.get(url)
print(r.text)
# 检查结果
assert r.status_code == 200
assert r.reason == 'OK'
assert r.json()['status'] == 1
assert r.json()['code'] == '10001'

# get请求带参数
# 方法1：拼接到URL后面(金融项目注册接口)
url = "http://jy001:8081/futureloan/mvc/api/member/register" \
      "?mobilephone=&pwd=123456&regname=helloworld"
r = requests.get(url)
print(r.text)
print("==================================END==========================")
# 方法2：使用params传参数
url = "http://jy001:8081/futureloan/mvc/api/member/register"
canshu = {"mobilephone": "18012345678", "pwd": 123456, "regname": ""}
r = requests.get(url, params=canshu)
print(r.text)
print("==========================END============================")
# get请求带请求头，设置User-Agent伪装成浏览器发送的请求，避免服务器屏蔽自动化发的请求。
# 一个测试网站，get是接口名字，发送的请求，原封的返回回来。
url = "http://www.httpbin.org/get?mobilephone=&pwd=123456&regname=helloworld"
r = requests.get(url)  # "User-Agent": "python-requests/2.18.4"
print(r.text)
print("=================================END=============================")
# User-Agent 包含浏览器的版本号、操作系统的版本号等信息。
tou = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/84.0.4147.89 Safari/537.36"}
r = requests.get(url, headers=tou)
print(r.text)
print("===========================END=======================")

url = "https://wenku.baidu.com/view/027d607deff9aef8941e06c0.html"
r = requests.get(url, headers=tou)
print(r.text)
print("蜂群算法源代码" in r.text)
