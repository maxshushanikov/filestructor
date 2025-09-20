import pytest


@pytest.fixture
def sample_project(tmp_path):
    """Fixture for creating a test project structure"""
    # Creates basic files
    (tmp_path / "file1.txt").write_text("Content of file1")
    (tmp_path / "file2.py").write_text("# Python file content")

    # Creates a subdirectory
    subdir = tmp_path / "subdir"
    subdir.mkdir()
    (subdir / "file3.md").write_text("# Markdown file")
    (subdir / "file4.png").touch()  # Simulates an image

    # Creates an excluded directory
    excluded = tmp_path / ".git"
    excluded.mkdir()
    (excluded / "config").touch()

    return tmp_path
