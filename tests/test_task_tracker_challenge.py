import pytest
from lib.task_tracker_challenge import *

""" test checks if task is added """

def test_Task_tracker():
    task_tracker = Task_tracker()
    task_tracker.add("Shopping")
    result = task_tracker.read()

    assert result == "shopping"

""" test checks if todo string returns desired value"""

def test_Task_tracker_checks_for_todo():
    task_tracker = Task_tracker()
    result = task_tracker.add("#TODO")

    assert result == "#TODO has been added"


""" test checks that the same task inst added twice"""
def test_Task_tracker_adds_once():
    task_tracker = Task_tracker()
    task_tracker.add("Pick up my kids")
    task_tracker.add("go to school")
    task_tracker.add("pick up my kids")
    result = task_tracker.read()

    assert result == "pick up my kids, go to school"

""" test checks if string is empty """

def test_Task_tracker_for_empty_string():
    task_tracker = Task_tracker()
    
    with pytest.raises(Exception) as e:
        task_tracker.add("")
    
    assert str(e.value) == "can't add an empty string"


def test_todo_added_and_todo_in_list():
    task_tracker = Task_tracker()
    task_tracker.add("#TODO")
    result = task_tracker.read()

    assert result == "#TODO"


