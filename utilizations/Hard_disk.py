from psutil import *
from time import sleep
def usage(details_about):
    disk=disk_usage('/')
    if details_about=='free':
        return 'free='+str(disk.free)
    else:
        return 'total=' + str(disk.total)
details_about=input()
print(usage(details_about))