import os
from components import FileComponent, DirectoryComponent

class ProjectBuilder:
    """
    Builds a hierarchical file system tree starting from a given root path.
    """

    def __init__(self, root_path, excluded_dirs=None):
        """
        Args:
            root_path (str): Path to the root directory.
            excluded_dirs (set): Directory names to exclude from traversal.
        """
        self.root_path = root_path
        self.excluded_dirs = excluded_dirs or set()

    def build_tree(self):
        """Build the complete file system tree."""
        return self._build_component(self.root_path)

    def _build_component(self, path):
        """Recursively build a file or directory component."""
        if os.path.isfile(path):
            return FileComponent(path)

        directory = DirectoryComponent(path)
        if directory.name in self.excluded_dirs:
            return directory

        try:
            items = os.listdir(path)
            dirs = [i for i in items if os.path.isdir(os.path.join(path, i)) and i not in self.excluded_dirs]
            files = [i for i in items if os.path.isfile(os.path.join(path, i))]

            for d in sorted(dirs):
                directory.add_child(self._build_component(os.path.join(path, d)))
            for f in sorted(files):
                directory.add_child(FileComponent(os.path.join(path, f)))
        except PermissionError:
            # Skip directories without read permissions
            pass

        return directory
