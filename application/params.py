from dataclasses import dataclass
from constants import Models, FunctionType


@dataclass()
class NetworkParameters:
    dimension_N: int
    dimension_M: int
    model: Models
    p_high_state_init: int


@dataclass()
class VinParameters:
    v_type: FunctionType
    amplitude: float
    freq: int


@dataclass()
class SpiceParameters:
    samples: int
    tstop: int
    tstep: float
    tstart: float


@dataclass()
class PershinParameters:
    Roff: float
    ratio: int
    vt: float
    beta: float
    alpha: float
