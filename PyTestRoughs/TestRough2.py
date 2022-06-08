import pytest


def test_total_divisible_by_11(input_total):
    assert input_total % 11 == 0


def test_total_divisible_by_12(input_total):
    assert input_total % 12 == 0
