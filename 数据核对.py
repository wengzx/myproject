
import pandas as pd

def autocheck(io_form,io_form2,io_to):
    print(333)
    df_1=pd.read_excel(io_form)
    df_2=pd.read_excel(io_form2)
    result=pd.merge(df_1,df_2,on="姓名",how="outer",suffixes=('_1','_2'))

    result.fillna(0,inplace=True)
    result["差异——语文"]=result["语文_1"]-result["语文_2"]
    result["差异——数学"]=result["数学_1"]-result["数学_2"]
    result["差异——英语"]=result["英语_1"]-result["英语_2"]

    df=result[(result["差异——语文"]!=0)|result["差异——数学"]|result["差异——英语"]]
    df.to_excel(io_to,index=False)


if __name__ == '__main__':
    autocheck("1.xlsx","2.xlsx","io_to.xlsx")
