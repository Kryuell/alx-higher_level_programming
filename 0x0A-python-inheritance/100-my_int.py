#!/usr/bin/python3
"""Class MyInt inherits from int with inverted == and != operators."""


class MyInt(int):
    """Overrides equality (==) operator."""
    def __eq__(self, other):
        return super().__ne__(other)

    """Overrides inequality (!=) operator."""
    def __ne__(self, other):
        """Overrides inequality (!=) operator."""
        return super().__eq__(other)
