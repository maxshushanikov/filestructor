import os

class FileUtils:
    """Utility methods for file operations."""

    @staticmethod
    def get_file_type_description(file_path, type_map):
        """
        Determine the file type based on its extension.

        Args:
            file_path (str): Path to the file.
            type_map (dict): Mapping of file extensions to type descriptions.

        Returns:
            str: File type description or an empty string if unknown.
        """
        _, ext = os.path.splitext(file_path)
        return type_map.get(ext.lower(), "")

    @staticmethod
    def read_file_content(file_path):
        """
        Read the content of a file with error handling.

        Args:
            file_path (str): Path to the file.

        Returns:
            str: File content or an error message if reading fails.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except UnicodeDecodeError:
            return "[Binary file - content not displayed]"
        except PermissionError:
            return "[ACCESS ERROR: Cannot read file]"
        except Exception as e:
            return f"[ERROR: {str(e)}]"
