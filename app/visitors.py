import sys
from file_utils import FileUtils

class FileSystemVisitor:
    """Abstract base class for file system visitors."""

    def visit_file(self, file, prefix, is_last):
        raise NotImplementedError

    def visit_directory(self, directory, prefix, is_last):
        raise NotImplementedError


class ProjectStructureVisitor(FileSystemVisitor):
    """
    Visitor that generates a project structure report including file contents.
    """

    def __init__(self, output_file, excluded_dirs=None):
        """
        Args:
            output_file (str): Path to the output report file.
            excluded_dirs (set): Directory names to exclude from traversal.
        """
        self.output_file = output_file
        self.structure = []
        self.content = []
        self.excluded_dirs = excluded_dirs or set()
        self.type_map = self._create_type_map()

    def _create_type_map(self):
        """Create a mapping of file extensions to type descriptions."""
        return {
            '.png': ' [image]',
            '.jpg': ' [image]',
            '.mp3': ' [audio]',
            '.mp4': ' [video]',
            '.pdf': ' [document]',
            '.zip': ' [archive]',
            '.exe': ' [executable]'
        }

    def visit_file(self, file, prefix, is_last):
        """Process a file and add it to the structure list."""
        connector = "└── " if is_last else "├── "
        desc = FileUtils.get_file_type_description(file.path, self.type_map)
        self.structure.append(f"{prefix}{connector}{file.name}{desc}")
        self.content.append(
            f"\n\n{'='*50}\nFile: {file.path}\n{'='*50}\n{FileUtils.read_file_content(file.path)}"
        )

    def visit_directory(self, directory, prefix, is_last):
        """Process a directory and add it to the structure list."""
        if directory.name in self.excluded_dirs:
            return
        connector = "└── " if is_last else "├── "
        self.structure.append(f"{prefix}{connector}{directory.name}/")

    def save_report(self):
        """Save the generated report to the output file."""
        try:
            with open(self.output_file, 'w', encoding='utf-8') as f:
                f.write("PROJECT STRUCTURE:\n")
                f.write("\n".join(self.structure))
                f.write("\n\nFILE CONTENTS:")
                f.write("".join(self.content))
        except Exception as e:
            print(f"ERROR saving report: {e}")
            sys.exit(1)
