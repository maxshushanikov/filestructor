import pytest


@pytest.fixture
def sample_project(tmp_path):
    """Fixture для создания тестовой структуры проекта"""
    # Создаем базовые файлы
    (tmp_path / "file1.txt").write_text("Content of file1")
    (tmp_path / "file2.py").write_text("# Python file content")

    # Создаем поддиректорию
    subdir = tmp_path / "subdir"
    subdir.mkdir()
    (subdir / "file3.md").write_text("# Markdown file")
    (subdir / "file4.png").touch()  # Имитируем изображение

    # Создаем исключаемую директорию
    excluded = tmp_path / ".git"
    excluded.mkdir()
    (excluded / "config").touch()

    return tmp_path
