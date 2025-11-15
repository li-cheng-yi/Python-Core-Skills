#创建一个包含6门可选课程的集合
available_courses={'摆烂学','躺平学','高等元素论','高速退学','熬夜学'}
print("可选课程:", available_courses)
#创建一个空的已选课程集合
yijingxuanlede_courses=set()
print("已选课程:", yijingxuanlede_courses)
#创建一个包含3门推荐课程的集合
advised_courses={'不想学','还能学','死里学'}
#向已选课程集合中添加两门课程
yijingxuanlede_courses.add('二年级数学')
yijingxuanlede_courses.add('死里学')
print('添加课程后',yijingxuanlede_courses)
#使用交集操作找出已选课程和推荐课程中的共同课程
print('已选课程和推荐课程中的共同课程',yijingxuanlede_courses & advised_courses)
#使用并集操作合并已选课程和推荐课程
print('合并已选课程和推荐课程',yijingxuanlede_courses|advised_courses)
#使用差集操作找出推荐课程中尚未选择的课程
print('推荐课程中尚未选择的课程',advised_courses-yijingxuanlede_courses)
#遍历已选课程集合，逐个显示每门课程
for item in yijingxuanlede_courses:
    print(item)
#检查选课数量是否超过限制（假设最多选4门课程）
if len(yijingxuanlede_courses) > 4:
    print('超过限制')
else:
    print('没超过')