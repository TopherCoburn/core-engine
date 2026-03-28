import os
import shutil
import logging
import re
from typing import Union, List, Dict

class FilesystemUtils:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def copy_file(self, source: str, destination: str) -> str:
        try:
            shutil.copy2(source, destination)
            self.logger.info(f"Copied file from {source} to {destination}")
            return destination
        except Exception as e:
            self.logger.error(f"Failed to copy file from {source} to {destination}: {e}")
            raise

    def move_file(self, source: str, destination: str) -> str:
        try:
            shutil.move(source, destination)
            self.logger.info(f"Moved file from {source} to {destination}")
            return destination
        except Exception as e:
            self.logger.error(f"Failed to move file from {source} to {destination}: {e}")
            raise

    def delete_file(self, file_path: str) -> None:
        try:
            os.remove(file_path)
            self.logger.info(f"Deleted file at {file_path}")
        except Exception as e:
            self.logger.error(f"Failed to delete file at {file_path}: {e}")
            raise

    def delete_directory(self, directory_path: str) -> None:
        try:
            shutil.rmtree(directory_path)
            self.logger.info(f"Deleted directory at {directory_path}")
        except Exception as e:
            self.logger.error(f"Failed to delete directory at {directory_path}: {e}")
            raise

    def get_file_size(self, file_path: str) -> int:
        try:
            return os.path.getsize(file_path)
        except Exception as e:
            self.logger.error(f"Failed to get file size of {file_path}: {e}")
            raise

    def get_file_extension(self, file_path: str) -> str:
        try:
            return os.path.splitext(file_path)[1]
        except Exception as e:
            self.logger.error(f"Failed to get file extension of {file_path}: {e}")
            raise

    def get_all_files_in_directory(self, directory_path: str) -> List[str]:
        try:
            return [os.path.join(directory_path, f) for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
        except Exception as e:
            self.logger.error(f"Failed to get all files in directory {directory_path}: {e}")
            raise

    def get_all_directories_in_directory(self, directory_path: str) -> List[str]:
        try:
            return [os.path.join(directory_path, d) for d in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, d))]
        except Exception as e:
            self.logger.error(f"Failed to get all directories in directory {directory_path}: {e}")
            raise

    def get_file_content(self, file_path: str) -> str:
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except Exception as e:
            self.logger.error(f"Failed to get file content of {file_path}: {e}")
            raise

    def write_to_file(self, file_path: str, content: str) -> None:
        try:
            with open(file_path, 'w') as file:
                file.write(content)
            self.logger.info(f"Wrote to file at {file_path}")
        except Exception as e:
            self.logger.error(f"Failed to write to file at {file_path}: {e}")
            raise

    def replace_text_in_file(self, file_path: str, old_text: str, new_text: str) -> None:
        try:
            with open(file_path, 'r+') as file:
                content = file.read()
                content = content.replace(old_text, new_text)
                file.seek(0)
                file.write(content)
                file.truncate()
            self.logger.info(f"Replaced text in file at {file_path}")
        except Exception as e:
            self.logger.error(f"Failed to replace text in file at {file_path}: {e}")
            raise

    def search_pattern_in_file(self, file_path: str, pattern: str) -> bool:
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                return re.search(pattern, content) is not None
        except Exception as e:
            self.logger.error(f"Failed to search pattern in file at {file_path}: {e}")
            raise

    def get_directory_size(self, directory_path: str) -> int:
        try:
            total_size = 0
            for dirpath, dirnames, filenames in os.walk(directory_path):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    total_size += os.path.getsize(fp)
            return total_size
        except Exception as e:
            self.logger.error(f"Failed to get directory size of {directory_path}: {e}")
            raise

class PathUtils:
    @staticmethod
    def join_paths(*paths: Union[str, os.PathLike]) -> str:
        return os.path.join(*paths)

    @staticmethod
    def is_absolute(path: Union[str, os.PathLike]) -> bool:
        return os.path.isabs(path)

    @staticmethod
    def is_relative(path: Union[str, os.PathLike]) -> bool:
        return os.path.isrelpath(path)

    @staticmethod
    def exists(path: Union[str, os.PathLike]) -> bool:
        return os.path.exists(path)

    @staticmethod
    def get_directory(path: Union[str, os.PathLike]) -> str:
        return os.path.dirname(path)

    @staticmethod
    def get_filename(path: Union[str, os.PathLike]) -> str:
        return os.path.basename(path)

    @staticmethod
    def get_extension(path: Union[str, os.PathLike]) -> str:
        return os.path.splitext(path)[1]

    @staticmethod
    def get_size(path: Union[str, os.PathLike]) -> int:
        return os.path.getsize(path)

def normalize_path(path: Union[str, os.PathLike]) -> str:
    return os.path.normpath(path)