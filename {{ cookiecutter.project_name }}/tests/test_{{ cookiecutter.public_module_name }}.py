"""Tests related to {{ cookiecutter.public_module_name }} module."""
from {{ cookiecutter.public_module_name }}.exceptions import {{ cookiecutter.exception_name }}


def test_exception():
    """`{{ cookiecutter.exception_name }}` should be Exception subclass."""
    assert issubclass({{ cookiecutter.exception_name }}, Exception)
