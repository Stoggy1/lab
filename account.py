class Account:
    def __init__(self, name: str) -> None:
        self.__account_name = name
        self.__account_balance = 0

    def get_name(self) -> str:
        return self.__account_name

    def get_balance(self) -> int:
        return self.__account_balance

    def deposit(self, amount: float) -> bool:
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self, amount: float) -> bool:
        if amount <= 0 or amount > self.get_balance():
            return False
        else:
            self.__account_balance -= amount
            return True