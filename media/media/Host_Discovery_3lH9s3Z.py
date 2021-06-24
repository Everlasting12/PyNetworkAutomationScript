import nmap                             # python-nmap is a python library which helps in using nmap port scanner.
from getmac import get_mac_address      # Pure-Python package to get the MAC address of network interfaces and hosts on the local network.
from colored import fg, attr            # Python library for color and formatting in terminal.

ns = nmap.PortScanner()     # initialize the port scanner

color2 = fg(9)
color3 = fg(11)
color4 = fg(10)
reset = attr('reset')


print(color2 + "WELCOME TO PyNETWORK AUTOMATION SCRIPTS (PyNAS)")
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
print("---------------------------------------------\n" + reset)
print(color3 + "Nmap Version : ",ns.nmap_version())
print(reset)

class Network(object):
    def __init__(self):
        ip = input("\nPlease Enter IP Address Range (Default is 192.168.0.1) : ")   # Class for inserting IP Address range
        self.ip = ip


    def __GET_Mac(self, IP=''):
        mac = get_mac_address(ip=IP)            # Creating function for MAC address.
        return mac
    def networkscanner(self):
        if len(self.ip)==0:
            network = '192.168.0.1/24'          # Function for taking range of IP
        else:
            network = self.ip + '/24'
        color5 = fg(130)
        print(color5 + "Scanning Host Please Wait.......\n" + reset)

        ns.scan(hosts=network, arguments='-sn')
        host_list = [(x, ns[x]['status']['state']) for x in ns.all_hosts()]
        for host, status in host_list:
            mac = self.__GET_Mac(IP=host)                                           # Obtaining MAC Address from IP
            color = fg('green')
            print(color + "Host: {}\t\tMAC: {}\t".format(host, mac) + reset)


        print(color4 + "\nScan Completed !!!" + reset)
def main():

    D = Network()
    D.networkscanner()

main()



