'''
脚本层的公共方法
'''
from ZongHe.caw import DataRead  # 导入模块
import pytest

# 从环境文件中读取url
from ZongHe.caw.BaseRequests import BaseRequests # 从模块中导入类


@pytest.fixture(scope='session')
def url():
    return DataRead.readini("ZongHe/data_env/env.ini","url")

# 从环境文件中读取db
@pytest.fixture(scope='session')
def db():
    # 从ini中读取出来是字符串 将字符串转换成字典 使用eval函数
    return eval(DataRead.readini("ZongHe/data_env/env.ini","db"))

# 创建BaseRequests的一个实例
@pytest.fixture(scope='session')
def baserequests():
    return BaseRequests()
