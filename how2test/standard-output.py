"""
Summary:
    Using pytest capsys fixture to validate standard output and error
Description:
    An example of a command-line test, create after watching Anthony Explains
    [video](https://www.youtube.com/watch?v=sv46294LoP8)
"""
import sys
from argparse import ArgumentParser


def main(argv: list[str] = None) -> int:
    parser = ArgumentParser()
    parser.add_argument("name")
    args = parser.parse_args(argv)
    if args.name.strip() == "":
        print("No name provided!", file=sys.stderr)
        return 1

    print(f"Hello {args.name}!")
    return 0


def test_main_happy_path(capsys):
    """Test whether the expected happy path is successful"""
    main(["Gvido"])
    out, err = capsys.readouterr()
    assert out == "Hello Gvido!\n"
    assert not err


def test_main_error(capsys):
    """Test whether a specific message is printed to standard error stream"""
    main([""])
    out, err = capsys.readouterr()
    assert not out
    assert err == "No name provided!\n"


if __name__ == "__main__":
    raise SystemExit(main())
