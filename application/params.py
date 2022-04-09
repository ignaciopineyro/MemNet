from dataclasses import dataclass
from constants import Models, FunctionType


@dataclass()
class NetworkParameters:
    """N by M network using a given sub-circuit model."""
    dimension_N: int
    dimension_M: int
    model: Models
    p_high_state_init: int


@dataclass()
class VinParameters:
    """Input voltage source with a given waveform, amplitude value and frequency."""
    v_type: FunctionType
    amplitude: float
    freq: int


@dataclass()
class SpiceParameters:
    """Amount of samples to simulate, start and end time for the simulation and the step between samples."""
    samples: int
    tstop: int
    tstep: float
    tstart: float


@dataclass()
class PershinParameters:
    """WIP"""
    Roff: float
    ratio: int
    vt: float
    beta: float
    alpha: float
