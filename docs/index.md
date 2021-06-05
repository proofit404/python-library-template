# python-library-template

Python library template focused on code quality and security.

## Features

- 

## Usage

### Local repository

First, install dependencies:

```bash
$ pip install cookiecutter
```

Create project:

```bash
$ cookiecutter gh:proofit404/python-library-template
```

### GitHub repository

Create github repository for your project.

### Azure Pipelines

Create azure project. Enable pipelines option in azure project.

### Review Bot

Create GitHub bot user: https://danger.systems/js/guides/getting_started.html#github

Generate personal access token for that user: https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token

This token should have only `public_repo` access level.

![Generate Danger Token](./images/generate_danger_token.png)

Add public `DANGER_GITHUB_TOKEN` variable to the azure pipeline.

![Add Danger Token Variable](./images/add_danger_token_variable.png)

### Semantic Release

`SEMANTIC_RELEASE_PYPI_TOKEN`

`SEMANTIC_RELEASE_GITHUB_TOKEN`