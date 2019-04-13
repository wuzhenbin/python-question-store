

# 现有字典 d= {'a':24,'g':52,'i':12,'k':33}请按value值进行排序?
d = {'a':24,'g':52,'i':12,'k':33}
res = dict(sorted(d.items(),key=lambda x:x[1]))
print(res)

# 字典推导式
dict1 = {"name": "zhangsan", "age": 18}
dict2 = {value: key for key, value in dict1.items()}
print(dict2)

# 请反转字符串 "aStr"?
print("aStr"[::-1])

# 将字符串 "k:1|k1:2|k2:3|k3:4"，处理成字典 {k:1,k1:2,...}
str1 = "k:1|k1:2|k2:3|k3:4"
def str2dict(str1):
    dict1 = {}
    for iterms in str1.split('|'):
        key,value = iterms.split(':')
        dict1[key] = value
    return dict1

res = str2dict(str1)


# 请按alist中元素的age由大到小排序
alist = [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]
def sort_by_age(list1):
    return sorted(alist,key=lambda x:x['age'],reverse=True)


# 下面代码的输出结果将是什么？
list = ['a','b','c','d','e']
print(list[10:])
'''
代码将输出[],不会产生IndexError错误，就像所期望的那样，尝试用超出成员的个数的index来获取某个列表的成员。例如，尝试获取list[10]和之后的成员，会导致IndexError。然而，尝试获取列表的切片，开始的index超过了成员个数不会产生IndexError，而是仅仅返回一个空列表。这成为特别让人恶心的疑难杂症，因为运行的时候没有错误产生，导致Bug很难被追踪到。
'''


# 写一个列表生成式，产生一个公差为11的等差数列
print([x*11 for x in range(10)])


# 给定两个列表，怎么找出他们相同的元素和不同的元素？
list1 = [1,2,3]
list2 = [3,4,5]
set1 = set(list1)
set2 = set(list2)
print(set1 & set2)
print(set1 ^ set2)
A,B 中相同元素： print(set(A)&set(B))
A,B 中不同元素:  print(set(A)^set(B))



# 请写出一段python代码实现删除list里面的重复元素？
l1 = ['b','c','d','c','a','a']
print(list(set(l1)))


l1 = ['b','c','d','c','a','a']
l2 = list(set(l1))
l2.sort(key=l1.index)
print(l2)


l1 = ['b','c','d','c','a','a']
l2 = sorted(set(l1),key=l1.index)
print(l2)


l1 = ['b','c','d','c','a','a']
l2 = []
for i in l1:
    if not i in l2:
        l2.append(i)
print(l2)















