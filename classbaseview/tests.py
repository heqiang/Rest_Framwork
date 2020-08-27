from django.test import TestCase
from django.utils.decorators import  classonlymethod
# Create your tests here.

class  Test(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod  #类方法 类和实例均可以调用
    # @staticmethod
    def sleep(sel):
        print("1")
    # 只是给类提供 不给实例提供
    @classonlymethod
    def  go(cls):
        print("go")

test = Test("hq",12)
print(Test.__dict__)

dic_new = {
    "java":""
}
