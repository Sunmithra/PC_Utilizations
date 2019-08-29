from psutil import *
from time import sleep
def cpu_utilizations(_interval,process):            #CPU UTILIZATION
    for util in range(process):
        print(cpu_percent(interval=_interval,percpu=True))
    return 'Task Completed\n'
def memory_utilization(process,delay):              #MEMORY UTILIZATION
    a=virtual_memory()
    for util in range(process):
        print(a.percent)
        sleep(delay)
    return "Task Completed\n"
def usage(details_about):                           #USAGE OF HARD DISK
    disk=disk_usage('/')
    if details_about=='free':
        return 'free='+str(disk.free)
    else:
        return 'total=' + str(disk.total)

while(True):
    print('Enter Your Required Command Number:\n')
    command=int(input('1.CPU Utilization\n''2.Memory Utilization\n''3.Hard Disk Space\n''4.Exit\n'))

    if command==1:
        print('Details of CPU Utilization:\n')
        _interval=int(input('Enter the required interval:\n'))
        process=int(input('Please enter how many times you would like to continue:\n'))
        print(cpu_utilizations(_interval,process))
        a=input('Would you like to continue for other commands(yes/no:)\n').lower()#Converting all the input into lower_alpha
        if a=='yes':
            pass
        elif a=='no':
            break
        else:
            print('Invalid Input')

    elif command==2:
        print('Details of Memory Utilizaton:\n')
        process = int(input('Please enter how many times you would like to continue:\n'))
        delay=int(input('Please enter the delay you wish to see between each utilization:\n'))#delay in seconds
        print(memory_utilization(process,delay))
        a = input('Would you like to continue for other commands(yes/no:)\n').lower()
        if a == 'yes':
            pass
        elif a == 'no':
            break
        else:
            print('Invalid Input')

    elif command==3:
        print('Details of Hard Disk Usage:\n')
        details_about=input('Please choose the one which you wish to see->free or total\n').lower()
        print(usage(details_about))
        print('Task Completed')
        a = input('Would you like to continue for other commands(yes/no:)\n').lower()
        if a == 'yes':
            pass
        elif a == 'no':
            break
        else:
            print('Invalid Input')
    else:
        print('Thank You!')
        break




