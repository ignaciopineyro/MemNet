import os

from application.constants import REPO_PATH, FILEPATH

import pandas as pd

from application.services.externalsourceservice import ExternalSourceService


class SingleDeviceService:
    def __init__(self):
        self.external_source_service = ExternalSourceService()

    def run_single_dev_simulation(self, params, folder):
        self._write_netlist(params, folder)
        os.system(f"ngspice spice/test.cir")
        self._export_data(folder)

    def _write_netlist(self, params, folder):
        models_path = f"{REPO_PATH}/simulation_platform/memristor_models"
        sim_time = params['tran_params']['stop_time']
        sim_init = params['tran_params']['start_time']
        data_points = params['tran_params']['data_points']
        sim_step = float(sim_time) / int(data_points)

        f = open(f"exported_data/{folder}/netlists/single_dev.cir", "w+")
        f.write("Single memristor simulation\n")
        f.write(f".include {models_path}/{params['model']}.sub\n")

        voltage_source = self.external_source_service.define_voltage_source(
            params['signal_waveform'],
            params['signal_params'],
            sim_init,
            sim_time,
            data_points
        )
        f.write(f"V1 vin gnd {voltage_source}\n")

        memristor_params = ""
        for model_param in params['model_params'].keys():
            memristor_params += \
                f"{model_param}={params['model_params'][model_param]} "

        f.write(f"Xmem vin gnd l memristor {memristor_params}\n")

        f.write(f".tran {sim_step} {sim_time} {sim_init} uic\n")
        f.write(".control\n")
        f.write("run\n")
        f.write("set wr_vecnames\n")
        f.write("set wr_singlescale\n")
        f.write(f"wrdata {FILEPATH}/single_dev_sim.csv vin i(v1) l\n")
        f.write("quit\n")
        f.write(".endc\n")
        f.write(".end\n")
        f.close()

    def _export_data(self, folder):
        try:
            data = pd.read_csv(
                f'{FILEPATH}/single_dev_sim.csv',
                sep=r'\s+'
            )

        except:
            data = pd.read_csv(
                f'{FILEPATH}/single_dev_sim.csv.data',
                sep=r'\s+'
            )
            data.drop(data.columns[[2, 4]], axis=1, inplace=True)

        data.columns = ['time', 'voltage', 'current', 'state']
        data.to_csv(
            f'{FILEPATH}/single_dev_sim.csv',
            header=True,
            index=False,
            encoding='utf-16'
        )
        data.to_csv(
            f'exported_data/{folder}/single_dev_sim.csv',
            header=True,
            index=False,
            encoding='utf-16'
        )
