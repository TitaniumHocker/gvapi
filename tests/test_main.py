# -*- coding: utf-8 -*-
import pytest


@pytest.mark.parametrize('data', ('a', 'b', 'c'))
def test_dummy(data):
    assert data == data
