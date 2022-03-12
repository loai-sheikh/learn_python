import subprocess
import sys

#subprocess.run("notepad")
process = subprocess.Popen(
    "ca.exe https://www.ynet.co.il/", stdout=subprocess.PIPE, stderr=subprocess.PIPE
)

#process = subprocess.run(
#    "ca.exe https://www.ynet.co.il/", stdout=subprocess.PIPE, stderr=subprocess.PIPE
#)

#process = subprocess.run(
#    "dir", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
#)

print(process.stdout)