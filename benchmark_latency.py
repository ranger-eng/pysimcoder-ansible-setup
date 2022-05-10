import os
import numpy as np
import matplotlib.pyplot as plt

name = "5.13.0-40-generic-PREEMPT-RT==FALSE"

num_loops = 1000000
os.system("sudo cyclictest -l{} -m -S -p90 -i200 -h400 -q >".format(num_loops)+name+".txt")
os.system('grep -v -e "^#" -e "^$" {}.txt | tr " " "," | tr "\t" "," > {}.csv'.format(name, name))

data = np.loadtxt("{}.csv".format(name), dtype=float, delimiter=',')

plt.bar(data[:,0],data[:,1])
plt.bar(data[:,0],data[:,2])
plt.bar(data[:,0],data[:,3])
plt.bar(data[:,0],data[:,4])

plt.yscale("log")

plt.title("cyclictest {}".format(name))
plt.ylabel("counts [out of {}]".format(num_loops))
plt.xlabel("latency [us]")
plt.legend(["core1 - 200us", "core2 - 700us","core3 - 1200us","core4 - 1700us"])

plt.grid(True, which='both', linestyle='--')

plt.show()
