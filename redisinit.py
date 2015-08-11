import os

def Run_Redis():
    os.chdir('C:/APP/Redis')
    os.system('redis-server.exe redis.windows.conf')