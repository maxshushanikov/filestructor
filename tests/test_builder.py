import os

from app.builder import ProjectBuilder


def test_build_tree_creates_structure(sample_project):
    # Adds excluded directories
    excluded = {".git"}
    builder = ProjectBuilder(str(sample_project), excluded)
    root = builder.build_tree()

    assert root.name == os.path.basename(str(sample_project))

    # Checks the presence of basic files and directories
    assert any(child.name == "file1.txt" for child in root.children)
    assert any(child.name == "file2.py" for child in root.children)
    assert any(child.name == "subdir" for child in root.children)

    # Checks that excluded directories are not added
    assert not any(child.name == ".git" for child in root.children)

    # Checks the contents of the subdirectory
    for child in root.children:
        if child.name == "subdir":
            cn = child.children
            assert any(grandchild.name == "file3.md" for grandchild in cn)
            assert any(grandchild.name == "file4.png" for grandchild in cn)
            break
    else:
        assert False, "subdir not found in root children"
