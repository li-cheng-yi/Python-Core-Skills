import re
#使用字符串方法处理用户输入的数学表达式,去除输入字符串中多余的空格
biaodashi=input('请输入数学表达式').strip()
#验证输入是否为空，为空时给出提示信息
if biaodashi=='':
    print('表达式为空')
'''使用正则表达式验证输入是否为有效的数学表达式
    允许的运算符：+, -, *, /, %
    禁止除数字和运算符外的其他字符'''
yunsuanfu=r'[+,-,*,/,%]'
if re.search(yunsuanfu,biaodashi)==None:
    print('表达式没有运算符')
try:
    biaodashi1=re.sub(r'[+,-,*,/,%]','',biaodashi)
    biaodashi2=float(biaodashi1)
except ValueError:#处理类型转换错误（ValueError）
    print('禁止除数字和运算符外的其他字符')
else:
    try:
        biaodashi3 = eval(biaodashi)
    except ZeroDivisionError:  # 处理除零错误（ZeroDivisionError）
        print('除数不能为0')
    except BaseException:
        print('未知错误')
    else:
        print('计算结果:', biaodashi3)




