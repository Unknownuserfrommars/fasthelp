import subprocess
import sys


class PipHelper:
    """
    Provides methods for managing Python packages using pip.
    """

    @staticmethod
    def install_package(package_name: str):
        """
        Installs a Python package using pip.

        Parameters:
        package_name (str): Name of the package to install.
        """
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", package_name], check=True)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Failed to install package '{package_name}': {e}")

    @staticmethod
    def upgrade_package(package_name: str):
        """
        Upgrades a Python package using pip.

        Parameters:
        package_name (str): Name of the package to upgrade.
        """
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", package_name], check=True)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Failed to upgrade package '{package_name}': {e}")

    @staticmethod
    def uninstall_package(package_name: str):
        """
        Uninstalls a Python package using pip.

        Parameters:
        package_name (str): Name of the package to uninstall.
        """
        try:
            subprocess.run([sys.executable, "-m", "pip", "uninstall", "-y", package_name], check=True)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Failed to uninstall package '{package_name}': {e}")
