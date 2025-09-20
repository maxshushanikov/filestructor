from app.components import DirectoryComponent, FileComponent
from app.visitors import ProjectStructureVisitor


def test_visit_file_and_directory_and_save_report(tmp_path):
    # Creates text file
    file_path = tmp_path / "file.txt"
    file_path.write_text("content")

    output_file = tmp_path / "report.txt"
    visitor = ProjectStructureVisitor(str(output_file))

    # Creates components
    dir_comp = DirectoryComponent(str(tmp_path))
    file_comp = FileComponent(str(file_path))

    # Visits the components
    visitor.visit_directory(dir_comp, "", True)
    visitor.visit_file(file_comp, "│   ", False)

    # Saves the report
    visitor.save_report()

    # Checks the contents of the report
    report = output_file.read_text()
    assert "PROJECT STRUCTURE:" in report
    assert "FILE CONTENTS:" in report
    assert "file.txt" in report
    assert "content" in report
