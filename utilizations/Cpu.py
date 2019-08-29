from psutil import *
from time import sleep
def cpu_utilizations(_interval,process):#
    for util in range(process):
        print(cpu_percent(interval=_interval,percpu=True))
_interval=int(input())
process=int(input())
print(cpu_utilizations(_interval,process))