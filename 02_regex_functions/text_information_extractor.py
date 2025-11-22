import re
original_information='''联系人信息：
张三的电话是138-1234-5678，邮箱zhangsan@email.com
李四的电话是111-8765-4321，邮箱lisi123@company.cn
王五的电话是137-5555-8888，邮箱wangwu.test@university.edu
重要日期：
项目启动：2023-11-15，截止日期：2024-02-28'
会议时间：2023年12月05日 14:30
敏感信息：
信用卡号：6222-1234-5678-9012，身份证号：110101199001011234
密码：abc123，安全码：789'''
#使用re.search在文本中查找第一个出现的邮箱地址
pattern0='邮箱.*'
email_search=re.search(pattern0,original_information)
if email_search:
    print(email_search.group())
#使用re.findall提取文本中所有的日期格式（包括YYYY-MM-DD和YYYY年MM月DD日）
pattern1=r'\d{4}-\d{2}-\d{2}'
pattern2=r'\d{4}年\d{2}月\d{2}日'
date_findall1=re.findall(pattern1,original_information)
date_findall2=re.findall(pattern2,original_information)
date_findall=date_findall1+date_findall2
print(date_findall)
#使用re.sub将所有的电话号码替换为"[电话已隐藏]"
pattern3=r'1\d{2}-\d{4}-\d{4}'
ph_sub=re.sub(pattern3,' 电话已隐藏 ',original_information)
print(ph_sub)
#使用re.split按换行符分割文本
pattern5='\n'
original_information=re.split(pattern5,original_information)
print(original_information)
