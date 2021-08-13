"""Tests for the AssEventList class."""
from copy import copy, deepcopy

import pytest

from ass_parser.ass_event import AssEvent
from ass_parser.ass_event_list import AssEventList


def test_ass_event_list_append_sets_parent() -> None:
    """Test that event insertion sets the item parent."""
    event = AssEvent()
    events = AssEventList()
    events.append(event)
    assert event.parent == events


def test_ass_event_list_removal_unsets_parent() -> None:
    """Test that event removal unsets the item parent."""
    event = AssEvent()
    events = AssEventList()
    events.append(event)
    assert event.parent == events
    del events[events.index(event)]
    assert event.parent is None


def test_ass_event_list_double_parenthood() -> None:
    """Test that event insertion cannot reclaim parenthood from another list."""
    event = AssEvent()
    events1 = AssEventList()
    events2 = AssEventList()
    events1.append(event)
    with pytest.raises(TypeError):
        events2.append(event)


def test_copying_event() -> None:
    """Test that copied events are detached from their original parents."""
    event = AssEvent()
    events = AssEventList()
    events.append(event)
    assert copy(event).parent is None
    assert event.parent == events


def test_copying_event_list() -> None:
    """Test that events copied with their parents are still linked to their
    original parent.
    """
    event = AssEvent()
    events = AssEventList()
    events.append(event)
    events_copy = copy(events)
    assert events[0].parent == events
    assert events_copy[0].parent == events


def test_deep_copying_event_list() -> None:
    """Test that events deep-copied with their parents are linked to their
    copied parent.
    """
    event = AssEvent()
    events = AssEventList()
    events.append(event)
    events_copy = deepcopy(events)
    assert events[0].parent == events
    assert events_copy[0].parent == events_copy
