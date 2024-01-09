#!/usr/bin/python3
"""class_to_json module"""


def class_to_json(obj):
    """Converts an object to a JSON-serializable dictionary."""
    if hasattr(obj, "__dict__"):
        return obj.__dict__
    elif hasattr(obj, "__iter__") and not isinstance(obj, str):
        return [class_to_json(item) for item in obj]
    else:
        return obj
