import main
if main.act==1:
        verify=input("\n")
        if(verify==main.pw):
                print(f"\nHello, {main.king}.\n")
                main.init()
                while(True):
                        cmd=input()
                        if(cmd[:4].lower()=="exit"):
                                print(f"\nGoodbye, {main.king}.\n")
                                exit()

                        elif(cmd[:4].lower()=="time"):
                                import time
                                print("\n",time.ctime(time.time()),"\n")
                        #elif(cmd[:3].lower()=="rsh"):
                  
                        else:
                                print("\nI dont understand.\n")

        else:
                print(f"Invalid!\n")
~
