"""AssColor definition."""
from typing import NamedTuple


class AssColor(NamedTuple):
    """ASS color."""

    red: int
    green: int
    blue: int
    alpha: int

    @staticmethod
    def from_ass_string(text: str) -> "AssColor":
        """Deserialize .ass text reperesentation to an AssColor.

        :param text: text to parse
        :return: parsed AssColor
        """
        if text.endswith("&"):
            text = text[:-1]
        if not text.startswith("&H"):
            raise ValueError('ASS colors should start with "&H"')
        val = int(text[2:], base=16)
        red = val & 0xFF
        green = (val >> 8) & 0xFF
        blue = (val >> 16) & 0xFF
        alpha = (val >> 24) & 0xFF
        return AssColor(red, green, blue, alpha)
