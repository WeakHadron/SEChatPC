import socket
import _thread
import threading
soc = socket.socket()


port = 6985

soc.connect(('127.0.0.1',port))

def getMsg(soc):
    while True:
        msg = soc.recv(1024)
        if not msg:
            break
        elif str.strip(msg.decode("utf-8")) == 'exit':
            print('Connection closed. Type something to exit ...')
            break
        print(str.strip(msg.decode("utf-8")))
    soc.close()
    
    
    


th = threading.Thread(target=getMsg,args=(soc,),daemon=True)
th.start()


while th.is_alive():
    msg=input()

    if not th.is_alive():
        break
    elif msg == "exit":
        soc.send(str.encode('exit'))
        soc.close()
        break
    elif not th.is_alive():
        soc.close()
        break
    soc.send(str.encode(msg))
    
    

