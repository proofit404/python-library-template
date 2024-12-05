# Installation

{% if not cookiecutter.is_private %}The `{{ cookiecutter.project_name }}` library is available on PyPI.

{% endif %}```bash
pip install -U {{ cookiecutter.project_name }}
```

We use [semantic release](https://semantic-release.gitbook.io/semantic-release/)
to publish packages as soon as pull requests land to the release branch. It's
not necessary to use develompment version of the library.

We officially support the latest minor release of CPython interpreter.
