'''
pytest命名规则：
1.测试文件以test_开头或结尾
2.测试类以Test开头
3.测试方法/函数以test_开头
'''
import requests

def register(data):
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    r = requests.post(url, data=data)
    return r

# 手机号码格式不正确
def test_register_001():
    # 测试数据
    data = {"mobilephone":"1801235767","pwd":123456,"regname":"hello"}
    # 预期结果
    expect = {"status":0,"code":"20109","data":None,"msg":"手机号码格式不正确"}
    # 测试步骤
    real = register(data)
    # 检查结果
    assert real.json()['msg'] == expect['msg']
    assert real.json()['code'] == expect['code']


# 密码不正确
def test_register_002():
    # 测试数据
    data = {"mobilephone":"1801654568","pwd":12345,"regname":"world"}
    # 预期结果
    expect = {"status":0,"code":"20108","data":None,"msg":"密码不正确"}
    # 测试步骤
    real = register(data)
    # 检查结果
    assert  real.json()['msg'] == expect['msg']
    assert  real.json()['code'] == expect['code']
