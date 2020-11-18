import pytest
import requests

def register(data):
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    r = requests.post(url,data=data)
    return r

@pytest.fixture(params=[{"casedata":{"mobilephone":"13734869852","pwd":"123456789012345678","regname":"aaa"},"expect":{"status":"1","code":"10001","msg":"注册成功"}},
                        {"casedata":{"mobilephone":"13745781112","pwd":None,"regname":"aaa"},"expect":{"status":"0","code":"20103","msg":"参数错误：参数不能为空"}},
                        {"casedata":{"mobilephone":"137124556789","pwd":"123456abc","regname":"aaa"},"expect":{"status":"0","code":"20109","msg":"手机号码格式不正确"}},
                        {"casedata":{"mobilephone":"156","pwd":"123456abc","regname":"aaa"},"expect":{"status":"0","code":"20109","msg":"手机号码格式不正确"}}
                        ])

def data(request):
    return request.param

def test_register(data):
    real = register(data['casedata'])
    a = real.json()['msg']

    assert a == data['expect']['msg']
