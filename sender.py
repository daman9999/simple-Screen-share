from vidstream import ScreenShareClient
ip_address = input("Enter ip address to connect to ")
sender = ScreenShareClient(ip_address,9999)


reciever = StreamingServer(IP_ADDRESS,PORT)

t = threading.Thread(target=reciever.start_stream)
t.start()

while input("") != "STOP":
    continue

reciever.stop_stream()
