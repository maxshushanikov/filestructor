"""
Filestructor — project structure generator with file content inspection.

Usage:
- As a library: import ProjectBuilder, ProjectStructureVisitor, etc.
- As a CLI: install the package and run `filestructor` or `python -m filestructor`
"""

__version__ = "0.1.0"
__author__ = "Maxim Shushanikov"
__license__ = "MIT"

from .file_utils import FileUtils
from .components import FileSystemComponent, FileComponent, DirectoryComponent
from .visitors import FileSystemVisitor, ProjectStructureVisitor
from .builder import ProjectBuilder
from .console import ConsoleInputHandler
from .app import main  # Import CLI entry point from app.py

__all__ = [
    "FileUtils",
    "FileSystemComponent",
    "FileComponent",
    "DirectoryComponent",
    "FileSystemVisitor",
    "ProjectStructureVisitor",
    "ProjectBuilder",
    "ConsoleInputHandler",
    "main",
]
