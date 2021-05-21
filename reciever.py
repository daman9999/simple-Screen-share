from vidstream import StreamingServer
import threading
import socket


#-----************************************************-------#
#                                                            #
#     getting ip address of host machine dynamically         #
#                                                            #
#-----************************************************-------#


# getting the hostname by socket.gethostname() method
hostname = socket.gethostname()
# getting the IP address using socket.gethostbyname() method
IP_ADDRESS = socket.gethostbyname(hostname)
PORT = 9999




#-----************************************************-------#
#                                                            #
#                     streaming the server                   #
#                                                            #
#-----************************************************-------#

reciever = StreamingServer(IP_ADDRESS,PORT)

t = threading.Thread(target=reciever.start_server)
t.start()

while input("") != "STOP":
    continue

reciever.stop_server()
