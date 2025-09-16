import os
import sys

# Handle imports depending on execution context
if __name__ == "__main__" or __package__ is None or __package__ == "":
    # Running as a standalone script — adjust sys.path
    d_name = os.path.dirname(__file__)
    sys.path.insert(0, os.path.abspath(os.path.join(d_name, "..")))
    from app.components import DirectoryComponent, FileComponent
else:
    # Running as part of the package
    from .components import DirectoryComponent, FileComponent


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
        if not os.path.exists(path):
            return None

        if os.path.isfile(path):
            return FileComponent(path)

        directory = DirectoryComponent(path)
        if directory.name in self.excluded_dirs:
            return directory

        try:
            items = os.listdir(path)
            ex_dir = self.excluded_dirs
            dirs = [
                i
                for i in items
                if os.path.isdir(os.path.join(path, i)) and i not in ex_dir
            ]
            files = [i for i in items if os.path.isfile(os.path.join(path, i))]
            for d in sorted(dirs):
                component = os.path.join(path, d)
                directory.add_child(self._build_component(component))
            for f in sorted(files):
                directory.add_child(FileComponent(os.path.join(path, f)))
        except PermissionError:
            # Skip directories without read permissions
            print(f"Warning: Permission denied for {path}. Skipping.")
        except FileNotFoundError:
            # Handle case where directory no longer exists
            print(f"Warning: Directory {path} no longer exists. Skipping.")
        except Exception as e:
            print(f"Error processing {path}: {str(e)}")

        return directory
