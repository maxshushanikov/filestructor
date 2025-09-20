import os


class ConsoleInputHandler:
    """Handles interactive console input for Structorex."""

    @staticmethod
    def get_directory():
        """
        Prompt the user for a directory path and validate it.

        Returns:
            str: Valid directory path.
        """
        while True:
            path = input("Enter directory path: ").strip()
            if os.path.isdir(path):
                return path
            print("Invalid directory. Try again.")

    @staticmethod
    def get_output_file():
        """
        Prompt the user for an output filename.

        Returns:
            str: Output filename (default: project_report.txt).
        """
        text = "Enter output filename (default: project_report.txt): "
        name = input(text).strip()
        return name or "project_report.txt"
