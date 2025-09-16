import os
from abc import ABC, abstractmethod


class FileSystemComponent(ABC):
    """Abstract base class for file system components (files and directories)."""

    def __init__(self, path):
        self.path = path
        self.name = os.path.basename(path)

    @abstractmethod
    def accept(self, visitor, prefix="", is_last=True):
        """Accept a visitor for processing this component."""
        pass


class FileComponent(FileSystemComponent):
    """Represents a file in the file system."""

    def accept(self, visitor, prefix="", is_last=True):
        visitor.visit_file(self, prefix, is_last)


class DirectoryComponent(FileSystemComponent):
    """Represents a directory in the file system."""

    def __init__(self, path):
        super().__init__(path)
        self.children = []

    def add_child(self, component):
        """Add a child component (file or directory) to this directory."""
        self.children.append(component)

    def accept(self, visitor, prefix="", is_last=True):
        visitor.visit_directory(self, prefix, is_last)
        for i, child in enumerate(self.children):
            child.accept(
                visitor,
                prefix + ("    " if is_last else "│   "),
                i == len(self.children) - 1,
            )
