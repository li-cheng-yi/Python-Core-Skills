
#使用输入获取用户名、密码、邮箱、手机号
name=input('用户名：')
password=input('密码：')
email=input('邮箱：')
number=input('手机号：')
#验证用户名长度是否≥4个字符
while True:
    name1 = name.strip()
    if len(name1)<4:
        print('用户名太短不符合要求')
        name=input('请重新输入用户名')
    else:
        break

#定义非法字符字符串 invalid_chars = "!@#$%^&*()+=[]{}|;:,.<>?/"
invalid_chars = "!@#$%^&*()+=[]{}|;:,.<>?/"
#遍历用户名中的每个字符，检测是否包含非法字符
psdyanzheng=0
while True:
    password1 = (password.strip())
    for item in invalid_chars:
        for item2 in password1:
            if item == item2 or len(password1)<8:
                print('密码非法或太短')
                psdyanzheng=1
                break
            else:
                psdyanzheng=0
        if psdyanzheng == 0:
            break
        else:
            password=input('请重新输入密码')
    break
#检查邮箱是否包含"@"符号且只包含一个"@",邮箱长度是否在5-50个字符之间,不能以"@"或"."开头或结束"
while True:
    email1 = email.strip()
    c = email1.find('@')
    a = email1.count('@')
    if len(email1)<5 or len(email1)>50 or c==0  or c == len(email1)-1 or a!=1:
        print('邮箱错误')
        email1=input('请重新输入邮箱')
    else:
        break

#检查手机号是否为数字且11位
while True:
    number1=number.strip()
    number2=number1.isdigit()
    if number2==False or len(number1)!=11:
        print('手机号错误')
        number=input('请重新输入手机号')
    else:
        break
#使用%格式化生成："用户：xxx，注册时间：2025年"
print('用户:%s,注册时间：2025年'%(name1))
#使用str.format() 生成："联系方式：邮箱-xxx，手机-xxx"
print('联系方式：邮箱-{0},手机-{1}'.format(email1,number1))


