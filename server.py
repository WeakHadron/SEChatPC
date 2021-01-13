import socket
import _thread
import threading


socs = []

def socT(mconn,pconn,msoc):
    
    while True:
        msg = mconn.get('conn').recv(1024).decode("utf-8")
        if not msg:
            break
        pconn.get('conn').send(str.encode(msg+"\n"))
    mconn.get('conn').close()
    pconn.get('conn').close()
    msoc.close()

    print('Connection closed')
    
        
        


soc = socket.socket()
soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 6985
soc.bind(('',port))
soc.listen(5)

for i in range(2):
    if i == 0:
        s = 1
    elif i == 1:
        s = 0
    conn,addr = soc.accept()
    socs.append({'conn': conn , 'addr' : addr})
    print("Connection {0} established".format(i+1))

x = threading.Thread(target=socT, args=(socs[0],socs[1],soc),daemon=True)
y = threading.Thread(target=socT, args=(socs[1],socs[0],soc),daemon=True)
x.start()
y.start()
print('Communication started')
while x.is_alive() and y.is_alive():
    continue


soc.close()
