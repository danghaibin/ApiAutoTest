'''
测试登录功能
'''
import pytest

from ZongHe.baw import DbOp, Member
from ZongHe.caw import DataRead

# 测试前置：获取测试数据 数据是列表 通过readyaml读取来的
@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/login_data.yaml"))
def login_data(request): # 固定写法
    return request.param

# 测试前置：获取测试数据 数据是列表 通过readyaml读取来的
@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/login_setup.yaml"))
def setup_data(request): # 固定写法
    return request.param


# 测试前置和后置
@pytest.fixture()
def register(setup_data,url,baserequests,db):
    # 注册
    phone = setup_data['casedata']['mobilephone']
    DbOp.deleteUser(db,phone)
    Member.register(url,baserequests,setup_data['casedata'])
    yield
    # 删除注册用户
    DbOp.deleteUser(db,phone)


def test_login(register,login_data,url,baserequests):
    # 登录
    # 检查登录结果
    r = Member.login(url,baserequests,login_data['casedata'])
    assert str(r.json()['msg']) == str(login_data['expect']['msg'])
    assert str(r.json()['status']) == str(login_data['expect']['status'])
    assert str(r.json()['code']) == str(login_data['expect']['code'])
