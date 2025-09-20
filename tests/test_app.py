import builtins

from app.app import main


def test_main_runs(monkeypatch, tmp_path):
    inputs = iter([str(tmp_path), "report.txt"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    main()
