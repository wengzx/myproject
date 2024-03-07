from testxl import load_workbook

# 1.打开 Excel 表格并获取表格名称

# 打开当前py程序路径下excelDemo文件夹下的qiyuan.xlsx文件
workbook = load_workbook(filename='./3.xlsx')

# 2.获取表格 只有一张表格的时候，可以直接 active
sheet3 = workbook.active
print(sheet3)
# 输出结果 <Worksheet "Sheet1">


# 3.获取一系列格子  .iter_rows()与.iter_cols()方式

# 按行获取值
# 读取1-2行中1-4列的数据（先行后列）
# for i in sheet3.iter_rows(min_row=1, max_row=2, min_col=1,max_col=4):
# 	for j in i:
# 		print(j.value)

# 输出结果：
# 功能模块(依据导图一级分支)
# 功能点（二级功能点/二级测试子任务）
# 优先级（主、高、中、低）
# 用例编号（M-00001---管理端，A-00001---APP）
# 机审规则
# 年龄检测
# 主
# A-00001

#  按列获取值
# 读取1-2行中1-4列的数据（先列后行）
for i in sheet3.iter_cols(min_row=1, max_row=2, min_col=1, max_col=4):
    for j in i:
        print(j.value)

# 输出结果：
# 功能模块(依据导图一级分支)
# 机审规则
# 功能点（二级功能点/二级测试子任务）
# 年龄检测
# 优先级（主、高、中、低）
# 主
# 用例编号（M-00001---管理端，A-00001---APP）
# A-00001

