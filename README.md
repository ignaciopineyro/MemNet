[comment]: <> (# MemNet_2 - A forked repository from MemNet_1 &#40;fabriziodifran/MemNet&#41;)
This is a forked repository from fabriziodifran/MemNet. The main goal of this project is to deal with the 
high computation times and scalability constraint present on previous stages of the research.

This repository contains code to simulate square-shaped memristive arrays of an arbitrary size. 
The size (N) is determined by the number of nodes of each side in a matrix geometrical array. 
Every two consecutive nodes, one memristive unit is placed either along horizontal or vertical directions.  
The model determining each memristive unit's behaviour has been adapted from previously developed models: 

> Y. V. Pershin and M. Di Ventra, 'SPICE model of memristive devices with threshold', Radioengineering 22, 485 (2013).
> 
> I. Vourkas and G. Sirakoulis, 'Memristor-Based Nanoelectronic Computing Circuits and Architectures' (Springer, 2015).


## Requirements
- Python3
- Numpy
- Pandas
- Networkx
- Matplotlib
- NGSpice (with executable path on PATH enviroment variable)

## Getting started
* Download the full repository
* Install NGSpice and add its exec file to the PATH variable:
    - Windows: http://ngspice.sourceforge.net/download.html
    - Linux: ```sudo apt-get install ngspice```
* Install the required libraries - ```pip install -r requirements.txt```
* Set the parameters by editing params.py and run main.py.
* Run code on /application folder: ```python3 main.py```

## Simulated results
Once the script ```main.py``` is executed, a folder named exported_data should be created and two outputs files will be displayed: 
> simulation_iv 
> > containing three columns: time, current, and voltage (the latter two measured at the source)
> > 
> simulation_states
> > containing N x N + 1 columns: time, X(0 0), X(0 1), ..., X(N-1 N-1) 
> > 
> > being X(i j) the internal state of the unit whose cathode is connected to node (i j)   

For further questions email us at cquinteros@unsam.edu.ar.

## License
This code is for non-commercial use under a CC BY license (Creative Commons Attribution 4.0 International License).
