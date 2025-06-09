import socket
import json
import multiprocessing
from question_manager import QuestionManager
from shared_data import SharedData

class QuizServer:
    def __init__(self, host='0.0.0.0', port=5555):
        self.host = host
        self.port = port
        self.question_manager = QuestionManager('questions.json')
        self.shared_data = SharedData()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Servidor PyQuiz rodando em {self.host}:{self.port}")
        
        try:
            while True:
                client_socket, addr = self.server_socket.accept()
                print(f"Conexão estabelecida com {addr}")
                
                # Cria um novo processo para cada cliente
                process = multiprocessing.Process(
                    target=self.handle_client,
                    args=(client_socket, addr)
                )
                process.daemon = True
                process.start()
                
        except KeyboardInterrupt:
            print("\nEncerrando servidor...")
        finally:
            self.server_socket.close()
    
    def handle_client(self, client_socket, addr):
        try:
            player_id = self.shared_data.add_player()
            client_socket.sendall(f"Bem-vindo ao PyQuiz! Seu ID: {player_id}\n".encode())
            
            for question in self.question_manager.get_questions():
                # Envia a pergunta
                client_socket.sendall(f"Pergunta: {question['question']}\nOpções:\n".encode())
                for idx, option in enumerate(question['options']):
                    client_socket.sendall(f"{idx+1}. {option}\n".encode())
                
                # Recebe a resposta
                client_socket.sendall("Sua resposta: ".encode())
                answer = client_socket.recv(1024).decode().strip()
                
                # Verifica a resposta
                if answer == str(question['answer']):
                    self.shared_data.increment_score(player_id)
                    feedback = "Correto!\n"
                else:
                    feedback = f"Incorreto! A resposta correta era {question['answer']}\n"
                
                client_socket.sendall(feedback.encode())
            
            # Mostra pontuação final
            score = self.shared_data.get_score(player_id)
            client_socket.sendall(f"Fim do jogo! Sua pontuação: {score}/{len(self.question_manager.get_questions())}\n".encode())
            
        except ConnectionResetError:
            print(f"Cliente {addr} desconectado abruptamente")
        finally:
            client_socket.close()
            self.shared_data.remove_player(player_id)
            print(f"Conexão com {addr} encerrada")

if __name__ == "__main__":
    server = QuizServer()
    server.start()