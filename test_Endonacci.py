# This code is an example of pytest testing
import unittest

import pytest

from Endonacci import *
























def input(x, y):
    return type(x), type(y)



def test_dir(tmpdir):
    import os

    print(tmpdir)







    assert os.path.exists(tmpdir)


def test_dir2(tmpdir):
    import os
    import json

    print(tmpdir)
    assert os.path.exists(tmpdir)


class TestEndonacci(unittest.TestCase):
    @pytest.mark.initial_test
    def test_error(self):
        with pytest.raises(TypeError):
            endonacci("hello", 2)

    @pytest.mark.xfail
    def test_types(self):
        t1, t2 = input(2, 3)
        assert t1 == int and t2 == int

    @pytest.mark.skip(reason="no way of currently testing this")
    def test_all_n(self):
        for i in range(3, 9999):
            endonacci(2, i)
