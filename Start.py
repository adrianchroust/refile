"""
import sys
if "win32" not in sys.platform:
    import time
    print("Leider funktioniert das Programm nur auf Windows :(")
    time.sleep(2)
else:
    import os
    os.chdir(os.path.join(os.getcwd(),"Library"))
    os.system("execute.py")
"""
import os
os.chdir(os.path.join(os.getcwd(),"Library"))
os.system("execute.py")
