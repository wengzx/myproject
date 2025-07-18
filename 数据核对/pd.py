import pandas as pd  # 导入模块

df1 = pd.DataFrame({'One': [1, 2, 3],"twi":[5,8,9]})
df1.to_excel('excel1.xlsx', sheet_name='Sheet1', index=False) # index false为不写入索引
