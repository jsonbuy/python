"""
函数名： def get_excel_data()
版本： v1.0
函数功能：
    1，获取请求的body与预期的响应结果
具体方案：
    1，导入对应的excel读取的库 xlrd 处理.xls格式, openpyxl处理.xlxs
    2，把excel文件读取到内存 excel对象
    3，找到你需要操作的sheet
    4，读取对应的行与列数据（单元格数据）
"""
import xlrd
import json

#-------------判断是否是json-------------------
def is_json(str):
    try:
        json.loads(str)
    except: # 只有try报错才执行里面的代码
        return False
    return True

def get_excel_data(excelDir,sheetName,caseName,*colName,selectCase=['all']):
    """
    :param excelDir: 文件路径
    :param sheetName: 文件页签名
    :param caseName: 用例名称
    :param colName: 需要读取的列名称
    :param selectCase: 需要执行的用例 某一个 某一段 ['001','003-006']
    :return:
    """
    resList = []
    # 加载excel
    # formatting_info = True 保持样式
    workBook = xlrd.open_workbook(excelDir,formatting_info=True)
    workSheet = workBook.sheet_by_name(sheetName)
    # 把函数调用者输入的列明 -- 转化 -- 编号
    colIndex = []
    for name in colName:
        index = workSheet.row_values(0).index(name)
        colIndex.append(index)
    #-------------------挑选执行用例--------------------
    selectList = []
    if 'all' in selectCase: #全部执行
        selectList = workSheet.col_values(0)
    else:#1 某一个 2某一段 ['001','003-006']
        for one in selectCase:
            if '-' in one:
                start,end = one.split('-')
                for i in range(int(start),int(end)+1):
                    selectList.append(caseName+f'{i:0>3}')
            else:
                selectList.append(caseName+f'{one:0>3}')
    #-------------------------------------------------
    # 获取数据
    print(selectList)
    idx = 0 # 代表行号初始值
    for one in workSheet.col_values(0): # 获取第0列数据
        if caseName in one and one in selectList: # 条件满足， 这一行数据的对应列是需要的数据
            getColData = [] # 存放一行对应的很多列数据
            for colI in colIndex:
                res = workSheet.cell_value(idx,colI) # 读取某一个单元格的数据
                if is_json(res): # 判断单元格数据是否是json数据
                    res = json.loads(res)
                getColData.append(res)
            resList.append(getColData)
        idx += 1
    print(resList)
    return resList

if __name__ == '__main__':
    configData= ['用例编号','请求参数','URL']
    get_excel_data('../data/Delivery_System_V1.0.xls','登录','Login',*configData,selectCase=['004','001-002'])