import numpy as np
import pandas as pd
import glob
import os

from matplotlib import pyplot as plt
from scipy.signal import argrelextrema

BASE_FILENAMES = "simulation"
REPO_PATH = os.path.dirname(__file__)
SIMULATIONS_PATH = os.path.join(REPO_PATH, "exported_data")
print(f'\n\nREPO_PATH={REPO_PATH}\n\n')

#path = os.path.join(SIMULATIONS_PATH, 'memristor_simulation.csv')
path = os.path.join('../NGSpice', 'memristor_simulation')
# all_files = glob.glob(path + "/*.csv")
print(f'\n\npath={path}\n\n')
all_files = glob.glob(os.path.join(path, "*.csv"))

                        ## Option 1 - the output seems to be a list
# li = []

# for filename in all_files:
  #  df = pd.read_csv(filename, index_col=None, header=0)
   # li.append(df)

# frame = pd.concat(li, axis=0, ignore_index=True)

                        ## Option 2 - the output is a core frame
print(f'\n\nall_files={all_files}\n\n')
df = pd.DataFrame(np.concatenate([pd.read_csv(f, sep=r"\s+")[1:len(pd.read_csv(f, sep=r"\s+"))+1] for f in all_files]), columns=pd.read_csv(all_files[0], sep=r"\s+").columns)


# sim = np.matrix(concatenated_df)
sim = np.matrix(df)


plt.figure(dpi=120)
plt.rcParams['font.size'] = 7

plt.subplot(2, 4, 1) 
plt.xlabel("Voltage (V)", fontsize=8) 
plt.ylabel("Current ($\mu$A)", fontsize=8) 
plt.plot(sim[1:int(len(sim)/4),1],-1*sim[1:int(len(sim)/4),2]/1e-6,"k") 

plt.subplot(2, 4, 2) 
plt.xlabel("Voltage (V)", fontsize=8) 
plt.ylabel("Current ($\mu$A)", fontsize=8) 
plt.plot(sim[int(len(sim)/4):int(len(sim)/2),1],-1*sim[int(len(sim)/4):int(len(sim)/2),2]/1e-6,"g")

plt.subplot(2, 4, 3) 
plt.xlabel("Voltage (V)", fontsize=8) 
plt.ylabel("Current ($\mu$A)", fontsize=8) 
plt.plot(sim[int(len(sim)/2):int(3*len(sim)/4),1],-1*sim[int(len(sim)/2):int(3*len(sim)/4),2]/1e-6,"m")

plt.subplot(2, 4, 4) 
plt.xlabel("Voltage (V)", fontsize=8) 
plt.ylabel("Current (mA)", fontsize=8) 
plt.plot(sim[int(3*len(sim)/4):len(sim),1],-1*sim[int(3*len(sim)/4):len(sim),2]/1e-3,"c")

plt.subplot(2, 4, 5)
plt.xlabel("Voltage (V)", fontsize=8) 
plt.ylabel("Current (A)", fontsize=8) 
plt.ylim(1e-7, 5e-3)
plt.semilogy(sim[1:int(len(sim)/4),1],np.abs(sim[1:int(len(sim)/4),2]), "k")

plt.subplot(2, 4, 6)
plt.xlabel("Voltage (V)", fontsize=8) 
plt.ylabel("Current (A)", fontsize=8) 
plt.ylim(1e-7, 5e-3)
plt.semilogy(sim[int(len(sim)/4):int(len(sim)/2),1],np.abs(sim[int(len(sim)/4):int(len(sim)/2),2]), "g")

plt.subplot(2, 4, 7)
plt.xlabel("Voltage (V)", fontsize=8) 
plt.ylabel("Current (A)", fontsize=8) 
plt.ylim(1e-7, 5e-3)
plt.semilogy(sim[int(len(sim)/2):int(3*len(sim)/4),1],np.abs(sim[int(len(sim)/2):int(3*len(sim)/4),2]), "m")

plt.subplot(2, 4, 8) 
plt.xlabel("Voltage (V)", fontsize=8) 
plt.ylabel("Current (A)", fontsize=8) 
plt.ylim(1e-7, 5e-3)
plt.semilogy(sim[int(3*len(sim)/4):len(sim),1],np.abs(sim[int(3*len(sim)/4):len(sim),2]), "c")

plt.tight_layout(pad=1.0)

plt.show()
# plt.figure(figsize=figsize, constrained_layout=True)

plt.figure(dpi=90)
plt.rcParams['font.size'] = 12

plt.xlabel("time (s)", fontsize=12) 
plt.ylabel("Voltage (V)", fontsize=12) 

plt.plot(sim[1:int(len(sim)/4),0],sim[1:int(len(sim)/4),1],"k") 
plt.plot(sim[int(len(sim)/4):int(len(sim)/2),0],sim[int(len(sim)/4):int(len(sim)/2),1],"g")
plt.plot(sim[int(len(sim)/2):int(3*len(sim)/4),0],sim[int(len(sim)/2):int(3*len(sim)/4),1],"m")
plt.plot(sim[int(3*len(sim)/4):len(sim),0],sim[int(3*len(sim)/4):len(sim),1],"c")

plt.plot(sim[1:int(len(sim)/4),0],0.6*np.ones(int(len(sim)/4)-1),"--r")
plt.plot(sim[1:int(len(sim)/4),0],-0.6*np.ones(int(len(sim)/4)-1),"--r")

plt.show()


plt.figure(dpi=120)
plt.rcParams['font.size'] = 7

plt.subplot(1, 3, 1) 
plt.xlabel("Voltage (V)", fontsize=8) 
plt.ylabel("Current (A)", fontsize=8) 

plt.plot(sim[1:int(len(sim)/4),1],-1*sim[1:int(len(sim)/4),2],"k") 
plt.plot(sim[int(len(sim)/4):int(len(sim)/2),1],-1*sim[int(len(sim)/4):int(len(sim)/2),2],"g")
plt.plot(sim[int(len(sim)/2):int(3*len(sim)/4),1],-1*sim[int(len(sim)/2):int(3*len(sim)/4),2],"m")
plt.plot(sim[int(3*len(sim)/4):len(sim),1],-1*sim[int(3*len(sim)/4):len(sim),2],"c")

plt.subplot(1, 3, 2)
plt.xlabel("Voltage (V)", fontsize=8) 
plt.ylabel("Current (A)", fontsize=8) 
plt.ylim(1e-7, 5e-3)

plt.semilogy(sim[1:int(len(sim)/4),1],np.abs(sim[1:int(len(sim)/4),2]), "k")
plt.semilogy(sim[int(len(sim)/4):int(len(sim)/2),1],np.abs(sim[int(len(sim)/4):int(len(sim)/2),2]), "g")
plt.semilogy(sim[int(len(sim)/2):int(3*len(sim)/4),1],np.abs(sim[int(len(sim)/2):int(3*len(sim)/4),2]), "m")
plt.semilogy(sim[int(3*len(sim)/4):len(sim),1],np.abs(sim[int(3*len(sim)/4):len(sim),2]), "c")

plt.legend(['ExtAmp = 0.7 V', 'ExtAmp = 1 V', 'ExtAmp = 2 V', 'ExtAmp = 4 V'])

plt.subplot(1, 3, 3)
plt.xlabel("Voltage (V)", fontsize=8) 
plt.ylabel("State ($\Omega$)", fontsize=8) 
# plt.ylim(1e3, 3e5)

plt.plot(sim[1:int(len(sim)/4-1),1],np.abs(sim[1:int(len(sim)/4-1),3]), "k")
plt.plot(sim[int(len(sim)/4):int(len(sim)/2-3),1],np.abs(sim[int(len(sim)/4):int(len(sim)/2-3),3]), "g")
plt.plot(sim[int(len(sim)/2):int(3*len(sim)/4-5),1],np.abs(sim[int(len(sim)/2):int(3*len(sim)/4-5),3]), "m")
plt.plot(sim[int(3*len(sim)/4):len(sim)-1,1],np.abs(sim[int(3*len(sim)/4):len(sim)-1,3]), "c")

plt.tight_layout(pad=1.0)

plt.show()

plt.plot(sim[1:int(len(sim)/4-1),0],np.abs(sim[1:int(len(sim)/4-1),3]), "k")
plt.plot(sim[int(len(sim)/4):int(len(sim)/2-3),0],np.abs(sim[int(len(sim)/4):int(len(sim)/2-3),3]), "g")
plt.plot(sim[int(len(sim)/2):int((3*(len(sim)/4))-5),0],np.abs(sim[int(len(sim)/2):int((3*(len(sim)/4))-5),3]), "m")
plt.plot(sim[int(3*len(sim)/4):len(sim),0],np.abs(sim[int(3*len(sim)/4):len(sim),3]), "c")


R = np.zeros((len(sim)-2,1))

for i in range(1,len(sim)-1):
    R[i-1] = -1*(sim[i,1] - sim[i-1,1]) / (sim[i,2] - sim[i-1,2])

LF = np.zeros((len(sim)-3,2))
RL = np.zeros((len(sim)-4,1))

# To-solve: export the uncertainty by activating some additional options 
# it will also imply to rescale LF

for j in range(10,len(sim)-10):
    LF[j,:] = np.polyfit(np.array(sim[j-10:j+10,2]).ravel(), np.array(-1*sim[j-10:j+10,1]).ravel(), 1)
    RL[j] = LF[j,0]

# Comparison between the results of the two methods:

# print(R[10])
# print(LF[10,0])
# print(LF[10,1])
# print(RL[0])

# Adding the two extreme conditions:

# beginning of first run
RL = np.insert(RL, 0, R[0], axis=None)

# end of last one
RL = np.append(RL, R[len(sim)-3], axis=None)

# The resistive value at the initial condition of each run is still the one calculated with the incremental ratio

delta = R[:,0] - RL
RL = np.where(delta > 2000, R[:,0], RL)


## New version

min = argrelextrema(np.abs(sim[:,1]), np.less)

Min = np.insert(min[0], 0, 0, axis=None)
Min = np.append(Min, len(sim[:,1])-3, axis=None)

plt.figure(dpi=150)

plt.subplot(3, 1, 1)
plt.title("Concatenated external signal") 
# plt.ylabel("Abs Voltage (V)")
plt.ylabel("Voltage (V)")
plt.xlabel("time (a.u.)")  
# plt.plot(np.arange(1, len(sim[:,2])+1), np.abs(sim[:,2]), "r")
plt.plot(np.arange(1, len(sim[:,1])+1), sim[:,1], "r")

# These are the resistive states calculated using the incremental ratio
plt.subplot(3, 1, 2)
# plt.subplot(2, 1, 1)
plt.title("Resistive states - incremental ratio method")
plt.ylabel("R @ 0 V ($\Omega$)")
plt.ylim(100, 800000)
plt.semilogy(Min, R[Min], "^r")

# These are the resistive states calculated as a linear fit 
# except for the beginning of each run and the end point of the last one 
plt.subplot(3, 1, 3)
# plt.subplot(2, 1, 2)
plt.title("Resistive states - linear fit method")
plt.ylabel("R @ 0 V ($\Omega$)") 
plt.xlabel("Number of cross point @ 0 V (a.u.)") 
plt.ylim(100, 800000)
plt.semilogy(Min, RL[Min], "pk")

plt.tight_layout(pad=2.0)

plt.savefig('ResistiveStates0V')


b = 0
c = 0
d = 0

State1 = np.zeros(int(len(Min)/4))
State2 = np.zeros(int(len(Min)/4))
State3 = np.zeros(int(len(Min)/4))

vb = np.zeros(int(len(Min)/4))
vc = np.zeros(int(len(Min)/4))
vd = np.zeros(int(len(Min)/4))

for a in range(0,len(Min)-1):
    if a % 3 == 0:
        State1[b] = RL[Min[a]]    # Initial states
        vb[b] = b
        b +=1
        
    if a % 3 == 1:
        State2[c] = RL[Min[a]]    # After-first-semicycle states
        vc[c] = c
        c +=1 
        
    if a % 3 == 2:
        State3[d] = RL[Min[a]]    # After-one-complete-AC state
        vd[d] = d
        d +=1


plt.figure(dpi=150)
        
plt.subplot(1, 3, 1)
plt.title("As initiated") 
plt.ylabel("Resistance ($\Omega$)") 
plt.xlabel("Run number (a.u.)")
plt.ylim(2000, 800000) # (5347,323215)
plt.semilogy(vb, State1, "og")

plt.subplot(1, 3, 2)
plt.title("After one semicycle") 
plt.ylabel("Resistance ($\Omega$)") 
plt.xlabel("Run number (a.u.)") 
plt.ylim(2000, 800000) # (5347,323215)
plt.semilogy(vc, State2, "sr")

plt.subplot(1, 3, 3)
plt.title("After complete cycle") 
plt.ylabel("Resistance ($\Omega$)") 
plt.xlabel("Run number (a.u.)")
plt.ylim(2000, 800000) # (5347,323215)
plt.semilogy(vd, State3, "pb")

plt.tight_layout(pad=2.0)

plt.savefig('States@diff-conditions')


RS = np.zeros(4)
RS[0] = np.mean(State1)
RS[1] = np.mean(State2)
RS[2] = np.mean(State3)
RS[3] = np.mean(State4)


from numpy import savetxt
savetxt('RS_individual_memristor.csv', RS, delimiter=',')


print(State2)


minS = argrelextrema(State2, np.less)
print(minS)
print(State2[minS])

print(5 % 4)