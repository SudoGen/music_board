import sys
# importing subprocess module 
import subprocess 
import os
# importing urllib.requests for internet cheking funtions 
import urllib.request 
  
# initializing host to gfg. 
def connect(host='https://google.com/'):
    # trying to open gfg 
    try: 
        urllib.request.urlopen(host) 
        return True
  
    # trying to catch exception when internet is not ON. 
    except: 
        return False
package_q = ['ursina','pynput']

def main(module_name): 
  
    # updating pip to latest version 
    subprocess.run('python -m pip install --upgrade pip') 
  
    # commanding terminal to pip install 
    p = subprocess.run('pip3 install '+module_name) 
  
    # internet off 
    if(p.returncode == 1 and connect() == False): 
        print("error!! occured check\nInternet conection") 
  
    # Every thing worked fine 
    elif(p.returncode == 0): 
        print("It worked", module_name, " is installed") 
  
    # Name of module wrong 
    elif(p.returncode == 1 and connect() == True): 
        print("error!! occured check\nName of module") 
print('Installing')
print('Please wait....')
print('Do not close this program')
for package in package_q:
    main(package)
print('Installation finished')
subprocess.run('python main.py')
