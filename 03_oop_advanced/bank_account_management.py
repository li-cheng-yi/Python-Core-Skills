'''创建一个BankAccount类，包含以下属性：
账户持有人姓名(account_holder)
账户余额(balance)
账户号码(account_number)
实现以下方法：
__init__(): 构造函数，初始化账户信息
deposit(amount): 存款方法，将指定金额存入账户
withdraw(amount): 取款方法，从账户取出指定金
get_balance(): 查询当前余额
display_info(): 显示账户基本信息
功能要求
存款时金额必须为正数
取款时金额不能超过账户余额
账户号码可以简单使用Python内置的id()函数生成
余额属性应设置为受保护属性(使用单个下划线前缀)
测试要求
在main()函数中：
创建一个初始余额为1000元的账户
演示存款500元
演示取款200元
演示取款超过余额的情况(如2000元)
显示最终账户信息'''
class BankAccount:
    def __init__(self,account_holder,balance,account_number):
        self.account_holder=account_holder
        self._balance=balance
        self.account_number=account_number
    def deposit(self,amount):
        if amount>0:
            self._balance+=amount
        else:
            print('存款时金额必须为正数')
    def withdraw(self,amount):
        if amount<=self._balance:
            self._balance-=amount
        else:
            print('取款时金额超过账户余额')
    def get_balance(self):
        print('当前余额为：',self._balance)
    def display_info(self):
        print('姓名:',self.account_holder,'号码:',self.account_number)
def main():
    account1=BankAccount('lcy',1000,11111111111)
    account1.deposit(500)
    account1.get_balance()
    account1.withdraw(200)
    account1.get_balance()
    account1.withdraw(2000)
    account1.display_info()
main()

