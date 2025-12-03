import pytest
from zz import checkEqual


def test_single_wildcard_match():
    """Test that '.' matches a single character"""
    assert checkEqual("ro.t", "rokt") == True


def test_single_wildcard_no_match():
    """Test that '.' doesn't match when strings have different lengths"""
    assert checkEqual("r.t", "rokt") == False


def test_digit_wildcard_match():
    """Test that '2' matches exactly 2 characters"""
    assert checkEqual("r2t", "rokt") == True


def test_digit_wildcard_no_match():
    """Test that '2' doesn't match when pattern doesn't match"""
    assert checkEqual("r2k", "rokt") == False


def test_multidigit_wildcard_no_match():
    """Test that '12' matches exactly 12 characters (which doesn't match)"""
    assert checkEqual("r12t", "rokt") == False


def test_digit_wildcard_at_end():
    """Test digit wildcard at the end of pattern"""
    assert checkEqual("r2", "rab") == True

