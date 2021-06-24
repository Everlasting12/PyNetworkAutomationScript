from socket import *            # connecting two nodes on a network to communicate.
from nmap import *              # python-nmap is a python library which helps in using nmap port scanner.
import optparse                 # library for parsing command-line options.
import threading                # used to run multiple threads (tasks, function calls) at the same time.
from colored import fg, attr    # Python library for color and formatting in terminal.

ns = nmap.PortScanner()          # initialize the port scanner
reset = attr('reset')


def portScan(host , port):
    try:
        s = socket(AF_INET , SOCK_STREAM)
        s.connect((host , int(port)))
        print("\n" + "IP" + "\t" + "PROTOCOL" + "\t" + "STATE")
        print("-----------------------------------------------")
        c10 = fg(10)
        print(c10 + "[+]" + host + " tcp/" + str(port) + " open" + reset)
        s.close() # closing socket

    except:
        print("\n" + "IP" + "\t" + "PROTOCOL" + "\t" + "STATE")
        print("----------------------------------------------")
        c196 = fg(196)
        print(c196 + "[-]" + host + " tcp/" + str(port) + " closed" + reset)


def main():
    c226 = fg(226)

    print(c226+ "WELCOME TO PyNETWORK AUTOMATION SCRIPTS (PyNAS)")
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
    print("                   ***              *--------------------------------------------*     " + reset)

    c214 = fg(214)
    print(c214 + "\nHAVE A LOOK INTO YOUR NETWORK & SECURE IT.")
    print("-------------------------------------------\n" + reset)

    # Taking user inputs
    parser = optparse.OptionParser("usage%prog " + "-H <specify target host> -p <specify ports separated by ',' >")

    parser.add_option("-H" , '--host' , dest = 'targethost' , type = 'string' , help = 'specify target host')
    parser.add_option("-p" , '--ports' , dest = 'targetports', type = 'string' , help = 'specify target ports separated by "," ')

    option , args = parser.parse_args()

    thost = option.targethost
    tports = str(option.targetports).split(",")


    if thost == None or tports[0] == None:
        print(parser.usage)
        exit(0)
    c153 = fg(153)
    print(c153 + "\nNmap Version : ", ns.nmap_version())
    print(reset)
    c184 = fg(184)
    print(c184 + "\nScanning Host Please Wait......" + reset)
    host_ip = gethostbyname(thost)

    for port in tports:

        t = threading.Thread(target=portScan , args=(host_ip,port))
        t.start()
        ns.scan(host_ip, port)
        c172 = fg(172)

        print(c172 + ns.csv().strip('host;hostname;hostname_type;protocol;port;name;state;product;extrainfo;reason;version;conf;cpe'))
        print(ns.scaninfo())
        print(ns.scanstats())
        print(reset)
    c190 = fg(190)
    print(c190 + "\nScan Complete !!!" + reset)

main()


