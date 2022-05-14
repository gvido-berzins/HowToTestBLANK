
From `gunicorn:tests/test_config.py`
- https://github.com/benoitc/gunicorn

Testing if environment variable set the configuration attribute

```python
def test_load_enviroment_variables_config(monkeypatch):
    monkeypatch.setenv("GUNICORN_CMD_ARGS", "--workers=4")
    with AltArgs():
        app = NoConfigApp()
    assert app.cfg.workers == 4
```

Testing if the CLI overrides the set environment variables with pytest monkeypatch

```python
def test_cli_overrides_enviroment_variables_module(monkeypatch):
    monkeypatch.setenv("GUNICORN_CMD_ARGS", "--workers=4")
    with AltArgs(["prog_name", "-c", cfg_file(), "--workers", "3"]):
        app = NoConfigApp()
    assert app.cfg.workers == 3
```
