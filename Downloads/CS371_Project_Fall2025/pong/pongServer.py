# =================================================================================================
# Contributing Authors:	    <Anyone who touched the code>
# Email Addresses:          <Your uky.edu email addresses>
# Date:                     <The date the file was last edited>
# Purpose:                  <How this file contributes to the project>
# Misc:                     <Not Required.  Anything else you might want to include>
# =================================================================================================

from asyncio import Handle
import socket
import threading
import json

def handle_client(conn1:socket.socket, conn2:socket.socket, address:tuple[str,int], playerName:str) -> None:
    print(f"New connection from {address} ({playerName})") #print statement
    try:
        while True:
            #recieve data from client
            data = conn1.recv(1024)
            if not data:
                print(f"Disconnecting from {address}") #print statement
                break
            
            #forwards data from the other client/player
            if conn2:
                conn2.sendall(data)

    except Exception as e:
        print(f"Error with {address}: {e}")
    finally:
        conn1.close()
        print(f"Player disconnected")

def main() -> None:
    HOST = "127.0.0.1"
    PORT = 54321

    server = socket.socket(socket.AF_INET, socket.socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(2)

    print(f"Server started: Listening on {HOST}:{PORT}")

    print("Waiting for Player1 (Left)")
    conn1, addr1 = server.accept()
    print("Player1 Connected!")

    print("Waiting for Player2 (Right)")
    conn2, addr2 = server.accept()
    print("Player2 Connected!")

    thread1 = threading.Thread(target=handle_client, args=(conn1, conn2, addr1))
    thread2 = threading.Thread(target=handle_client, args=(conn2, conn1, addr2))
    thread1.start()
    thread2.start()

    print("Both players Connected: Game Start!")
    
    thread1.join()
    thread2.join()



# Use this file to write your server logic
# You will need to support at least two clients
# You will need to keep track of where on the screen (x,y coordinates) each paddle is, the score 
# for each player and where the ball is, and relay that to each client
# I suggest you use the sync variable in pongClient.py to determine how out of sync your two
# clients are and take actions to resync the games