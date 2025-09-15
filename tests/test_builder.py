import os
import tempfile
from app.builder import ProjectBuilder

def test_build_tree_creates_structure():
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = os.path.join(tmpdir, "file.txt")
        with open(file_path, "w") as f:
            f.write("data")

        builder = ProjectBuilder(tmpdir)
        root = builder.build_tree()
        assert root.name == os.path.basename(tmpdir)
        assert any(child.name == "file.txt" for child in root.children)
