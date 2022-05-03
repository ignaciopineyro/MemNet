from constants import Models, FunctionType
from params import NetworkParameters, VinParameters, SpiceParameters, PershinParameters


network_parameters = NetworkParameters(
    dimension_N=2,
    dimension_M=2,
    model=Models.PERSHIN,
    p_high_state_init=1,
)

vin_parameters = VinParameters(
    v_type=FunctionType.SINE,
    amplitude=10.0,
    freq=1,
)

spice_parameters = SpiceParameters(
    samples=1500,
    tstop=3,
    tstep=(1500/3),
    tstart=1e-9,
)

pershin_parameters = PershinParameters(
    Roff=2e5,
    ratio=100,
    vt=0.6,
    beta=5e5,
    alpha=0,
)
