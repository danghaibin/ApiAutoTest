import requests
import xlrd
# 读取用例
# 1.获取文件路径
excelDir = r"D:\ApiAutoTest\ZuoYe\data\金融接口测试用例_1.1.xlsx"
# 打开excel
workBook = xlrd.open_workbook(excelDir)
# 操作sheet1
workSheet = workBook.sheets()[0]
# print(workSheet)
data = workSheet.cell(6, 7).value
print("data="+data)
# # 2.获取地址
url = 'http://jy001:8081/futureloan/mvc/api/member/register'

# 3.执行用例

# 4判断 断言
# 5.报告