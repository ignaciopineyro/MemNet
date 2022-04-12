import os
import numpy as np

from constants import FILEPATH, SpiceNodeName
from config import network_parameters, vin_parameters, spice_parameters, pershin_parameters


class SpiceNetlistService:

    def __init__(self):
        self.connections = []
        self.state_nodes = []
    
    def generate_netlist(self, network, netlist_name, sensibilize_params=None) -> None:
        for edge in network.edges:
            node1 = edge[0]
            node2 = edge[1]
            gnd_node = self._get_gnd_node(network, network_parameters.dimension_N)
            voltage_input_node = list(network.nodes)[0] 
            
            n1 = f"n{node1[0]}{node1[1]}"
            n2 = f"n{node2[0]}{node2[1]}"

            if node1 == voltage_input_node:
                n1 = SpiceNodeName.VIN
                
            if node1 == gnd_node:
                n1 = SpiceNodeName.GND
                
            if node2 == gnd_node:
                n2 = SpiceNodeName.GND
            
            self.state_nodes.append(f"L({node1[0]};{node1[1]})({node2[0]};{node2[1]})")
            self.connections.append((n1, n2))
        
        self._write_netlist_file(self.connections, netlist_name, sensibilize_params)

    def run_ngspice(self, netlist_name) -> None:
        os.system(f"ngspice {FILEPATH}/{netlist_name}.cir")

    def _get_gnd_node(self, graph, n):
        last_row_nodes = []
        for node in graph.nodes:
            if str(n-1) in str(node[0]):
                last_row_nodes.append(node)
        return last_row_nodes[0]

    # TODO: sensibilize_params no se utiliza
    def _write_netlist_file(self, connections, netlist_name, sensibilize_params) -> None:
        states = ""
        f = open(f"{FILEPATH}/{netlist_name}.cir", "w+")   
        f.write("Memristor Random network \n")
        f.write(f".include ../models/{network_parameters.model.value}.sub\n")
        vin = self._get_vin_type()
        f.write(f"V1 vin gnd {vin}\n")

        # TODO: Esto deberia variar segun que modelo se elija
        for idx, c in enumerate(connections):
            alpha = pershin_parameters.alpha
            beta = pershin_parameters.beta
            vt = pershin_parameters.vt
            roff = pershin_parameters.Roff
            ratio = pershin_parameters.ratio
            p_high_state_init = network_parameters.p_high_state_init
            rinit = np.random.choice((roff/ratio, roff), p=[1-p_high_state_init, p_high_state_init])
            
            model_params = f"alpha={alpha} beta={beta} Roff={roff} Ron={roff/ratio} Rinit={rinit} Vt={vt}"
            
            f.write(f"Xmem{idx} {c[0]} {c[1]} l{idx} memristor {model_params}\n")
            states += f"l{idx} "

        f.write(f".tran {spice_parameters.tstep} {spice_parameters.tstop} {spice_parameters.tstart} uic\n")
        f.write(".control\n")
        f.write("run\n")
        # f.write("option numdgt=7\n")
        f.write("set wr_vecnames\n")
        f.write("set wr_singlescale\n")
        f.write(f"wrdata {FILEPATH}/{netlist_name}_states.csv " + states + " \n")
        f.write(f"wrdata {FILEPATH}/{netlist_name}_iv.csv i(v1) vin\n")
        # f.write("plot -i(v1) vs vin\n")
        f.write("quit\n")
        f.write(".endc\n")
        f.write(".end\n")
        f.close()

    # TODO: Implementar Strategy Pattern
    def _get_vin_type(self):
        if vin_parameters.v_type.value == "sine":
            return f"sin (0 {vin_parameters.amplitude} {vin_parameters.freq}"
        elif vin_parameters.v_type.value == "pwl":
            f = open(f"{FILEPATH}/vsource.txt", "r")
            pwl = f.read()
            return f"{pwl}"
