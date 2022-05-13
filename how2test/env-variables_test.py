"""
Learned from assotile
"""
import os
import unittest


def greet() -> None:
    username = os.environ["USER"]  # use getpass.getuser()
    print(f"hello {username}")


def main() -> int:
    greet()
    return 0


def test_greet_using_pytest(capsys, monkeypatch):
    """Using pytest built-in.
    Patched until monkeypatch is broken down, not certain"""
    monkeypatch.setenv("USER", "tester")
    greet()
    out, err = capsys.readouterr()
    assert out == "hello tester\n"


def test_greet_using_unittest(capsys):
    """Considered to be a better practice, because it only mocks for a known duration"""
    with unittest.mock.patch.dict(os.environ, {"USER": "tester"}):
        greet()
    out, err = capsys.readouterr()
    assert out == "hello tester\n"


if __name__ == "__main__":
    raise SystemExit(main())
