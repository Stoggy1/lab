from pytest import *
from account import *


class Test:
    abs = 0.001

    def setup_method(self):
        self.account = Account('Alex')

    def teardown_method(self):
        del self.account

    def test_init(self):
        assert self.account.get_name() == 'Alex'
        assert self.account.get_balance() == 0

    def test_deposit(self):
        assert self.account.deposit(0) is False
        assert self.account.get_balance() == 0
        assert self.account.deposit(-1) is False
        assert self.account.get_balance() == 0
        assert self.account.deposit(10) is True
        assert self.account.get_balance() == 10
        assert self.account.deposit(1.5) is True
        assert self.account.get_balance() == approx(11.5, abs=abs)

    def test_withdraw(self):
        assert self.account.withdraw(0) is False
        self.account.deposit(10)
        assert self.account.withdraw(11) is False
        assert self.account.withdraw(10) is True
        assert self.account.withdraw(-1) is False
        self.account.deposit(1.5)
        assert self.account.withdraw(1.5) is True
        assert self.account.get_balance() == 0
