import os
import pandas as pd

from datetime import datetime
from constants import BASE_FILENAMES, REPO_PATH, FILEPATH, TableColumns


class ExportDataService:
    def __init__(self):
        self.base_filenames = BASE_FILENAMES
        self.repo_path = REPO_PATH
        self.filepath = FILEPATH

    def create_data_folders(self) -> None:
        if 'tmp_data' not in os.listdir():
            os.mkdir('tmp_data')
        if 'exported_data' not in os.listdir():
            os.mkdir('exported_data')

    def _create_sim_folder(self) -> str:
        actual_time = datetime.now().strftime("%d-%m-%Y_%H%M%S")
        dir_path = f"{self.repo_path}/exported_data/{actual_time}"
        os.mkdir(dir_path)
        return dir_path

    def data_export(self, states, amount_simulations) -> None:
        simulation_dir = self._create_sim_folder()
        for i in range(amount_simulations):
            data_iv = pd.read_csv(f"{self.filepath}/{self.base_filenames}_{i}_iv.csv", sep="\s+")
            data_iv.columns = [TableColumns.TIME, TableColumns.CURRENT, TableColumns.VOLTAGE]
            data_states = pd.read_csv(f"{self.filepath}/{self.base_filenames}_{i}_states.csv", sep="\s+")
            data_states.columns = ["time"] + states[i]

            data_iv.to_csv(f"{simulation_dir}/{self.base_filenames}_{i}_iv.csv", sep=",", header=True, index=False)
            data_states.to_csv(
                f"{simulation_dir}/{self.base_filenames}_{i}_states.csv", sep=",", header=True, index=False
            )
