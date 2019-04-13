
# 对__if__name__ == 'main'的理解陈述
__name__是当前模块名，当模块被直接运行时模块名为_main_，也就是当前的模块，当模块被导入时，
模块名就不是__main__，即代码将不会执行。



# python有哪些数据类型？如何判断一个数据类型的类型？如何判断a是否为数组？

# 转置一个字符串 ‘hello world’

# 使用python去重 a = ['b','c','d','b','c','a','a']


# 请写出一段Python代码实现删除一个list里面的重复元素
# 1.使用set函数
list = [1, 3, 4, 5, 51, 2, 3]
set(list)
# 2.使用字典函数，
>>> a = [1, 2, 4, 2, 4, 5, 6, 5, 7, 8, 9, 0]
>>> b = {}
>>> b = b.fromkeys(a)
>>> c = list(b.keys())
>>> c


# 定义reverse_dict函数来实现键值对倒转

# 请写出你知道的python中的数据结构以及用途

# 同步/ 异步/ 协程/ 多线程/ 多进程 ？以及试用场景

# python 函数是传值还是传应用？

# 有见过哪些设计模式


# python是如何进行内存管理的？
a、对象的引用计数机制
	python内部使用引用计数，来保持追踪内存中的对象，Python内部记录了对象有多少个引用，
	即引用计数，当对象被创建时就创建了一个引用计数，当对象不再需要时，这个对象的引用计数为0时，它被垃圾回收。

b、垃圾回收
	1>当一个对象的引用计数归零时，它将被垃圾收集机制处理掉。
	2>当两个对象a和b相互引用时，del语句可以减少a和b的引用计数，并销毁用于引用底层对象 的名称。
	然而由于每个对象都包含一个对其他对象的应用，因此引用计数不会归零，对象也不会销毁。（从而导致内存泄露）。
	为解决这一问题，解释器会定期执行一个循环检测器，搜索不可访问对象的循环并删除它们。

c、内存池机制
	Python提供了对内存的垃圾收集机制，但是它将不用的内存放到内存池而不是返回给操作系统。
	1>Pymalloc机制。为了加速Python的执行效率，Python引入了一个内存池机制，用于管理 对小块内存的申请和释放。
	2>Python中所有小于256个字节的对象都使用pymalloc实现的分配器，而大的对象则使用 系统的malloc。
	3>对于Python对象，如整数，浮点数和List，都有其独立的私有内存池，对象间不共享他们的内存池。
	也就是说如果你分配又释放了大量的整数，用于缓存这些整数的内存就不能再分配给浮点数。


# Python里面如何拷贝一个对象？（赋值，浅拷贝，深拷贝的区别）
赋值（=），就是创建了对象的一个新的引用，修改其中任意一个变量都会影响到另一个。
浅拷贝：创建一个新的对象，但它包含的是对原始对象中包含项的引用（如果用引用的方式修改其中一个对象，另外一个也会修改改变）
{ 1,完全切片方法; 2，工厂函数，如list(); 3，copy模块的copy()函数}
深拷贝：创建一个新的对象，并且递归的复制它所包含的对象（修改其中一个，另外一个不会改变）
{copy模块的deep.deepcopy()函数}


# 介绍一下except的用法和作用？
try…except…except…else…
执行try下的语句，如果引发异常，则执行过程会跳到except语句。对每个except分支顺序尝试执行，
如果引发的异常与except中的异常组匹配，执行相应的语句。如果所有的except都不匹配，
则异常会传递到下一个调用本代码的最高层try代码中。
try下的语句正常执行，则执行else块代码。如果发生异常，就不会执行如果存在finally语句，最后总是会执行。



# Python中__new__与__init方法的区别
__new__:它是创建对象时调用，会返回当前对象的一个实例，可以用_new_来实现单例
__init__:它是创建对象后调用，对当前对象的一些实例初始化，无返回值



# Python在服务器的部署流程，以及环境隔离


# Django 和 Flask 的相同点与不同点，如何进行选择？


# 写一个Python中的单例模式
class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)  
        return cls._instance  
class MyClass(Singleton):  
    a = 1
one = MyClass()
two = MyClass()
id(one) = id(two)
>>> True


# 什么是lambda函数？它有什么好处?
lambda 表达式，通常是在需要一个函数，但是又不想费神去命名一个函数的场合下使用，也就是指匿名函数
lambda函数：首要用途是指点短小的回调函数
lambda [arguments]:expression
>>> a=lambdax,y:x+y
>>> a(3,11)



python 常用数据结构有哪些？请简要介绍一下。

简要描述 Python 中单引号、双引号、三引号的区别。

如何在一个 function 里面设置一个全局的变量？

Python 里面如何拷贝一个对象？（赋值、浅拷贝、深拷贝的区别）

如果 custname 字符串的内容为 utf-8 的字符，如何将 custname 的内容转为 gb18030 的字符串？

请写出一段 Python 代码实现删除一个 list 里面的重复元素。

这两个参数是什么意思：args，*kwargs？

统计如下 list 单词及其出现次数。
a=['apple', 'banana', 'apple', 'tomato', 'orange', 'apple', 'banana', 'watermeton']

给列表中的字典排序：假设有如下 list 对象
alist=[{"name":"a", "age":20}, {"name":"b", "age":30}, {"name":"c", "age":25}]
将 alist 中的元素按照 age 从大到小排序。


写出下列代码的运行结果
a = 1
def fun(a):
  a = 2
fun(a)
print(a)

a = []
def fun(a):
  a.append(1)
fun(a)
print(a)

class Person:
    name = 'Lily'

p1 = Person()
p2 = Person()
p1.name = 'Bob'
print(p1.name)
print(p2.name)
print(Person.name)


假设有如下两个 list：a = ['a', 'b', 'c', 'd', 'e']，b = [1, 2, 3, 4, 5]，
将 a 中的元素作为 key，b 中元素作为 value，将 a，b 合并为字典。


使用 python 已有的数据结构，简单的实现一个栈结构。


















