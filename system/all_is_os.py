import platform
import psutil
import shutil
import socket

class OS:
    """
    Provides methods to retrieve OS and system-related information.
    """

    @staticmethod
    def get_os_name() -> str:
        """
        Returns the name of the operating system.
        """
        return platform.system()

    @staticmethod
    def get_os_version() -> str:
        """
        Returns the version of the operating system.
        """
        return platform.version()

    @staticmethod
    def get_machine_info() -> str:
        """
        Returns the machine type (e.g., 'x86_64').
        """
        return platform.machine()

    @staticmethod
    def get_hostname() -> str:
        """
        Returns the hostname of the machine.
        """
        return socket.gethostname()

    @staticmethod
    def get_memory_info() -> dict:
        """
        Returns memory information.

        Returns:
        dict: A dictionary with total, available, and used memory.
        """
        mem = psutil.virtual_memory()
        return {
            "total": mem.total,
            "available": mem.available,
            "used": mem.used
        }

    @staticmethod
    def get_disk_space(path: str = "/") -> dict:
        """
        Returns disk space information for the given path.

        Parameters:
        path (str): The directory to check.

        Returns:
        dict: A dictionary with total, used, and free space.
        """
        disk = shutil.disk_usage(path)
        return {
            "total": disk.total,
            "used": disk.used,
            "free": disk.free
        }
