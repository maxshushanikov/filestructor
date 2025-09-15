import os
from app.visitors import ProjectStructureVisitor
from app.components import FileComponent, DirectoryComponent

def test_visit_file_and_directory_and_save_report(tmp_path):
    # Создаем тестовый файл
    file_path = tmp_path / "file.txt"
    file_path.write_text("content")
    
    output_file = tmp_path / "report.txt"
    visitor = ProjectStructureVisitor(str(output_file))
    
    # Создаем компоненты
    dir_comp = DirectoryComponent(str(tmp_path))
    file_comp = FileComponent(str(file_path))
    
    # Посещаем компоненты
    visitor.visit_directory(dir_comp, "", True)
    visitor.visit_file(file_comp, "│   ", False)
    
    # Сохраняем отчет
    visitor.save_report()
    
    # Проверяем содержимое отчета
    report = output_file.read_text()
    assert "PROJECT STRUCTURE:" in report
    assert "FILE CONTENTS:" in report
    assert "file.txt" in report
    assert "content" in report