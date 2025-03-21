# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

**{% if not cookiecutter.is_private %}[PyPI]({{ cookiecutter.__pypi_project }}) |
{% endif %}[Documentation]({{ cookiecutter.__documentation_url }}) |
[Source Code]({{ cookiecutter.__github_repository }}) |
[Task Tracker]({{ cookiecutter.__issues_url }})**

## Questions

If you have any questions, feel free to create an issue in our
[Task Tracker]({{ cookiecutter.__issues_url }}). We have the
[question label]({{ cookiecutter.__issues_url }}?q=is%3Aopen+is%3Aissue+label%3Aquestion)
exactly for this purpose.

## Enterprise support

If you have an issue with any version of the library, you can apply for a paid
enterprise support contract. This will guarantee you that no breaking changes
will happen to you. No matter how old version you're using at the moment. All
necessary features and bug fixes will be backported in a way that serves your
needs.

Please contact [{{ cookiecutter.author_email }}](mailto:{{ cookiecutter.author_email }}) if you're
interested in it.

## License

`{{ cookiecutter.project_name }}` library is offered under {% if cookiecutter.is_private %}proprietary{% else %}the two clause BSD{% endif %} license.
