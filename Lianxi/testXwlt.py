# -*- coding = utf-8 -*-
# Time :2020/11/8 11:51
# Author
# @File:testXwlt.py
# @software:pycharm
import xlwt
# workbook = xlwt.Workbook(encoding="utf-8") # 创建workbook对象
# worksheet = workbook.add_sheet('sheet1') # 创建工作表
# worksheet.write(0,0,'hello') # 写入数据  第一个参数表示行 第二个参数表示列 第三个参数表示内容
# workbook.save('student.xls') # 保存数据表

workbook = xlwt.Workbook(encoding="utf-8") # 创建workbook对象
worksheet = workbook.add_sheet('sheet1') # 创建工作表
for i in range(0,9):
    for j in range(0,i+1):
        worksheet.write(i,j,"%d*%d=%d"%(i+1,j+1,(i+1)*(j+1)))

workbook.save('student.xls') # 保存数据表

'''
# 保存数据
def saveData(datalist,savepath):
    print(save...)
    book = xwlt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('单元表名') 
    col = ("a","s","d","f","g")
    for i in range(0,5):
        sheet.write(0,i,col[i])
    for i in range(250):
        print("第%d条"%(i+1))
        data = datalist[i]    
        for j in range(0,8):
            sheet.write(i+1,j,data[j])  # 第二行第一列（1,0）       
    book.save("student.xls")
'''