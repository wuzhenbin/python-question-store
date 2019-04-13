
# python爬虫的7个经典问题


# 下面代码的输出是什么？
def multipliers():
    return [lambda x : i * x for i in range(4)]
 
print([m(2) for m in multipliers()])
'''
上面代码的输出是[6, 6, 6, 6](不是[0, 2, 4, 6]).
原因是Python的闭包是延迟绑定(late binding)的。
这表明在闭包中使用的变量直到内层函数被调用的时候才会被查找。
结果是，当调用multipliers()返回的函数时，i参数的值会在这时被在调用环境中查找。
所以，无论调用返回的哪个函数，for循环此时已经结束，i等于它最终的值3。
因此，所有返回的函数都要乘以传递过来的3，因为上面的代码传递了2作为参数，
所以他们都返回了6（即，3 * 2）
顺便提一句，正如在书《The Hitchhiker’s Guide to Python》中提出来的一样,
有一种广泛传播的误解认为这个问题和lambda表达式有关，事实并非如此。
通过labda表达式产生的函数并没有什么特别之处，使用普通的def定义的函数的行为和lambda表达式产生的函数的行为是一样的.
下面是一些可以绕过这个问题的方法。
'''
# 生成器
def multipliers():
    for i in range(4): 
        yield lambda x : i * x 

# 另一个方法是创造一个闭包，通过使用一个默认参数来立即绑定它的参数
def multipliers():
    return [lambda x, i=i : i * x for i in range(4)]

# 或者，你也可以使用functools.partial函数(偏函数) ：
from functools import partial
from operator import mul
 
def multipliers():
    return [partial(mul, i) for i in range(4)]



# 下面代码的输出是什么
class Parent(object):
    x = 1

class Child1(Parent):
    pass

class Child2(Parent):
    pass

print(Parent.x, Child1.x, Child2.x)
Child1.x = 2
print(Parent.x, Child1.x, Child2.x)
Parent.x = 3
print(Parent.x, Child1.x, Child2.x)
'''
让很多人感到疑惑和惊讶的是，最后一行的输出竟然不是3 2 1而是3 2 3.
为什么修改了Parent.X的值会影响到Child2.x，但是同时又没有改变Child1.x的值呢？
这个问题的关键在于，在python中，类中的变量在内部被当作字典处理。
如果一个变量名在当前类的字典中没有被发现，系统将会在这个类的祖先(例如，它的父类)中继续寻找，
直到找到为止(如果一个变量名在这个类和这个类的祖先中都没有，那么将会引发一个AttributeError错误)
因此，在父类中将变量x赋值为1，那么x变量将可以被当前类和所有这个类的子类引用。
这就是为什么第一个print语句输出为1 1 1.
接下来，如果它的子类覆盖了这个值(例如， 当我们执行Child1.x = 2)，那么这个变量的值仅仅在这个子类中发生了改变。
这就是为什么第二个print语句输出1 2 1
最后，如果父类改变了这个变量的值(例如，我们执行Parent.x = 3)，所有没有覆盖这个参数值的子类(在这个例子中覆盖了参数的就是Child2)都会受到影响，
这就是为什么第三个print语句的输出为3 2 3
'''


# 下面代码的输出是什么？
def extendList(val, y=5):
    y += val
    return y

list1 = extendList(10)
list2 = extendList(123,0)
list3 = extendList(9)

print("list1= %s" % list1)
print("list2= %s" % list2)
print("list3= %s" % list3)
'''
list1和list3都是在操作同一个默认list，
而list2是在操作它自己创建的一个独立的list(将自己的空list作为参数传递过去)
extendlist的定义可以这样定义来达到我们预期的效果：
'''

def extendList(val, list=None):
    if list is None:
        list = []
    list.append(val)
    return list


# 下面代码的输出是什么？
def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print("list1 = %s" % list1)
print("list2 = %s" % list2)
print("list3 = %s" % list3)

'''
很多人会错误地预计list1等于［10］，list3等于['a']，
认为extendList函数的list参数在每一次函数被调用时都会被设置为默认值[]
但是，真实的情况是，默认的list只在函数定义的时候被创建一次。
之后不指定list参数地调用extendList函数时，使用的都是同一个list。
这是因为默认参数在函数定义的时候被计算的，而不是在函数调用时。
'''


# 下面的代码在输出是什么？
def div1(x,y):
    print("%s/%s = %s" % (x, y, x/y))

def div2(x,y):
    print("%s//%s = %s" % (x, y, x//y))

div1(5,2)
div1(5.,2)
div2(5,2)


# 下面的代码输出什么？
list = ['a', 'b', 'c', 'd', 'e']
print(list[10])
'''
当取列表元素的时候，如果索引值超过了元素的个数
将会导致IndexError错误
但是，取一个列表的切片的时候，如果起始索引超过了元素个数，
将不会引起IndexError错误，仅返回一个空列表
'''