"""
定义学生类录入5个学生信息存储到列表中
需求：定义学生类Student，包含姓名，年龄，性别，分数四个属性，
提供一个用于学员信息输出的方法info(self)。编写测试代码，使用循环录入5位学生的信息，
由于录入的学生信息中间使用“#”进行分隔，所以需要使用字符串的split()方法，进行劈分，
使用劈分的信息创建学生对象，使用列表存储学生信息，最后使用循环遍历列表，
调用对象的info()方法输出学员信息。
"""
class Student():
    def __init__(self,name,age,sex,score):
        self.name=name
        self.age=age
        self.sex=sex
        self.score=score
    def info(self):
        print('姓名:',self.name,'年龄:',self.age,'性别:',self.sex,'分数:',self.score)
students=[]
for i in range(1,6):
    data=input('请输入学生信息，使用''姓名#年龄#性别#分数''的格式')
    lst_data=data.split(sep='#')
    student=Student(lst_data[0],lst_data[1],lst_data[2],lst_data[3])
    students.append(student)
for item in students:
    item.info()


