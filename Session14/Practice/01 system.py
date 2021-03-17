# get information about user's system 

import psutil
import platform
from os import *
from datetime import datetime


def CPU_Info_OS() :
    print("--- CPU Info OS ---")
    if platform.system() == "Windows" :
        return platform.processor() 
    elif platform.system() == "Linux" :
        command = "cat /proc/cpuinfo" 
        return popen(command).read().strip() 
    else :
        return "Platform not Identified "


def get_size(bytes , suffix="B") : 
    factor = 1024 
    for unit in ["","K","M","G","T","P"] : 
        if bytes < factor : 
            return f"{bytes:2f}{unit}{suffix}"
        bytes /= factor


def Platform_Info() : 
    print("--- System Information ---")
    uname = platform.uname() 
    print(f"System : {uname.system}")
    print(f"Node Name : {uname.node}")
    print(f"Release : {uname.release}")
    print(f"Version : {uname.version}")
    print(f"Machine : {uname.machine}")
    print(f"Processor : {uname.processor}")
   

def Boot_Info() : 
    print("--- Boot Time ---")
    boot_time_timestamp = psutil.boot_time() 
    bt = datetime.fromtimestamp(boot_time_timestamp)
    print(f"Boot Time : {bt.year}/{bt.month}/{bt.day} {bt.hour} : {bt.minute} : {bt.second}")


def CPU_Info() : 
    print("--- CPU Info ---")
    print("Physical cores : ",psutil.cpu_count(logical=False))
    print("Total cores : ",psutil.cpu_count(logical=True))

    cpufrequ = 



# print(CPU_Info_OS() )