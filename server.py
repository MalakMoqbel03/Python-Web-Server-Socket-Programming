import socket
import time
import os
import platform

def lock_screen():
    system_platform = platform.system()

    if system_platform == "Darwin":  # macOS
        os.system("osascript -e 'tell application \"System Events\" to keystroke \"q\" using {command down, control down}'")
    elif system_platform == "Linux":
        os.system("gnome-screensaver-command -l")
    else:
        print("Screen lock not supported on this platform.")

def connection(client_socket, student_ids):
    # Split the received student IDs
    ids_list = student_ids.split(',')

    for studentID in ids_list:
        print(f"Received student ID: {studentID}")

        # Check if the student ID is valid or not
        if studentID in ["1210608", "1210221", "1201264"]:
            print("Valid ID")
            response = "Welcome to the server!"
            client_socket.send(response.encode('utf-8'))

            print("The OS will lock the screen after 10 seconds")

            # Send a message to the client about the screen lock
            client_socket.send("Locking screen in 10 seconds...".encode('utf-8'))

            # Wait for 10 seconds
            time.sleep(10)

            # Lock the screen
            lock_screen()

            print("Screen locked!")
        else:
            print("Invalid ID")
            response = "Invalid ID"

        try:
            # Send the response to the client
            client_socket.send(response.encode('utf-8'))
        except (BrokenPipeError, ConnectionResetError):
            print("Client disconnected.")

    # Close the client socket after handling the connection for all student IDs
    client_socket.close()

def handle_client(client_socket, address):
    print(f"Connection from {address} has been established!")
    
    # Send a welcome message to the client
    client_socket.send(bytes("Welcome to the server!", "utf-8"))

    # Receive data from the client and handle the connection
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Received data from the client: {data}")

    # Handle the connection based on student IDs
    connection(client_socket, data)

def main():
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    sAddress = ('192.168.1.106', 9955)
    server_socket.bind(sAddress)

    # Listen for incoming connections
    server_socket.listen(5)
    print("Server is listening on port 9955")

    while True:
        # Accept a new connection
        client_socket, caddress = server_socket.accept()

        # Handle the client connection without using threads
        handle_client(client_socket, caddress)

if __name__ == "__main__":
    main()