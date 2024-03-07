
import os

# with open(r"C:\Users\Thinkpad\Desktop\33.txt",'a') as fp:
#     fp.write("\n")
#     fp.write("sssass")

with open(r"C:\Users\Thinkpad\Desktop\33.txt",'r+')as fp:

    fp.write("\n")
    fp.write("3123s")
    print(fp.read())

# 获取当前目录
print(os.getcwd())


aa=os.path.abspath("33.txt")

# 原始文件夹或者文件
os.path.basename(r"C:\Users\Thinkpad\Desktop")
print(os.path.basename(r"C:\Users\Thinkpad\Desktop\33.txt"))

# 是否存在文件
if os.path.exists(r"C:\Users\Thinkpad\Desktop\35.txt"):
    print(1222)
else:
    with open(r"C:\Users\Thinkpad\Desktop\35.txt",'w') as ff:
        ff.write("222")
        print(2333)