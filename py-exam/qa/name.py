
from const import PI

def calc_round_area(radius):
    return PI * (radius ** 2)

def main():
    print("round area: ", calc_round_area(2))

main()


# PI = 3.14
# def main():
#     print("PI:", PI)

# main()
PI = 3.14

def main():
    print("PI:", PI)

if __name__ == "__main__":
    main()


# 理解Python中的if __name__ == '__main__'
# 假如你叫小明.py，在朋友眼中，你是小明(__name__ == '小明')；在你自己眼中，你是你自己(__name__ == '__main__')
# 当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；
# 当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。

# 假设我们有一个const.py文件
PI = 3.14

def main():
    print("PI:", PI)

main()

# 运行结果：PI: 3.14


# area
from const import PI

def calc_round_area(radius):
    return PI * (radius ** 2)

def main():
    print("round area: ", calc_round_area(2))

main()

# 我们看到const.py中的main函数也被运行了，实际上我们不希望它被运行，
# 因为const.py提供的main函数只是为了测试常量定义。
# 这时if __name__ == '__main__'派上了用场，我们把const.py改一下，添加if __name__ == "__main__"：