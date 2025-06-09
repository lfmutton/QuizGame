# QuizGame# 🧠 PyQuiz

**PyQuiz** é um jogo multiplayer de perguntas e respostas desenvolvido em Python. Ele utiliza **sockets TCP** para comunicação entre cliente e servidor, suporte a **múltiplos jogadores simultâneos via multiprocessing** e perguntas carregadas dinamicamente de um arquivo JSON.

## 📌 Funcionalidades

- Servidor multiusuário com suporte a múltiplas conexões simultâneas.
- Interface em linha de comando simples e intuitiva.
- Sistema de pontuação por jogador.
- Carregamento dinâmico de perguntas a partir de arquivo `questions.json`.
- Gerenciamento seguro de dados compartilhados entre processos.

---

## 🗂 Estrutura do Projeto

```
pyquiz/
├── server.py             # Código principal do servidor
├── client.py             # Código principal do cliente
├── question_manager.py   # Gerencia o carregamento e salvamento de perguntas
├── shared_data.py        # Dados compartilhados entre processos
├── questions.json        # Arquivo com perguntas e respostas
└── README.md             # Este arquivo
```

---

## ▶️ Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/pyquiz.git
cd pyquiz
```

### 2. Execute o servidor

Em um terminal:

```bash
python server.py
```

O servidor será iniciado em `0.0.0.0:5555`.

### 3. Execute um ou mais clientes

Em outros terminais (ou em diferentes máquinas na mesma rede):

```bash
python client.py
```

Você será conectado ao servidor e poderá começar a jogar.

---

## 🧪 Exemplo de Uso

- O cliente recebe uma pergunta com múltiplas opções.
- Ele responde digitando o número correspondente à opção correta.
- O servidor responde com "Correto!" ou "Incorreto!".
- No fim do quiz, a pontuação total é exibida.

---

## 📄 Formato do Arquivo `questions.json`

O arquivo deve conter uma lista de perguntas com o seguinte formato:

```json
[
  {
    "question": "Qual é o sistema operacional desenvolvido pela Microsoft?",
    "options": ["Linux", "macOS", "Windows", "Android"],
    "answer": 3
  }
]
```

**Nota:** A resposta correta deve ser o número da opção correta (base 1).

---

## 🚧 Melhorias Futuras

- Interface gráfica (GUI) com Tkinter ou PyQt.
- Persistência de ranking em banco de dados.
- Timer para resposta e suporte a rodadas.
- Modo de jogo por equipes.

---

## 📚 Requisitos

- Python 3.6 ou superior
- Não são necessárias bibliotecas externas

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

---

## 🧑‍💻 Autor

Desenvolvido por Luís Mutton – Projeto acadêmico.

---

## 📜 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
