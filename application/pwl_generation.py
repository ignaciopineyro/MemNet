import numpy as np

from constants import FILEPATH
from params import SpiceParameters, VinParameters


class PWLService:
    def generate_pwl(self) -> None:
        f = open(f"{FILEPATH}/vsource.txt", "w")
        time = np.linspace(SpiceParameters.tstart, SpiceParameters.tstop, 1000)
        voltage = -abs(VinParameters.amplitude * np.sin(2 * np.pi * VinParameters.freq * time))
        file_lines = ""
        for t, v in zip(time, voltage):
            file_lines += f"{t} {v} "
        f.write(f"pwl ({file_lines})")
        f.close()
