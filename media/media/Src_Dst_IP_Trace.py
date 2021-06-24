from scapy.all import *             # Scapy is a packet manipulation tool for computer networks.
from colored import fg, attr        # Python library for color and formatting in terminal.

c1 = fg(198)
c2 = fg(202)
c3 = fg(190)
reset = attr('reset')

def main():
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
    print(c2 + "\nTracing The Path.... Please Wait!" + reset)


main()

# Sniffing Source and Destination IP Address.
sniff(filter="ip", prn=lambda x:x.sprintf(c3 +"\nSource IP Address: "+'{IP:%IP.src% -> '+"Dest IP Address: "+'%IP.dst%\n}' + reset))

