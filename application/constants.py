import os

from enum import Enum

BASE_FILENAMES = "simulation"
REPO_PATH = os.path.dirname(__file__)
FILEPATH = os.path.join(REPO_PATH, "tmp_data")


class Models(Enum):
    PERSHIN = 'pershin'


class FunctionType(Enum):
    SINE = 'sine'
    PWL = 'pwl'


class SpiceNodeName(Enum):
    VIN = 'vin'
    GND = 'gnd'


class TableColumns(Enum):
    TIME = 'Time'
    CURRENT = 'Current'
    VOLTAGE = 'Voltage'


class NodeColors(Enum):
    GREEN = 'green'
