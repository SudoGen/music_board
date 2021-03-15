import sys
import subprocess
def install(package):
    subprocess.call([sys.executable, "-m", "pip","-q","install", package])
package_q = ['ursina','pynput']

print('Installing')
print('Please wait....')
print('Do not close this program')
for package in package_q:
    install(package)
print('Installation finished')
