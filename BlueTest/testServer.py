import bluetooth

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_sock.bind(("",bluetooth.PORT_ANY))

server_sock.listen(1)
port = server_sock.getsockname()[1]

uuid="94f39d29-7d6d-437d-973b-fba39e49d4ee"

bluetooth.advertise_service(server_sock, "SampleServer", service_id=uuid, service_classes=[uuid,bluetooth.SERIAL_PORT_CLASS], profiles=[bluetooth.SERIAL_PORT_PROFILE], protocols=[bluetooth.OBEX_UUID])

print("Waiting for connectio port: ", port)

client_sock,client_info=server_sock.accept()
print("Accepted connection:",client_info)

try:
	while True:
		date = client_sock.recv(1024)
		if not data:
			break
		print("recieved:",data)
except OSError:
	pass

print("disconnect")

client_sock.close()
server_sock.close()
print("done")
