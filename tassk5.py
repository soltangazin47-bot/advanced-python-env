class BankAccount:
    def __init__(self, o, b=0):
        self.__o = o
        self.__b = b

    def deposit(self, a):
        if a <= 0:
            print("Deposit must be positive")
        else:
            self.__b += a

    def withdraw(self, a):
        if a > self.__b:
            print("Insufficient funds")
        else:
            self.__b -= a

    def get_balance(self):
        return self.__b


x = BankAccount("Ali", 500)
x.deposit(200)
x.withdraw(100)
print(x.get_balance())
