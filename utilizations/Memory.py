from psutil import *
from time import sleep
def memory_utilization(interval,required_utilizations):
    a=virtual_memory()
    for i in range(required_utilizations):
        print(a.percent)
        sleep(interval)
    return "Task Completed"
interval=int(input())
required_utilization=int(input())
print(memory_utilization(interval,required_utilization))