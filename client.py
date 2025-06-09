import socket

class QuizClient:
    def __init__(self, host='localhost', port=5555):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def connect(self):
        try:
            self.client_socket.connect((self.host, self.port))
            print("Conectado ao servidor PyQuiz!")
            
            while True:
                data = self.client_socket.recv(1024).decode()
                if not data:
                    break
                    
                print(data, end='')
                
                if "Sua resposta:" in data:
                    answer = input()
                    self.client_socket.sendall(answer.encode())
                    
        except ConnectionRefusedError:
            print("Não foi possível conectar ao servidor")
        except KeyboardInterrupt:
            print("\nDesconectando...")
        finally:
            self.client_socket.close()

if __name__ == "__main__":
    client = QuizClient()
    client.connect()