import builtins
import tempfile
from app import app

def test_main_runs(monkeypatch):
    with tempfile.TemporaryDirectory() as tmpdir:
        inputs = iter([tmpdir, "report.txt"])
        monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
        app.main()
