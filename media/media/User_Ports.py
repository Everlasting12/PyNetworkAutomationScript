from nmap import *                       # python-nmap is a python library which helps in using nmap port scanner.
from colored import fg, attr             # Python library for color and formatting in terminal.

ns = nmap.PortScanner()                 # initialize the port scanner
c1 = fg(202)
c2 = fg(11)
c3 = fg(10)
c4 = fg('green')
c5 = fg('blue')
reset = attr('reset')

print(c1 + "WELCOME TO PyNETWORK AUTOMATION SCRIPTS (PyNAS)")
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
print(c2 + "Nmap Version : ",ns.nmap_version())
print(reset)

def Open_Ports():   # function for open ports
    IP = input("\nEnter IP Address to scan : ")
    print(c5 + "Scanning User Ports Please Wait......" + reset)
    ns.scan(IP, '1024-49151', '-v')                                        # Function for scanning opened system ports.
    print(c4)
    print(ns.scaninfo())
    print(ns.scanstats())
    print(reset)
    print("\nOpen User Ports :")
    print(c4)

    print(ns.csv().strip('host;hostname;hostname_type;protocol;port;name;state;product;extrainfo;reason;version;conf;cpe'))
    print("Host is : ", ns[IP].state() + reset)
    print(c3 + "Scan Complete!!!" + reset)

def main():
    Open_Ports()                                            # Calling function
main()

