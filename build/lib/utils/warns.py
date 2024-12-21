import warnings

class DeprecationHelper:
    """
    Provides utility methods to issue deprecation warnings.
    """

    @staticmethod
    def _warn(message: str, stacklevel: int = 2):
        """
        Issues a custom warning.

        Parameters:
        message (str): The warning message to display.
        stacklevel (int): The stack level at which the warning originates.
        """
        warnings.warn(message, stacklevel=stacklevel, category=DeprecationWarning)

    @staticmethod
    def deprecation_warning(feature: str, version: str):
        """
        Issues a deprecation warning for a specific feature.

        Parameters:
        feature (str): The feature being deprecated.
        version (str): The version in which the feature will be removed.
        """
        message = f"The feature '{feature}' is deprecated and will be removed in version {version}."
        DeprecationHelper._warn(message)
