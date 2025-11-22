
# =================================================================================================
# Contributing Authors:	    Andres Aguirre
# Email Addresses:          <Your uky.edu email addresses>
# Date:                     <The date the file was last edited>
# Purpose:                  <How this file contributes to the project>
# Misc:                     <Not Required.  Anything else you might want to include>
# =================================================================================================

from asyncio import Handle
import socket
import threading

def handle_client(conn1:socket.socket, conn2:socket.socket, addr:tuple[str,int], playerName:str) -> None:
    print(f"New connection from {addr} ({playerName})") #server start statement
         
    try:
        while True:
            #recieve data from client
            data1 = conn1.recv(1024)
            if not data1:
                print(f"Disconnecting from {addr}") #client disconnect statement
                break
            
            #forwards data from the other client/player
            conn2.sendall(data1)

            data2 = conn2.recv(1024)
            if not data2:
                print(f"Disconneting from {addr}")
                break

            conn1.sendall(data2)

    except Exception as e:
        print(f"Error with {addr}: {e}")
    finally:
        conn1.close()
        conn2.close()
        print(f"Player disconnected") #end of client-server connection
    

def main() -> None:
    HOST = "0.0.0.0"
    PORT = 49513
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 480

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT)) #waits for a connction to local host on port 54321
    server.listen(2)

    print(f"Server started: Listening on {HOST}:{PORT}")

    print("Waiting for Player1 (Left)")
    conn1, addr1 = server.accept()
    print("Player1 Connected!")

    config1 = f"{SCREEN_WIDTH},{SCREEN_HEIGHT},left" #send screen information and which paddle they are
    conn1.sendall(config1.encode('utf-8'))

    print("Waiting for Player2 (Right)") 
    conn2, addr2 = server.accept()
    print("Player2 Connected!")

    config2 = f"{SCREEN_WIDTH},{SCREEN_HEIGHT},right"
    conn2.sendall(config2.encode('utf-8'))

    thread1 = threading.Thread(target=handle_client, args=(conn1, conn2, addr1, "Player1")) #creates threads to sync both players
    thread2 = threading.Thread(target=handle_client, args=(conn2, conn1, addr2, "Player2"))
    thread1.start()
    thread2.start()

    print("Both players Connected: Game Start!")
    
    thread1.join()
    thread2.join()
    
    server.close()

if __name__ == "__main__":
    main()


# Use this file to write your server logic
# You will need to support at least two clients
# You will need to keep track of where on the screen (x,y coordinates) each paddle is, the score 
# for each player and where the ball is, and relay that to each client
# I suggest you use the sync variable in pongClient.py to determine how out of sync your two
# clients are and take actions to resync the games