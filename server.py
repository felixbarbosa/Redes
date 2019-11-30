import socket
from playsound import playsound

print ("Servidor")

A = False
HOST = '192.168.43.33'             # Endereco IP do Servidor
PORT = 9876           # Porta que o Servidor esta
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
arquivo = open('musicaCliente.mp3', 'wb') # O arquivo que vai receber do cliente
orig = (HOST, PORT)
server.bind(orig)
server.listen(5)
while True:
    con, cliente = server.accept()
    print ('Aceitou conexao')
    while True:
        msg = con.recv(4096)
        if not msg:
            print("Nao chegou bytes")
            break
        A = True
        arquivo.write(msg) # Adicionando os bytes no arquivo criado
        print ("Recebendo dados no arquivo...")
    print ('Finalizando conexao do cliente')
    arquivo.close()
    con.close()
    break
print("Cliente desconectado")

if A==True: #Se alguma musica foi enviada
    print("Tocando musica do cliente...")
    playsound('musicaCliente.mp3')
    print("Tocando musica do servidor agora...")
    playsound('passinho.mp3')
    playsound('gaiola.mp3')
    playsound('surtada.mp3')
else: #Se nenhuma musica foi enviada
    print("Cliente não enviou musica...")
    print("Tocando musica do servidor")
    playsound('passinho.mp3')
    playsound('gaiola.mp3')
    playsound('surtada.mp3')

print("Acabaram as musicas")
