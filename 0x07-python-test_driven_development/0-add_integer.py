#!/usr/bin/python3
# 0-add_integer.py
"""Defines an integer addition function."""

def add_integer(a, b=98):
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer or float")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer or float")
    a = int(a) if type(a) == float else a
    b = int(b) if type(b) == float else b

    return a + b
