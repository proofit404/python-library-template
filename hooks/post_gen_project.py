from pathlib import Path


def main():
    Path("examples").mkdir()
    Path("testing").mkdir()
    Path("tests").mkdir()

    Path("README.md").symlink_to("docs/index.md")

    if "{% if cookiecutter.is_private %}T{% endif %}":
        Path("LICENSE").unlink()


if __name__ == "__main__":
    main()
