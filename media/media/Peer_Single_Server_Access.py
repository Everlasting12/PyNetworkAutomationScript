import socket        # way of connecting two nodes on a network to communicate with each other.
import sys           # module provides functions and variables which are used to manipulate different parts of the Python Runtime Environment.
import time          # time module provides many ways of representing time in code.

# Create socket (allows two computers to connect)
def socket_creation():
    try:
        global host
        global port
        global s
        host = '192.168.0.113' # Update IP if configured through DHCP.
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket Creation Error :" + str(msg))


# Bind socket to port (the host and port the communication will take place) and wait for connection from client
def socket_binding():
    try:
        global host
        global port
        global s
        print("\nBinding The Port : " + str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Socket Binding Error : " + str(msg) + "Retrying.....")
        time.sleep(5)
        socket_binding()

# Establishing and accepting connection
def socket_accept():
    conn, addr = s.accept()
    print(("\nConnection Has Been Established " + "IP : " + addr[0] + " Port : " + str(addr[1])))
    print("pynas : " + str(addr[0]) + " > ", end="")
    send_commands(conn)


# sending commands
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit(0)
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_resp = str(conn.recv(20480).decode("utf-8"))
            print(client_resp, end="")

def main():
    print("WELCOME TO PyNETWORK AUTOMATION SCRIPTS (PyNAS)")
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
    print("---------------------------------------------\n")

    socket_creation()
    socket_binding()
    socket_accept()


main()

