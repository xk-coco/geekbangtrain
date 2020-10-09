#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/26 23:41
# @File    : p3_diamond.py

# 钻石继承
class BaseClass(object):
    num_base_calls = 0

    def call_me(self):
        print("Calling method on Base Class.")
        self.num_base_calls += 1


# class LeftSubclass(BaseClass):
#     num_left_calls = 0
#
#     def call_me(self):
#         print("Calling method on Left SubClass.")
#         self.num_left_calls += 1

class LeftSubclass(BaseClass):
    num_left_calls = 0

    # def call_me(self):
    #     print("Calling method on Left SubClass.")
    #     self.num_left_calls += 1


class RightSubClass(object):
    num_right_calls = 0

    def call_me(self):
        print("Calling method on Right SubClass.")
        self.num_right_calls += 1


class SubClass(LeftSubclass, RightSubClass):
    pass


a = SubClass()
a.call_me()  # 调用哪一个？
# Output：Calling method on Left SubClass.

# 注释掉LeftSubclass的Call_me方法
# Output:Calling method on Right SubClass.

# 注释掉RightSubClass的Call_me方法
# Output:Calling method on Base Class.

# 结论：广度优先，另外Python3中不加(object)也是新式类，但是为了代码不会误运行在Python2下产生意外结果，仍然建议增加

print(SubClass.mro())  # 显示子类的执行顺序

# 修改RightSubClass的父类为object
print(SubClass.mro())
