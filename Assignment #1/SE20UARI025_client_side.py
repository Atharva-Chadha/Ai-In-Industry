# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 22:18:26 2023

@author: Atharva Chadha
"""

import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = "10.59.207.96"  # server ip address
    server_port = 8765  # Use the same port number as the server
    
    client_socket.connect((server_ip, server_port))
    
    while True:
        message = input("atharva here ")
        client_socket.send(message.encode())
        
        response = client_socket.recv(1024).decode()
        print(f"Received from server: {response}")
        
        if message.lower() == "exit":
            break
        
    client_socket.close()

if __name__ == "__main__":
    start_client()
