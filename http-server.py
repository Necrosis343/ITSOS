# Python HTTP Server
# TO-DO:  Mobile compatibility.

class HTTP-Server:
 vmajor= 1
 vminor=1
	def __init__(self):
		self.major=vmajor
		self.minor=vminor
	def sock(self):
		print("\nInitiating socket...\n")
		import socket
		try:
		  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		  print("\nSocket initiated!\n")
		except socket.error as err:
		  print(f"\nSocket failure!\n{err}\n")
	def bind(self):
		print("\nBinding socket...\n")
    ip="192.168.0.211"
    port=80
    wait=True
    t=10
    while wait:
    	try:
    		s.bind((ip,port))
    		print(f"\nSocket binded to {ip}:{port}\n")
  	  	wait=False
    	except socket.error as err:
    		print(f"\nFailed to bind {ip}:{port}!\n{err}\n")
    		import time
  	  	print(f"\nRetrying in {t} seconds\n")
    		time.sleep(10)
	def listen(self):
		s.listen()
    print("\nSocket is listening...\n")
	def server(self):
    import os
    import sys
    while True:
    	try:
    		os.chdir("/home/kali/Documents/TIRD-Website")
    		c,addr=s.accept()
    		print(f"\n{addr} has connected.\n")
    		r=c.recv(1024).split()[1].decode()
    		d=r.strip('/')
    		print(f"Requesting:",r)
    		if r=='/':
  	  		c.sendall('''HTTP/1.1 200 OK\n'''.encode())
    			f=open(os.getcwd()+'/index.html')
    			o=f.read()
    			f.close()
    			print("\nSending:",os.getcwd()+"/index.html","\n")
    			c.sendall(o.encode())
    		if d[-4:]=='.css':
    			f=open(os.getcwd()+'/style.css')
    			o=f.read()
  	  		f.close()
  	  		sty='''HTTP/1.1 200 OK
Content-Type: text/css\n
'''+o
    			print("\nSending:",os.getcwd()+r,"\n")
    			c.sendall(sty.encode())
    		if d[-3:]=='.js':
    			f=open(os.getcwd()+r)
    			o=f.read()
    			f.close()
    			js='''HTTP/1.1 200 OK
Content-Type: text/javascript\n
'''+o
    			print('Sending:', os.getcwd()+r,"\n")
  	  		c.sendall(js.encode())
    		if d[-4:]=='.ico':
          ico='''HTTP/1.1 200 OK
Content-Type: image/x-icon\n'''
    			print('Sending empty icon...')
    			c.sendall(ico.encode())
    		else:
    			f=open(os.getcwd()+r)
    			o=f.read()
    			f.close()
    			http='''HTTP/1.1 200 OK\n'''+o
    			print("Sending:",os.getcwd()+r,"\n")
    			c.sendall(http.encode())
    		c.close()
    	except socket.error as err:
        print(f"\nCommunication error!\n{err}\n")
				
server=HTTP-Server()
server.sock()
server.bind()
server.listen()
server.server()

