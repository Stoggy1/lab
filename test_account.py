import pytest
from account import *

class Test:
    def setup_method(self, name):
        self.account = Account('Alex')

    def test_init(self):
        assert self.account.get_name() == 'Alex'
        assert self.account.get_balance() == 0

    def test_deposit(self):
        assert self.account.deposit(0) is False
        assert self.account.deposit(10) is True

    def test_withdraw(self):
        assert self.account.withdraw(0) is False
        self.account.deposit(10)
        assert self.account.withdraw(11) is False
        assert self.account.withdraw(10) is True
