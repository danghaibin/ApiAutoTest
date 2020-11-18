import pytest

from ZongHe.baw import Member
from ZongHe.caw import DataRead

# 测试前置 获取测试数据 数据是列表 通过readyaml读取来的
@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/login_fail.yaml"))
def fail_data(request):
    return request.param

# 登录失败
def test_login_fail(fail_data,url,baserequests):
    # 发送请求
    r = Member.login(url,baserequests,fail_data['casedata'])
    # 检查结果
    assert str(r.json()['msg']) == str(fail_data['expect']['msg'])
    assert str(r.json()['status']) == str(fail_data['expect']['status'])
    assert str(r.json()['code']) == str(fail_data['expect']['code'])


# @pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/login_pass.yaml"))
# def pass_data(request):
#     return request.param
# # 登录成功
# def test_login_pass(pass_data,url,db,baserequests):


