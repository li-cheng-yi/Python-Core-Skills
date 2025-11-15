yanzheng=0
#使用输入获取用户名、密码、邮箱、手机号
name=input('用户名：')
password=input('密码：')
email=input('邮箱：')
number=input('手机号：')
#对每个输入使用.strip()去除首尾空格存入字典
name1=name.strip()
password1=(password.strip())
email1=email.strip()
number1=number.strip()
#验证用户名长度是否≥4个字符
if len(name1)<4:
    print('用户名太短不符合要求')
    yanzheng=1
#定义非法字符字符串 invalid_chars = "!@#$%^&*()+=[]{}|;:,.<>?/"
invalid_chars = "!@#$%^&*()+=[]{}|;:,.<>?/"
#遍历用户名中的每个字符，检测是否包含非法字符
b=0
for item in invalid_chars:
    for item2 in password1:
        if item == item2 or len(password)<8:
            print('密码非法或太短')
            yanzheng=1
            b=1
            break
    if b == 1:
        break
#检查邮箱是否包含"@"符号且只包含一个"@",邮箱长度是否在5-50个字符之间,不能以"@"或"."开头
c=email.find('@')
a=email1.count('@')
if len(email1)<5 or len(email1)>50 or c==0 or a!=1:
    print('邮箱错误')
    yanzheng=1
#检查手机号是否为数字且11位
number2=number1.isdigit()
if number2==False or len(number1)!=11:
    print('手机号错误')
    yanzheng=1
#使用%格式化生成："用户：xxx，注册时间：2025年"
if yanzheng==0:
    print('用户:%s,注册时间：2025年'%(name1))
    #使用str.format() 生成："联系方式：邮箱-xxx，手机-xxx"
    print('联系方式：邮箱-{0},手机-{1}'.format(email1,number1))


