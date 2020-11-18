import mock
import requests
class JinRong():

    def chongzhi(self,data):
        r = requests.post("http://jy001:8081/futureloan/mvc/api/member/amount", data=data).json()
        return r

    def quxian(self,data):

        r = requests.post("http://jy001:8081/futureloan/mvc/api/member/withdraw",data=data).json()
        return r


class TestJingRong():
    def test_quxian(self):
        jinrong =JinRong()
        c = {"mobilephone":15811110001,"amount":100}
        r = jinrong.chongzhi(c)
        assert r['msg'] == "取现成功"
        assert r['status'] == 1
        assert r['code'] == '10001'


        jinrong.quxian = mock.Mock(return_value={'status':1,'code':10001,'msg':'取现成功'})
        data = {"mobilephone":1581111001,"amount":"100"}
        r = jinrong.quxian(data)


        assert r['msg'] == "充值成功"
        assert r['status'] == 1
        assert r['code'] == '10001'
