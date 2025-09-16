"""
Filestructor CLI application entry point.
This script can be executed in two ways:
1. As a module within the package:
   python -m filestructor.app
2. As a standalone script:
   python app.py
"""

import os
import sys

# Handle imports depending on execution context
if __name__ == "__main__" or __package__ is None or __package__ == "":
    # Running as a standalone script — adjust sys.path
    d_name = os.path.dirname(__file__)
    sys.path.insert(0, os.path.abspath(os.path.join(d_name, "..")))
    from app.builder import ProjectBuilder
    from app.console import ConsoleInputHandler
    from app.visitors import ProjectStructureVisitor
else:
    # Running as part of the package
    from .builder import ProjectBuilder
    from .console import ConsoleInputHandler
    from .visitors import ProjectStructureVisitor


def main():
    """
    Main CLI entry point for Filestructor.
    Prompts the user for a directory path and output file name,
    builds the file system tree, and generates a report.
    """
    print("=== Filestructor ===")
    # Get user input
    directory = ConsoleInputHandler.get_directory()
    output_file = ConsoleInputHandler.get_output_file()
    # Directories to exclude from traversal
    excluded = {
        ".git",
        "__pycache__",
        ".idea",
        "venv",
        ".venv",
        "node_modules",
        ".vscode",
    }
    # Build the file system tree
    builder = ProjectBuilder(directory, excluded)
    root = builder.build_tree()
    # Visit the tree and generate the report
    visitor = ProjectStructureVisitor(output_file, excluded)
    root.accept(visitor)
    visitor.save_report()
    print(f"Report saved to: {output_file}")
    print(f"Excluded directories: {', '.join(excluded)}")


if __name__ == "__main__":
    main()
