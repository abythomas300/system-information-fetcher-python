
import platform
import os
import datetime
start = datetime.datetime.now()
print('\n*    *   *   *  * SYSTEM INFORMATION *  *   *    *     *')
print('Platform processor used: ', platform.processor())
print('Platform architecture: ', platform.architecture())
print('Machine type: ', platform.machine())
print('System network name: ', platform.node())
print('Operating System used: ', platform.system())
print('Current working directory:', os.getcwd())
print('Python Compiler used: ', platform.python_compiler())
time_status = datetime.datetime.now()

#Creating a file and writing timestamps whenever the program is run.
str_time_status = str(time_status) #converting time and date output to string type for printing.
f = open("AccessedTimeLive.txt", "a")
f.write("\nSystem Information has been accessed at:" + str_time_status)
f.close()
end = datetime.datetime.now()
difference = end - start
print('Time taken ', difference.total_seconds(), 'seconds.')
