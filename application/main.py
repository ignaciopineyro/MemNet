from constants import BASE_FILENAMES
from pwl_generation import PWLService
from netlist_generation import SpiceNetlistService
from network_generation import NetworkService
from export_data import ExportDataService


def main() -> None:
    """Main function to execute the simulations script"""
    export_data_service = ExportDataService()
    pwl_service = PWLService()
    netlist_service = SpiceNetlistService()
    network_service = NetworkService()

    export_data_service.create_data_folders()
    pwl_service.generate_pwl()
    network = network_service.generate_network()
    netlist_service.generate_netlist(network, f"{BASE_FILENAMES}_0")
    netlist_service.run_ngspice(f"{BASE_FILENAMES}_0")
    state_list = []
    state_list.append(netlist_service.state_nodes)
    export_data_service.data_export(state_list, 1)


if __name__ == '__main__':
    main()
