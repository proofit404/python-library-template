from pathlib import Path


def main():
    Path("examples").mkdir()
    Path("testing").mkdir()
    Path("tests").mkdir()


if __name__ == "__main__":
    main()
