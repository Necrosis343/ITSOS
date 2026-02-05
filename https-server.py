# Python HTTPS Server
# TO-DO:  Mobile compatibility.

import socket
import ssl
import os
import threading

class HTTPS_Server:
	def __init__(self, addr:str='', port:int=443, path=None, cert=None, key=None):
		self.major=1
		self.minor=2
		self.addr=addr
		self.port=port
		self.path=path
		self.cert=cert
		self.key=key

	def sock(self):
		try:
			self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			print("\nSocket initiated!\n")
		except socket.error as err:
			print(f"\nSocket failure!\n{err}\n")
			return
			
	def bind(self):
		print("\nBinding socket...\n")
		wait=True
		t=10
		if self.path is not None:
			try:
				os.chdir(self.path)
			except Exception as err:
				print(f"\nFilepath error: {err}\n")
		while wait:
			try:
				self.s.bind((self.addr,self.port))
				print(f"\nSocket binded to {self.addr}:{self.port}\n")
				wait=False
			except socket.error as err:
				print(f"\nFailed to bind {self.addr}:{self.port}!\n{err}\n")
				import time
				print(f"\nRetrying in {t} seconds\n")
				time.sleep(10)

	def authenticate(self): # set OPENSSL_CONF=C:\Program Files\OpenSSL-Win64\bin\openssl.cnf
		if self.cert is not None and self.key is not None:
			try:
				if not os.path.exists(self.cert) or not os.path.exists(self.key): 
					os.system("openssl req -new -x509 -days 365 -nodes -out cert.pem -keyout key.pem")
				self.context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
				self.context.load_cert_chain(certfile=self.cert, keyfile=self.key)
				self.s = self.context.wrap_socket(self.s, server_side=True)
				print("Authentication done.\n")
			except Exception as err:
				print(f"\nAuthentication failure: {err}\n")
				return

	def handler(self, c):
		while True:
			try:
				data = c.recv(1024).decode()
				if not data:
					break
				print(data)
				r = data.split()[1]
				print('\nRequest:', r,'\n')
				if r == "/":
					c.sendall('''HTTP/1.1 200 OK\n'''.encode())
					f=open('index.html')
					o=f.read()
					f.close()
					c.sendall(o.encode())
					c.close()
					print(f"\nSent {self.path}/index.html\n")
				elif r[-5:]==".html":
					c.sendall('''HTTP/1.1 200 OK\n'''.encode())
					f=open(r[1:])
					o=f.read()
					f.close()
					c.sendall(o.encode())
					c.close()
					print(f"\nSent {self.path}{r[1:]}\n")
				elif r[-4:]=='.css':
					f=open(r[1:])
					o=f.read()
					f.close()
					sty='''HTTP/1.1 200 OK
Content-Type: text/css\n
'''+o
					c.sendall(sty.encode())
					c.close()
					print(f"\nSent {self.path}{r[1:]}n")
				elif r[-4:]==".png":
					f=open(r[1:], "rb")
					o=f.read()
					f.close()
					png='''HTTP/1.1 200 OK
Content-Type: image/png\n
'''
					c.sendall(png.encode+o)
					c.close()
					print(f"\nSent: {self.path}{r[1:]}\n")
			except Exception as e:
				print(f"\nERR! {e}\n")
				return

	def server(self):
		self.s.listen()
		print("\nSocket is listening...\n")
		while True:
			try:
				c,addr=self.s.accept()
				print(f"\n{addr} has connected.\n")
				threading.Thread(target=self.handler, args=(c,)).start()
			except Exception as e:
				print(f"Error: {e}")

	def main(self):
		self.sock()
		self.bind()
		self.authenticate()
		self.server()

if __name__ == "__main__":
	server=HTTPS_Server(addr="", path="", cert='./cert.pem', key='./key.pem')
	server.main()


