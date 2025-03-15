import socket

def main():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('192.168.1.106', 9955)
        client_socket.connect(server_address)

        student_ids = "12345678,1210608,1000938"
        client_socket.send(student_ids.encode('utf-8'))
        print(f"Sent student IDs to the server: {student_ids}")

        response = client_socket.recv(1024).decode('utf-8')
        print(f"Server response: {response}")

    except socket.error as e:
        print(f"Socket error: {e}")

    finally:
        client_socket.close()

if __name__ == "__main__":
    main()