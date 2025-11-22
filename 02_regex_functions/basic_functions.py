'''编写一个函数，模拟简单的购物车功能：
必须参数：顾客姓名
可变位置参数：商品价格
默认参数：折扣（默认1.0，即无折扣）
计算商品总价、折后价格，并打印购物小票样式的输出'''
def shopping_car(name,*price,discount=1.0):
    sum=0
    for i in price:
        sum+=i
    discount_sum=sum*discount
    return name,sum,discount_sum
a,b,c=shopping_car('lcy',10,20,30,40,50)
print('姓名',a,'总价',b,'折后价',c)
'''编写一个函数，使用可变参数接收多个数字，将这些数字组成列表后，执行以下操作并分别打印结果：
列表排序（升序）
列表翻转
列表长度'''
def lst_function(*num):
    lst=[*num]
    lst_up=sorted(lst)
    lst_down=sorted(lst,reverse=True)
    lst_changdu=len(lst)
    return lst_up,lst_down,lst_changdu
a,b,c=lst_function(1,2,3,4,5)
print(a,b,c)
'''编写一个函数，使用可变参数接收一组销售数据，统计并打印：
销售总额
销售笔数
最大单笔销售额
最小单笔销售额'''
def xiaoshou(*xiaoshoumoney):
    bi=len(xiaoshoumoney)
    sum=0
    zuida=max(xiaoshoumoney)
    zuixiao=min(xiaoshoumoney)
    for i in xiaoshoumoney:
        sum+=i
    print('总额:',sum,'笔数:',bi,'最大单笔销售额:',zuida,'最小单笔销售额:',zuixiao)
xiaoshou(1,4,2,5,20,48,22,25)
'''编写三个独立函数：
计算两个数的加减乘除（四个运算都打印）
判断一个数是否为偶数
生成指定范围内的数字平方表（从1到n）'''
def calculation(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
calculation(10,20)
def judging_ou(m):
    if m%2==0:
        print('偶数')
    else:
        print('奇数')
judging_ou(13)
def pinfangbiao(n):
    for i in range(1,n+1):
        print(i,i**2,'\t')
pinfangbiao(10)
