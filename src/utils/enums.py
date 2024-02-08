from enum import Enum


def nameof(class_: Enum):
    return str(class_).split("'")[1]
