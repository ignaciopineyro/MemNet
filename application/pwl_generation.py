import numpy as np

from constants import FILEPATH
from config import spice_parameters, vin_parameters


class PWLService:
    def generate_pwl(self) -> None:
        f = open(f"{FILEPATH}/vsource.txt", "w")
        time = np.linspace(spice_parameters.tstart, spice_parameters.tstop, 1000)
        voltage = -abs(vin_parameters.amplitude * np.sin(2 * np.pi * vin_parameters.freq * time))
        file_lines = ""
        for t, v in zip(time, voltage):
            file_lines += f"{t} {v} "
        f.write(f"pwl ({file_lines})")
        f.close()
