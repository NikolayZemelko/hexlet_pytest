#!/usr/bin/env python3

from hexlet_pytest.example import reverse

def test_reverse():
    assert reverse("Hello") == "olleH"
