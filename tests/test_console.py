import builtins

from app.console import ConsoleInputHandler


def test_get_directory_valid(tmp_path, monkeypatch):
    monkeypatch.setattr(builtins, "input", lambda _: str(tmp_path))
    assert ConsoleInputHandler.get_directory() == str(tmp_path)


def test_get_directory_invalid(monkeypatch, tmp_path):
    # Сначала вводим невалидные пути, затем валидный
    inputs = iter(["/invalid/path", "/invalid/path2", str(tmp_path)])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    assert ConsoleInputHandler.get_directory() == str(tmp_path)


def test_get_output_file_default(monkeypatch):
    monkeypatch.setattr(builtins, "input", lambda _: "")
    assert ConsoleInputHandler.get_output_file() == "project_report.txt"


def test_get_output_file_custom(monkeypatch):
    monkeypatch.setattr(builtins, "input", lambda _: "custom.txt")
    assert ConsoleInputHandler.get_output_file() == "custom.txt"
