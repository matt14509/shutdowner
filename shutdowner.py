import psutil
import time
import os
dwwdww = 999
while dwwdww == 999:


 def checkIfProcessRunning(processName):

    for proc in psutil.process_iter():
        try:

            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

 def findProcessIdByName(processName):

    listOfProcessObjects = []

    for proc in psutil.process_iter():
       try:
           pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
           # Check if process name contains the given name string.
           if processName.lower() in pinfo['name'].lower() :
               listOfProcessObjects.append(pinfo)
       except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
           pass

    return listOfProcessObjects;

 def main():

    print("*** Проверяем есть ли процесс ***")

    if checkIfProcessRunning('GTA5'): #<process name
        print('работает')
    else:
        print("не работает")



    print("*** Ищем pid процессов ***")

    listOfProcessIds = findProcessIdByName('GTA5') #<process name

    if len(listOfProcessIds) > 0:
       print('Process Exists | PID and other details are')
       for elem in listOfProcessIds:
           processID = elem['pid']
           processName = elem['name']
           processCreationTime =  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(elem['create_time']))
           print((processID ,processName,processCreationTime ))

    else :
       print('Нету процесса,завершаем работу пк')
       os.system(['shutdown', '-r' '-t', '0'])



 if __name__ == '__main__':
   main()

