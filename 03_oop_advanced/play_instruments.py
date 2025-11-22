"""
使用面向对象思想实现乐器弹奏
需求：乐手可以弹奏不同的乐器从而发出不同的声音。可以弹奏的乐器包括二胡、钢琴和琵琶。
定义乐器类Instrument，包括方法make_sound()
定义乐器类的子类：二胡Erhu、钢琴Piano和小提琴Violin，
定义一个函数可以弹奏各种乐器play(instrument)，
测试给乐手不同的乐器让他弹奏
"""
class Instrument():
    def make_sound(self):
        print(f'{self}在演奏')
class Erhu(Instrument):
    def __str__(self):
        return '二胡'
class Piano(Instrument):
    def __str__(self):
        return '钢琴'
class Violin(Instrument):
    def __str__(self):
        return '小提琴'
def play(a):
    a.make_sound()
erhu=Erhu()
piano=Piano()
violin=Violin()
play(erhu)
play(piano)
play(violin)