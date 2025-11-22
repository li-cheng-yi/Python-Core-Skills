"""
请使用面向对象的思想，设计自定义类，描述出租车和家用轿车的信息
出租车类：
属性包括：车型，车牌，所属出租公司；方法包括：启动，停止
家用轿车类：
属性包括：车型，车牌，车主姓名；方法包括：启动，停止
"""
class Taxi():
    def __init__(self,shape,paizi,company):
        self.shape=shape
        self.paizi=paizi
        self.company=company
    def action(self):
        pass
    def stop(self):
        pass
class Car():
    def __init__(self,shape,paizi,name):
        self.shape=shape
        self.paizi=paizi
        self.name=name
    def action(self):
        pass
    def stop(self):
        pass