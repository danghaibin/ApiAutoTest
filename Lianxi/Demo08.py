import requests
from time import sleep
from lxml import etree
from multiprocessing import Pool,Manager

def download_chapter_list(url):
    # 获取章节列表页面
    response = requests.get(url)
    # 指定编码集
    response.encoding = 'utf-8'
    # 将文本格式页面转换为etree对象
    selector = etree.HTML(response.text)
    # 获取小说的名称
    title = selector.xpath('//div[@id="info"]/h1/text()')[0]
    # 获取所有章节地址
    links = selector.xpath('//div[@id="list"]/d1/dd/a/herf')

    links = [url+link for link in links]
    return title,links

def download_chapter_content(args):
    d = args[0]
    link = args[1]
    try:
        # 下载章节
        sleep(2)
        response = requests.get(link)
        response.encoding = 'utf-8'
        selector = etree.HTML(response.text)
        ctitle = selector.xpath('//h1/text()')[0]
        if ctitle == "503 Service Temporarily Unavailable":
            raise NameError('503异常')
        print('正在下载...%s'%ctitle)

        # 获取内容
        content = selector.xpath('//div[@id="content"]/text()')
        result = ''
        for line in content:
            result += line+'\n'

        # 保存到字典中
        d[link] = ctitle+'\n'+result

    except Exception as e:
        print(e)
        download_chapter_content(args)

def save_content(title,links,d):
    with open("%s.txt"%title,mode='a',encoding='utf-8')as f:
        for link in links:
            f.write(d[link])

# def main(url):
#
