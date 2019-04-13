
# -----大文件读取问题-----
'''
有一个jsonline格式的文件file.txt 大小约为10K
'''
def get_lines():
    l = []
    with open('file.txt','rb') as f:
        return [eachline for eachline in f]

if __name__ == '__main__':
    for e in get_lines():
    	print(e)


# 现在要处理一个大小为10G的文件，但是内存只有4G，如果在只修改get_lines 函数而其他代码保持不变的情况下，应该如何实现？需要考虑的问题都有那些？
def get_lines():
    l = []
    with open('file.txt','rb') as f:
        # 60000是字节数
        data = f.readlines(60000)
    l.append(data)
    yield l

'''
要考虑的问题有：内存只有4G无法一次性读入10G文件，需要分批读入,分批读入数据要记录每次读入数据的位置、分批每次读取数据的大小，
太小会在读取操作花费过多时间。
'''


# -----遍历目标文件夹所有目录的文件-----
import os

def print_directory_contents(sPath):
"""
这个函数接收文件夹的名称作为输入参数
返回该文件夹中文件的路径
以及其包含文件夹中文件的路径
"""
    # 获取当前目录文件列表
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath,sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)

print_directory_contents('/Users/chenpin/Documents/github')








