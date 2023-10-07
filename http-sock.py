import socket

ip='192.168.1.131'
port=80

try:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print(f"\nSocket created: {sock}.\n")
	try:
		sock.bind((ip, port))
		print(f"\nSocket binded: {ip}:{port}\n")
		sock.listen(1)
		while True:
			try:
				c, (cip, cport)= sock.accept()
				print(f"\nClient's address: {cip}:{cport}.\n")
				try:

					print(c.recv(1024).decode())
					c.send("HTTP/1.0 200 OK\n\n".encode())
					c.send(f"""<html><head><title>DTRS</title><link rel="icon" type="image/x-icon" href=""/></head><body style="background-color: #0088FF; color: #FFFFFF; text-align: center;"><h1>I love you!</h1><h1>(Your IP):(Your port); {cip}:{cport}</h1></body></html>""".encode())
					c.close()
					break
				except:
					print("\nCommunication error.\n")
					break
			except:
				print("\nConnection error.\n")
				break
	except:
		print("\nBind error.\n")
except:
	print("\nSocket error.\n")
	
