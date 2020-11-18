'''
用户模块的接口（注册，登录，获取用户列表，充值，取现）
'''

def register(url,baserequests,data):
    '''
    :param url: http://jy001:8081/
    :param baserequests:是BadeRequests的一个实例
    :param data:注册接口的参数
    :return:响应的信息
    '''
    url = url +"futureloan/mvc/api/member/register"
    r = baserequests.post(url,data = data)
    return r


def getList(url,baserequests):
    url = url + "futureloan/mvc/api/member/list"
    r = baserequests.get(url)
    return r


def login(url,baserequests,data):

    url = url + "futureloan/mvc/api/member/login"
    r = baserequests.post(url, data=data)
    return r


if __name__ == '__main__':
    from ZongHe.caw.BaseRequests import BaseRequests

    baserequests = BaseRequests()
    canshu = {"mobilephone": "137123456789", "pwd": "123456abc"}
    r = register("http://jy001:8081/",baserequests,canshu)
    print(r.text)


