import brain
if brain.act==1:
        verify=input("\n")
        if(verify==brain.pw):
                print(f"\nHello, {brain.vis}.\n")
                brain.init()
                while(True):
                        cmd=input()
                        if(cmd[:4].lower()=="exit"):
                                print(f"\nGoodbye, {brain.anon}.\n")
                                exit()

                        elif(cmd[:4].lower()=="time"):
                                import time
                                print("\n",time.ctime(time.time()),"\n")
                        #elif(cmd[:3].lower()=="rsh"):
                  
                        else:
                                print("\nI dont understand.\n")

        else:
                print(f"You're not {brain.anon}!\n")
~
