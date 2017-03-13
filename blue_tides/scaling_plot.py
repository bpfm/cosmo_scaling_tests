import numpy as np
import matplotlib.pyplot as plt

n_part=256.0

speed_256=np.zeros(shape=(8))
speed_512=np.zeros(shape=(3))
speed_1024=np.zeros(shape=(2))

proc_256=[24,48,96,192,384,768,1536,3072]
time_256=[2406.0,1480.0,852.0,627.0,527.0,381.0,320.0,1033.0]

proc_512=[192,384,768]
time_512=[4413.0,2631.0,1823.0]

proc_1024=[1536,3072]
time_1024=[9960.0,5159.0]

for i in range(6):
    speed_256[i]=256**3/time_256[i]/proc_256[i]

for i in range(3):
    speed_512[i]=512**3/time_512[i]/proc_512[i]

for i in range(2):
    speed_1024[i]=1024**3/time_1024[i]/proc_1024[i]   
    
plt.plot(proc_256,speed_256)
plt.plot(proc_512,speed_512)
plt.plot(proc_1024,speed_1024)
plt.title("Scaling Efficiency")
plt.xlabel("# Cores")
plt.ylabel("Efficiency [particles / second / core]")
plt.legend(["256^3 particles","512^3 particles","1024^3 particles"])
plt.show()
