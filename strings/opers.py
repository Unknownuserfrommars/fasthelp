import re
import string

class strings:
    """
    Provides methods for string manipulations such as case conversions,
    specific letter capitalization, and dedentation.
    """

    def __init__(self, text: str):
        """
        Initialize the StringHelper class with a string.

        Parameters:
        text (str): The original string.

        Example:
        ```python
        str_helper = StringHelper("HelloWorld")
        print(str_helper.upper())
        ```
        """
        self.text = text

    def __repr__(self):
        return f"StringHelper(text='{self.text[:20]}...')"

    def upper(self) -> str:
        """
        Converts the string to uppercase.
        """
        return self.text.upper()

    def lower(self) -> str:
        """
        Converts the string to lowercase.
        """
        return self.text.lower()

    def capitalize_letters(self, letters: list[str] | str = "") -> str:
        """
        Capitalizes specific letters in the string.

        Parameters:
        letters (list[str] or str): The letters to capitalize.

        Returns:
        str: The modified string.
        """
        letters_set = set(letters)
        return ''.join([char.upper() if char in letters_set else char for char in self.text])

    def lower_letters(self, letters: list[str] | str) -> str:
        """
        Converts specific letters to lowercase.

        Parameters:
        letters (list[str] or str): The letters to lowercase.

        Returns:
        str: The modified string.
        """
        letters_set = set(letters)
        return ''.join([char.lower() if char in letters_set else char for char in self.text])

    @staticmethod
    def lowercase_letters() -> str:
        """
        Returns all ASCII lowercase letters.
        """
        return string.ascii_lowercase

    @staticmethod
    def uppercase_letters() -> str:
        """
        Returns all ASCII uppercase letters.
        """
        return string.ascii_uppercase

    def dedent(self) -> str:
        """
        Removes leading whitespaces from all lines in the string.

        Returns:
        str: Dedented string.
        """
        lines = self.text.splitlines()
        indent = min(
            (len(re.match(r'^\s*', line).group()) for line in lines if line.strip()), 
            default=0
        )
        return '\n'.join(line[indent:] for line in lines)
