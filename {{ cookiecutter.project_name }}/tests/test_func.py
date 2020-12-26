"""Tests related to {{ cookiecutter.public_module_name }}.func function."""
import pytest

from {{ cookiecutter.public_module_name }} import func
from {{ cookiecutter.public_module_name }}.exceptions import {{ cookiecutter.exception_name }}


def test_func():
    """`func` should raise `{{ cookiecutter.exception_name }}`."""
    with pytest.raises({{ cookiecutter.exception_name }}):
        func()
