"""ASS sections definitions.

Each section is capable of serializing and deserializing itself to an ASS text
representation of itself.
"""
from .ass_base_section import AssBaseSection
from .ass_base_tabular_section import AssBaseTabularSection
from .ass_event_list import AssEventList
from .ass_key_value_section import AssKeyValueSection
from .ass_script_info import AssScriptInfo
from .ass_string_table_section import AssStringTableSection
from .ass_style_list import AssStyleList

__all__ = [
    "AssBaseSection",
    "AssBaseTabularSection",
    "AssEventList",
    "AssKeyValueSection",
    "AssScriptInfo",
    "AssStringTableSection",
    "AssStyleList",
]
