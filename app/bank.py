import threading


class InsufficientFunds(Exception):
    pass


class Account:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance
        self._lock = threading.Lock()

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("amount must be positive")
        with self._lock:
            self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("amount must be positive")
        with self._lock:
            if amount > self.balance:
                raise InsufficientFunds()
            self.balance -= amount


def transfer(src, dst, amount):
    src.withdraw(amount)
    dst.deposit(amount)