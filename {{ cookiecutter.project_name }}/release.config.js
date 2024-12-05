module.exports = {
  repositoryUrl: "{{ cookiecutter.__github_repository }}",
  branches: ["release"],
  tagFormat: "${version}",
  plugins: [
    "@semantic-release/commit-analyzer",
    [
      "@semantic-release/release-notes-generator",
      {
        linkCompare: false,
        linkReferences: false,
      },
    ],
    [
      "@semantic-release/changelog",
      {
        changelogFile: "docs/changelog.md",
      },
    ],
    [
      "@semantic-release/exec",
      {
        prepareCmd:
          "./scripts/check ; " +
          "poetry version ${nextRelease.version} && " +
          "npm version --no-git-tag-version ${nextRelease.version} && " +
          "poetry build",{% if not cookiecutter.is_private %}
        publishCmd: "poetry publish",{% endif %}
      },
    ],
    [
      "@semantic-release/git",
      {
        assets: ["docs/changelog.md", "pyproject.toml", "package.json"],
      },
    ],
    [
      "@semantic-release/github",
      {
        assets: [{ path: "dist/*.whl" }, { path: "dist/*.tar.gz" }],
      },
    ],
  ],
};
