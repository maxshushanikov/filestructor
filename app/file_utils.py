import logging
import os

logger = logging.getLogger(__name__)


class FileUtils:
    """Utilities for file operations."""

    MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

    @staticmethod
    def get_file_type_desc(file_path, type_map):
        """Determines the file type by extension."""
        _, ext = os.path.splitext(file_path)
        return type_map.get(ext.lower(), "")

    @staticmethod
    def read_file_content(file_path):
        """Reads the contents of a file with error handling."""
        try:
            # Checks file size
            file_size = os.path.getsize(file_path)
            if file_size > FileUtils.MAX_FILE_SIZE:
                f_size = file_size / (1024 * 1024)
                return f"[SKIPPED: File too large ({f_size:.1f} MB > 10 MB)]"

            # Reads small files.
            with open(file_path, "r", encoding="utf-8", errors="replace") as f:
                return f.read()
        except UnicodeDecodeError:
            return "[Binary file - content not displayed]"
        except PermissionError:
            return "[ACCESS ERROR: Cannot read file]"
        except Exception as e:
            return f"[ERROR: {str(e)}]"
