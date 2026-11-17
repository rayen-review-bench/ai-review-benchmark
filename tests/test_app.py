import pytest
from app.auth import hash_password, verify_password
from app.bank import Account, transfer, InsufficientFunds
from app.utils import paginate, average


def test_password_roundtrip():
    h = hash_password("secret")
    assert verify_password("secret", h)
    assert not verify_password("wrong", h)


def test_transfer():
    a, b = Account("a", 100), Account("b", 0)
    transfer(a, b, 40)
    assert (a.balance, b.balance) == (60, 40)


def test_insufficient_funds():
    with pytest.raises(InsufficientFunds):
        Account("a", 10).withdraw(50)


def test_paginate_first_page():
    assert paginate(list(range(25)), 1) == list(range(10))


def test_average_empty():
    assert average([]) == 0.0