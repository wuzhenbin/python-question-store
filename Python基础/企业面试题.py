

# python新式类和经典类的区别？
a. 在python里凡是继承了object的类，都是新式类 
b. Python3里只有新式类 
c. Python2里面继承object的是新式类，没有写父类的是经典类 
d. 经典类目前在Python里基本没有应用

# python中内置的数据结构有几种？
数字 Number
字符串 string、 
列表list、 
元祖tuple 
字典 dict 、 
集合 set


# python如何实现单例模式?请写出两种实现方式?？
'''
在它的核心结构中只包含一个被称为单例的特殊类。通过单例模式可以保证系统中，应用该模式的一个类只有一个实例。即一个类只有一个对象实例。
'''
第一种方法:使用装饰器
def singleton(cls):
    instances = {}
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper
@singleton
class Foo(object):
    pass
foo1 = Foo()
foo2 = Foo()
print(foo1 is foo2) #True


第二种方法：使用基类 New 是真正创建实例对象的方法，所以重写基类的new 方法，以此保证创建对象的时候只生成一个实例
class Singleton(object):
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = super(Singleton,cls).__new__(cls,*args,**kwargs)
        return cls._instance
    
class Foo(Singleton):
    pass

foo1 = Foo()
foo2 = Foo()

print(foo1 is foo2) #True


第三种方法：元类，元类是用于创建类对象的类，类对象创建实例对象时一定要调用call方法，
因此在调用call时候保证始终只创建一个实例即可，type是python的元类
class Singleton(type):
    def __call__(cls,*args,**kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = super(Singleton,cls).__call__(*args,**kwargs)
        return cls._instance


class Foo(object):
    __metaclass__ = Singleton

foo1 = Foo()
foo2 = Foo()
print(foo1 is foo2) #True




# 反转一个整数，例如-123 --> -321
class Solution(object):
    def reverse(self,x):
        if -10<x<10:
            return x
        str_x = str(x)
        if str_x[0] !="-":
            str_x = str_x[::-1]
            x = int(str_x)
        else:
            str_x = str_x[1:][::-1]
            x = int(str_x)
            x = -x
        return x if -2147483648<x<2147483647 else 0
if __name__ == '__main__':
    s = Solution()
    reverse_int = s.reverse(-120)
    print(reverse_int)


# 设计实现遍历目录与子目录，抓取.pyc文件
第一种方法：
import os

def getFiles(dir,suffix):
    res = []
    for root,dirs,files in os.walk(dir):
        for filename in files:
            name,suf = os.path.splitext(filename)
            if suf == suffix:
                res.append(os.path.join(root,filename))

    print(res)

getFiles("./",'.pyc')

第二种方法：
import os

def pick(obj):
    try:
        if obj.[-4:] == ".pyc":
            print(obj)
        except:
            return None
    
def scan_path(ph):
    file_list = os.listdir(ph)
    for obj in file_list:
        if os.path.isfile(obj):
    pick(obj)
        elif os.path.isdir(obj):
            scan_path(obj)
    
if __name__=='__main__':
    path = input('输入目录')
    scan_path(path)


# 一行代码实现1-100之和
count = sum(range(0,101))
 












