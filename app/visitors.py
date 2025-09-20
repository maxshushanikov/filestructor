import logging

from .file_utils import FileUtils

logger = logging.getLogger(__name__)


class FileSystemVisitor:
    """Base class for file system visitors."""

    def visit_file(self, file, prefix, is_last):
        raise NotImplementedError

    def visit_directory(self, directory, prefix, is_last):
        raise NotImplementedError


class ProjectStructureVisitor(FileSystemVisitor):
    """
    Generates a report on the project structure with the contents of the files.
    """

    def __init__(self, output_file, excluded_dirs=None):
        self.output_file = output_file
        self.structure = []
        self.content = []
        self.excluded_dirs = excluded_dirs or set()
        self.type_map = self._create_type_map()

    def _create_type_map(self):
        """Creates a map of file extensions to their descriptions."""
        return {
            ".png": " [image]",
            ".jpg": " [image]",
            ".jpeg": " [image]",
            ".gif": " [image]",
            ".svg": " [image]",
            ".mp3": " [audio]",
            ".wav": " [audio]",
            ".mp4": " [video]",
            ".avi": " [video]",
            ".pdf": " [document]",
            ".doc": " [document]",
            ".docx": " [document]",
            ".xlsx": " [spreadsheet]",
            ".pptx": " [presentation]",
            ".zip": " [archive]",
            ".gz": " [archive]",
            ".exe": " [executable]",
            ".dll": " [library]",
            ".so": " [library]",
        }

    def visit_file(self, file, prefix, is_last):
        """Processes a file and adds it to the structure."""
        connector = "└── " if is_last else "├── "
        desc = FileUtils.get_file_type_desc(file.path, self.type_map)
        self.structure.append(f"{prefix}{connector}{file.name}{desc}")

        # For binary files or files with descriptions, do not add content
        if desc or file.name.startswith(".") or ".min." in file.name:
            skip_text = f"Content skipped for {desc.strip()}"
            content = f"\n{'='*50}\nFile: {file.path}\n{'='*50}\n[{skip_text}]"
        else:
            f_path = FileUtils.read_file_content(file.path)
            content = f"\n{'='*50}\nFile: {file.path}\n{'='*50}\n{f_path}"

        self.content.append(content)

    def visit_directory(self, directory, prefix, is_last):
        """Processes a directory and adds it to the structure."""
        if directory.name in self.excluded_dirs:
            return

        connector = "└── " if is_last else "├── "
        self.structure.append(f"{prefix}{connector}{directory.name}/")

    def save_report(self):
        """Saves the generated report to the file."""
        try:
            with open(self.output_file, "w", encoding="utf-8") as f:
                f.write("PROJECT STRUCTURE:\n")
                f.write("\n".join(self.structure))
                f.write("\n\nFILE CONTENTS:")
                f.write("".join(self.content))

            logger.info(f"Report successfully saved to: {self.output_file}")
        except Exception as e:
            logger.error(f"ERROR saving report: {e}")
            print(f"ERROR saving report: {e}")
            raise
