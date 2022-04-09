from constants import Models, FunctionType
from params import NetworkParameters, VinParameters, SpiceParameters, PershinParameters


NetworkParameters(
    dimension_N=4,
    dimension_M=4,
    model=Models.PERSHIN,
    p_high_state_init=1,
)

VinParameters(
    v_type=FunctionType.SINE,
    amplitude=10.0,
    freq=1,
)

SpiceParameters(
    samples=1500,
    tstop=3,
    tstep=SpiceParameters.tstop/SpiceParameters.samples,
    tstart=1e-9,
)

PershinParameters(
    Roff=2e5,
    ratio=100,
    vt=0.6,
    beta=5e5,
    alpha=0,
)
