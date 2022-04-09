import os

from enum import Enum


class Path(Enum):
    BASE_FILENAMES = "simulation"
    repo_path = os.path.dirname(__file__)
    filepath = os.path.join(repo_path, "tmp_data")

    @staticmethod
    def set_path():
        repo_path = os.path.dirname(__file__)
        filepath = os.path.join(repo_path, "tmp_data")
        return repo_path, filepath


class Models(Enum):
    PERSHIN = 'pershin'


class FunctionType(Enum):
    SINE = 'sine'


class NodeColors(Enum):
    GREEN = 'green'
