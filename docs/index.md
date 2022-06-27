# python-library-template

Python library template focused on code quality and security.

## GitHub repository

Create github repository for your project.

![Create New Repository](./images/create_new_repository.png)

Create issue labels:

![Issue Labels](./images/issue_labels.png)

## Azure Pipelines

Create azure project.

![Create Azure Project](./images/create_azure_project.png)

Enable pipelines option in azure project.

You can create starter pipeline for that purpose.

![Create Azure Pipeline](./images/create_azure_pipeline.png)

## Review Bot

Create GitHub bot user: https://danger.systems/js/guides/getting_started.html#github

Generate personal access token for that user: https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token

This token should have only `public_repo` access level.

![Generate Danger Token](./images/generate_danger_token.png)

Add public `DANGER_GITHUB_TOKEN` variable to the azure pipeline.

![Add Danger Token Variable](./images/add_danger_token_variable.png)

## Semantic Release

Generate API token for Python Package Index: https://pypi.org/help/#apitoken

![Generate PyPI Token](./images/generate_pypi_token.png)

Add **secret** `SEMANTIC_RELEASE_PYPI_TOKEN` variable to the azure pipeline.

![Add PyPI Token Variable](./images/add_pypi_token_variable.png)

Generate personal access token for user with push access to the repository: https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token

This token should have only `public_repo` access level if you work on open source project.

![Generate Commit Token](./images/generate_commit_token.png)

Add **secret** `SEMANTIC_RELEASE_GITHUB_TOKEN` variable to the azure pipeline.

![Add Commit Token Variable](./images/add_commit_token_variable.png)

**Ensure** you are not allow builds of forks to access secret variables.

![Ensure Secrets Settings](./images/ensure_secrets_settings.png)

## Local repository

First, install dependencies:

```bash
$ pip install cruft
```

Create project:

```bash
$ echo $DANGER_GITHUB_API_TOKEN | base64
$ cruft create https://github.com/proofit404/python-library-template
```

Initialize git repository:

```bash
$ cd the-library
$ git init
```

Create `release` branch:

```bash
$ git checkout -b release
```

Commit created project to the repository:

```bash
$ git add .
$ git commit -m 'Hello world.'
```

Configure origin repository on GitHub:

```bash
$ git remote add origin git@github.com:proofit404/the-library.git
```

Push newly created project to the GitHub:

```bash
$ git push origin release
```

## GitHub repository settings

Change default branch of the repository:

![Change Default Branch](./images/change_default_branch.png)

Configure branch protection rule the same way for both `release` and `develop` branches:

![Branch Protection Rules](./images/branch_protection_rules.png)

Remove `main` branch:

![Remove Main Branch](./images/remove_main_branch.png)
