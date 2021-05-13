# {{ cookiecutter.public_module_name.replace('_', ' ')|capitalize }}

[![azure-devops-builds](https://img.shields.io/azure-devops/build/{{ cookiecutter.github_user }}/{{ cookiecutter.project_name }}/{{ cookiecutter.azure_definition_id }}?style=flat-square)](https://dev.azure.com/{{ cookiecutter.github_user }}/{{ cookiecutter.project_name }}/_build/latest?definitionId={{ cookiecutter.azure_definition_id }}&branchName=master)
[![azure-devops-coverage](https://img.shields.io/azure-devops/coverage/{{ cookiecutter.github_user }}/{{ cookiecutter.project_name }}/{{ cookiecutter.azure_definition_id }}?style=flat-square)](https://dev.azure.com/{{ cookiecutter.github_user }}/{{ cookiecutter.project_name }}/_build/latest?definitionId={{ cookiecutter.azure_definition_id }}&branchName=master)
[![pypi](https://img.shields.io/pypi/v/{{ cookiecutter.project_name }}?style=flat-square)]({{ cookiecutter.pypi_project }})
[![python](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_name }}?style=flat-square)]({{ cookiecutter.pypi_project }})

{{ cookiecutter.project_description }}

**[Documentation]({{ cookiecutter.documentation_url }}) |
[Source Code]({{ cookiecutter.github_repository }}) |
[Task Tracker]({{ cookiecutter.issues_url }})**

A paragraph of text explaining the goal of the library…

## Pros

- A feature
- B feature
- etc

## Example

A line of text explaining snippet below…

```pycon

>>> from {{ cookiecutter.public_module_name }} import *

```

## Questions

If you have any questions, feel free to create an issue in our
[Task Tracker]({{ cookiecutter.issues_url }}). We have the
[question label]({{ cookiecutter.issues_url }}?q=is%3Aopen+is%3Aissue+label%3Aquestion)
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

`{{ cookiecutter.project_name }}` library is offered under the two clause BSD license.

<p align="center">&mdash; ⭐ &mdash;</p>
<p align="center"><i>The <code>{{ cookiecutter.project_name }}</code> library is part of the SOLID python family.</i></p>
