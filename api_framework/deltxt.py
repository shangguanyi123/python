#encoding=utf-8
import os
# 清空文件内容
def delwenjian():
    with open(
    os.getcwd() + '\\log\\log1.txt', 'w') as f1, open(os.getcwd() + '\\log\\log2.txt', 'w') as f2, open(os.getcwd() + '\\log\\log3.txt', 'w') as f3,open(os.getcwd() + '\\log\\log4.txt', 'w') as f4:
        f1.write('')
        f2.write('')
        f3.write('')
        f4.write('')

delwenjian()


