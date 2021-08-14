"""AssBaseTabularSection definition."""
from collections.abc import MutableSequence
from typing import Generic, TypeVar

from ass_parser.ass_sections.ass_base_section import AssBaseSection
from ass_parser.errors import CorruptAssError, CorruptAssLineError

TAssTableItem = TypeVar("TAssTableItem")


class AssBaseTabularSection(
    AssBaseSection, Generic[TAssTableItem], MutableSequence[TAssTableItem]
):
    """Base tabular ASS section.

    Items are generic so that there can be detailed specializations for events
    and items.
    """

    def consume_ass_body_lines(self, lines: list[tuple[int, str]]) -> None:
        """Populate self from .ass lines representing this section, excluding
        the header.

        :param lines: list of tuples (line_num, line)
        """
        if not lines:
            raise CorruptAssError("expected a table header")

        line_num, line = lines[0]
        try:
            item_type, rest = line.split(":", 1)
        except ValueError as exc:
            raise CorruptAssLineError(
                line_num, line, "expected a colon"
            ) from exc
        if item_type != "Format":
            raise CorruptAssLineError(
                line_num,
                line,
                'expected the table header to be named "Format"',
            )
        field_names = [p.strip() for p in rest.strip().split(",")]

        self.clear()

        for line_num, line in lines[1:]:
            try:
                item_type, rest = line.split(": ", 1)
            except (ValueError, IndexError) as exc:
                raise CorruptAssLineError(
                    line_num, line, "expected a colon"
                ) from exc
            field_values = rest.strip().split(",", len(field_names) - 1)
            if len(field_names) != len(field_values):
                raise CorruptAssLineError(
                    line_num, line, f"expected {len(field_names)} values"
                )
            item = dict(zip(field_names, field_values))
            try:
                self.consume_ass_table_row(item_type, item)
            except (ValueError, IndexError) as exc:
                raise CorruptAssLineError(line_num, line, str(exc)) from exc

    def consume_ass_table_row(
        self, item_type: str, item: dict[str, str]
    ) -> None:
        """Populate self from a dict created by parsing an input .ass line.

        :param item_type: the part before the colon
        :param item: the dictified .ass line
        """
        raise NotImplementedError("not implemented")  # pragma: no cover