"""AssScriptInfo definition."""
from ass_parser.ass_sections.ass_key_value_section import AssKeyValueSection
from ass_parser.ass_sections.const import SCRIPT_INFO_SECTION_NAME


class AssScriptInfo(AssKeyValueSection):
    """ASS script info."""

    def __init__(self) -> None:
        """Initialize self."""
        super().__init__(SCRIPT_INFO_SECTION_NAME)
