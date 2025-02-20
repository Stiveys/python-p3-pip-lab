# lib/testing_env/module_test.py

import requests
import pytest

def requests_version():
    return requests.__version__

def pytest_version():
    return pytest.__version__

def test_requests_version():
    assert requests_version() == "2.32.3"

def test_pytest_version():
    assert pytest_version() == "8.3.4"