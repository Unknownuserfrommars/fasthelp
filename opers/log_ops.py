class LogicalOps:
    """
    Provides methods for logical operations such as AND, OR, XOR, and NOT.
    """

    @staticmethod
    def logical_and(a: bool, b: bool) -> bool:
        """
        Performs logical AND operation.

        Parameters:
        a (bool): First operand.
        b (bool): Second operand.

        Returns:
        bool: Result of a AND b.
        """
        return a and b

    @staticmethod
    def logical_or(a: bool, b: bool) -> bool:
        """
        Performs logical OR operation.

        Parameters:
        a (bool): First operand.
        b (bool): Second operand.

        Returns:
        bool: Result of a OR b.
        """
        return a or b

    @staticmethod
    def logical_not(a: bool) -> bool:
        """
        Performs logical NOT operation.

        Parameters:
        a (bool): Operand.

        Returns:
        bool: Result of NOT a.
        """
        return not a

    @staticmethod
    def logical_xor(a: bool, b: bool) -> bool:
        """
        Performs logical XOR operation.

        Parameters:
        a (bool): First operand.
        b (bool): Second operand.

        Returns:
        bool: Result of a XOR b.
        """
        return (a or b) and not (a and b)
