class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no
        print('Total balance = ',self.get_balance())
    
    def credit(self,amount):
        self.balance += amount
        print('Rs', amount, 'was credited .')
        print('Total balance = ',self.get_balance())


    def debit(self,amount):
        self.balance -= amount
        print('Rs', amount, 'was debited .')
        print('Total balance = ',self.get_balance())

        
    def get_balance(self):
        return self.balance

Account1 = Account(100000000,456)
Account1.debit(float(input('Enter the amount to debit:')))
Account1.credit(float(input('Enter the amount to be credited:  ')))


        
        
