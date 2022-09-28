'''Tests for utility functions'''

import pytest
import pickle

import alchemtest


def test_version():
    assert alchemtest.__version__


@pytest.fixture
def bunch():
    return alchemtest.Bunch(data=[0, 1, 1, 2, 3, 5], DESCR="Fibonacci")

class TestBunch:
    def test_getattr_key(self, bunch):
        assert bunch["DESCR"] == "Fibonacci"

    def test_getattr_key(self, bunch):
        assert bunch.DESCR == "Fibonacci"

    def test_setattr_key(self, bunch):
        bunch["foo"] = "bar"
        assert bunch.foo == "bar"

    def test_setattr_dot(self, bunch):
        bunch.foo = "bar"
        assert bunch.foo == "bar"

    def test_missing_attr_AttributeError(self, bunch):
        with pytest.raises(AttributeError):
            bunch.unknown_attribute

    def test_missing_key_KeyError(self, bunch):
        with pytest.raises(KeyError):
            bunch["unknown key"]

    def test_dir(self, bunch):
        bunch.a = "additional"
        assert sorted(dir(bunch)) == ["DESCR", "a", "data"]

    def test_serialize(self, bunch):
        bunch_copy = pickle.loads(pickle.dumps(bunch))
        assert bunch_copy == bunch
