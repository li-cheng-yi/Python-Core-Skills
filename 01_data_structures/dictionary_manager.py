#创建一个包含5个学生信息的字典，键为学生姓名，值为成绩（0-100的整数）
student_information={'张学良':95,'张作霖':90,'工藤新一':81,'蔡徐坤':50,'余则成':63}
#遍历学生成绩字典
for key,value in student_information.items():
    print('学生:',key,'-','成绩:',value)
#实现一个查询功能，输入学生姓名，如果存在则显示成绩，否则显示"该学生不存在"
chaxun=input('请输入要查询的学生姓名')
print(student_information.get(chaxun,'该学生不存在'))
#实现添加新学生功能，如果学生已存在则提示，否则添加到字典中
tianjia=input('请输入要添加的学生')
if student_information.get(tianjia)!=None:
    print('学生已存在')
else:
    chengji=eval(input('请输入该学生成绩'))
    student_information[tianjia]=chengji
    print(student_information)
#将百分制成绩转换为等级制：90-100: "优秀" 80-89: "良好" 70-79: "中等" 60-69: "及格" <60: "不及格"
for key,value in student_information.items():
    if value >=90:
        print(key,'优秀')
    elif value >=80:
        print(key,'良好')
    elif value >=70:
        print(key,'中等')
    elif value >=60:
        print(key,'及格')
    else:
        print(key,'不及格')




