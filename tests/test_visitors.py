import os
import tempfile
from app.visitors import ProjectStructureVisitor
from app.components import FileComponent, DirectoryComponent

def test_visit_file_and_directory_and_save_report():
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = os.path.join(tmpdir, "file.txt")
        with open(file_path, "w") as f:
            f.write("content")

        output_file = os.path.join(tmpdir, "report.txt")
        visitor = ProjectStructureVisitor(output_file)

        dir_comp = DirectoryComponent(tmpdir)
        file_comp = FileComponent(file_path)

        visitor.visit_directory(dir_comp, "", True)
        visitor.visit_file(file_comp, "", True)
        visitor.save_report()

        with open(output_file, "r", encoding="utf-8") as f:
            report = f.read()

        assert "PROJECT STRUCTURE" in report
        assert "FILE CONTENTS" in report
        assert "file.txt" in report
