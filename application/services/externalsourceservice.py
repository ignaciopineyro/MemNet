import numpy as np

from application.constants import FILEPATH
from application.config import spice_parameters, vin_parameters


class ExternalSourceService:
    def generate_pwl(self) -> None:
        f = open(f"{FILEPATH}/vsource.txt", "w")
        time = np.linspace(spice_parameters.tstart, spice_parameters.tstop, 1000)
        voltage = -abs(vin_parameters.amplitude * np.sin(2 * np.pi * vin_parameters.freq * time))
        file_lines = ""
        for t, v in zip(time, voltage):
            file_lines += f"{t} {v} "
        f.write(f"pwl ({file_lines})")
        f.close()

    def define_voltage_source(waveform, signal_params, tinit, tstop, datapoints):
        amp = float(signal_params["amplitud"])
        freq = float(signal_params["frecuencia"])

        if waveform == 'sin':
            return f'sin (0 {amp} {freq})'

        else:
            pwl_generation(tinit, tstop, datapoints, waveform, amp, freq)
            f = open(f"{TEMP_FILES_PATH}/pwl_source.txt", "r")
            pwl = f.read()
            f.close()
            return f'{pwl}'
