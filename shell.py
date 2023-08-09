import main
import usr
def shell(usr):
	print(main.ShellLogo)
	if usr=="Mikhael":
		while usr=="Mikhael":
			c=input(f"\n{usr}/Shell: ")
			if c=="shell":
				print(main.ShellLogo)
			elif c=="rsh":
				print(main.RSHLogo)
			elif c=="help":
				print("\nShell, RSH, help, exit.\n")
			elif c=="exit":
				break	
		print(f"Goodbye, {usr}.")
	elif usr=="IST":
		print(f"Goodbye, {usr}.")
def logon():
	i0=input("\nUsername: ")
	i1=input("\nPassword: ")
	if i0==usr.king[0]:                                  
		if i1==usr.king[1]:                             
			print(f"Signed in, as {usr.king[0]}.")   
			shell(usr.king[0])                   
		else:                                           
			print("Invalid!")                       
	elif i0==usr.sub[0]:                                  
		if i1==usr.sub[1]:                              
			print(f"Signed in, as {usr.sub[0]}.")   
			shell(usr.sub[0])                    
		else:                                           
			print("Invalid!")                       
	else:                                                   
		print("Invalid!")
main.init()
logon()
