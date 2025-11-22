"""
编写函数实现计算列表中元素的最大值
需求：随机产生10个元素，存储到列表中，编写函数获取这个列表中元素的最大值（不能使用内置函数max()）
"""
import random
lst=[]
for i in range(1,11):
    i=random.randint(1,100)
    lst.append(i)
def maximum(x):
    maxitem=x[0]
    for j in x:
        if j>maxitem:
            maxitem=j
    print(maxitem)
maximum(lst)
"""
编写函数实现提取指定字符串中的数字并求和
需求：使用input()获取一个字符串，编写并传参，使用isdigit()方法提取字符串中所有的数字，
并对提取的数字进行求和计算，最后将存储数字的列表和累加和返回
"""
a=input('输入字符串')
def sum_up(x):
    lst = []
    for i in x:
        if i.isdigit():
            lst.append(int(i))
    print(sum(lst))
sum_up(a)
"""
编写函数实现将字符串中字母的大小写转换
需求：使用input()获取一个字符串，编写并传参，将字符串中所有的小写字母转成大写字母，将大写字母转成小写字母
"""
a=input('输入字符串')
def fun(x):
    lst=[]
    for i in x:
        if i.islower():
            lst.append(i.upper())
        else:
            lst.append(i.lower())
    for j in lst:
        print(j,end='')
    print('')
fun(a)
"""
编写函数实现操作符in的功能
需求：使用input()从键盘获取一个字符串，判断这个字符串在列表中是否存在（函数体不能使用in），返回结果为True或False
"""
a=input('输入字符串')
def fun_in(x,lst):
    m=0
    for i in lst:
        if i==x:
            m=1
    if m==1:
        return True
    else:
        return False
lst1=['helloworld','NEUQ','lcy']
print(fun_in(a,lst1))
