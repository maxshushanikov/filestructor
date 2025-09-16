import logging
import os

logger = logging.getLogger(__name__)


class FileUtils:
    """Утилиты для операций с файлами."""

    MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

    @staticmethod
    def get_file_type_description(file_path, type_map):
        """Определяет тип файла по расширению."""
        _, ext = os.path.splitext(file_path)
        return type_map.get(ext.lower(), "")

    @staticmethod
    def read_file_content(file_path):
        """Читает содержимое файла с обработкой ошибок."""
        try:
            # Проверяем размер файла
            file_size = os.path.getsize(file_path)
            if file_size > FileUtils.MAX_FILE_SIZE:
                return f"[SKIPPED: File too large ({file_size/(1024*1024):.1f} MB > 10 MB)]"

            # Читаем небольшие файлы
            with open(file_path, "r", encoding="utf-8", errors="replace") as f:
                return f.read()
        except UnicodeDecodeError:
            return "[Binary file - content not displayed]"
        except PermissionError:
            return "[ACCESS ERROR: Cannot read file]"
        except Exception as e:
            return f"[ERROR: {str(e)}]"
