class VersionInfo:
    """
    Provides version-related information for the FastHelp package.
    """

    VERSION = "1.2.0-alpha"
    AUTHOR = "FastHelp Dev Team"
    LICENSE = "MIT"

    @classmethod
    def get_version(cls) -> str:
        """
        Returns the current version of FastHelp.
        """
        return cls.VERSION

    @classmethod
    def get_author(cls) -> str:
        """
        Returns the author of FastHelp.
        """
        return cls.AUTHOR

    @classmethod
    def get_license(cls) -> str:
        """
        Returns the license of FastHelp.
        """
        return cls.LICENSE

    @classmethod
    def full_info(cls) -> str:
        """
        Returns a full string with version, author, and license information.
        """
        return f"FastHelp v{cls.VERSION} by {cls.AUTHOR}. Licensed under {cls.LICENSE}."
