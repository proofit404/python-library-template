from {{ cookiecutter.private_module_name }}.exceptions import {{ cookiecutter.exception_name }}


def func():
    """Raise exception."""
    raise {{ cookiecutter.exception_name }}
