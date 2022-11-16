class Account:
    """
    Class representing a bank account
    """
    def __init__(self, name: str) -> None:
        """
        Constructor to create details for Account object
        :param name: Account's name
        """
        self.__account_name = name
        self.__account_balance = 0

    def get_name(self) -> str:
        """
        Getter Method used to return Account Name
        :return: Account's Name
        """
        return self.__account_name

    def get_balance(self) -> int:
        """
        Getter method used to return Account Balance
        :return:  Account's balance
        """
        return self.__account_balance

    def deposit(self, amount: float) -> bool:
        """
        Method used to Add money to Account Balance
        :param amount: Amount person wants to add
        :return: True or False
        """
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self, amount: float) -> bool:
        """
        Method used to Remove money from Account Balance
        :param amount: Amount person wants to take out
        :return: True or False
        """
        if amount <= 0 or amount > self.get_balance():
            return False
        else:
            self.__account_balance -= amount
            return True