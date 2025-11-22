"""
定义一个圆的类计算面积和周长
需求：定义一个圆类—Circle，提供一个属性r(半径)，提供两个方法：
计算圆的面积get_area(self)和计算圆的周长get_perimeter(self)
通过两个方法计算圆的周长和面积并且对计算结果进行输出
最后从键盘录入半径，创建圆类的对象，并调用计算面积和周长的方法输出面积和周长
"""
class Circle():
    def __init__(self,r):
        self.r=r
    def get_area(self):
        print('面积为', 3.14 * self.r ** 2)
    def get_perimeter(self):
        print('周长为',2*3.14*self.r)
r0=eval(input('请输入半径'))
circle=Circle(r0)
circle.get_area()
circle.get_perimeter()