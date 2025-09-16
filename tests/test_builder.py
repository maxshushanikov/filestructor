import os

from app.builder import ProjectBuilder


def test_build_tree_creates_structure(sample_project):
    # Добавляем исключенные директории
    excluded = {".git"}
    builder = ProjectBuilder(str(sample_project), excluded)
    root = builder.build_tree()

    assert root.name == os.path.basename(str(sample_project))

    # Проверяем наличие основных файлов и директорий
    assert any(child.name == "file1.txt" for child in root.children)
    assert any(child.name == "file2.py" for child in root.children)
    assert any(child.name == "subdir" for child in root.children)

    # Проверяем, что исключенные директории не добавлены
    assert not any(child.name == ".git" for child in root.children)

    # Проверяем содержимое поддиректории
    for child in root.children:
        if child.name == "subdir":
            assert any(grandchild.name == "file3.md" for grandchild in child.children)
            assert any(grandchild.name == "file4.png" for grandchild in child.children)
            break
    else:
        assert False, "subdir not found in root children"
