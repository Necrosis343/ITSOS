import users
import pw
act=0
def init(usr, pw):
    print("""
 ___   _______  _______  _______  _______ 
|   | |       ||       ||       ||       |
|   | |  _____||_     _||   _   ||  _____|
|   | | |_____   |   |  |  | |  || |_____ 
|   | |_____  |  |   |  |  |_|  ||_____  |
|   |  _____| |  |   |  |       | _____| |
|___| |_______|  |___|  |_______||_______| Founded, by Mikhael.
""")
    if usr==king.name:
        if pw==king.pw:
            print(f"Hello, {king.name}.")
            act=1
        else:
            print("Invalid!")
    elif usr==sub.name:
        if pw==sub.pw:
            print("Hello, {sub.name}.")
            act=1
        else:
            print("Invalid!")
    else:
        print("Invalid!")
