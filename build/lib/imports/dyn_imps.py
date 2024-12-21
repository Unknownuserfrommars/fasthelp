import importlib


class DynamicImporter:
    """
    Provides methods for dynamic import of Python modules.
    """

    @staticmethod
    def import_module(module_name: str):
        """
        Dynamically imports a module by name.

        Parameters:
        module_name (str): Name of the module to import.

        Returns:
        Module: The imported module.

        Raises:
        ImportError: If the module cannot be imported.
        """
        try:
            module = importlib.import_module(module_name)
            return module
        except ImportError as e:
            raise ImportError(f"Failed to import module '{module_name}': {e}")

    @staticmethod
    def reload_module(module):
        """
        Reloads a previously imported module.

        Parameters:
        module (Module): The module to reload.

        Returns:
        Module: The reloaded module.
        """
        try:
            return importlib.reload(module)
        except Exception as e:
            raise RuntimeError(f"Failed to reload module '{module.__name__}': {e}")
