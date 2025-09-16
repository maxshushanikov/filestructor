"""
Filestructor — project structure generator with file content inspection.
Usage:
- As a library: import ProjectBuilder, ProjectStructureVisitor, etc.
- As a CLI: install the package and run `filestructor` or `python -m filestru
  ctor`
"""

__version__ = "0.1.0"
__author__ = "Maxim Shushanikov"
__license__ = "MIT"
from .builder import ProjectBuilder
from .components import DirectoryComponent, FileComponent, FileSystemComponent
from .console import ConsoleInputHandler
from .file_utils import FileUtils
from .visitors import FileSystemVisitor, ProjectStructureVisitor

# УБРАТЬ ЭТУ СТРОКУ: from .app import main
__all__ = [
    "FileUtils",
    "FileSystemComponent",
    "FileComponent",
    "DirectoryComponent",
    "FileSystemVisitor",
    "ProjectStructureVisitor",
    "ProjectBuilder",
    "ConsoleInputHandler",
]
