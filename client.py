import socket

print ("Cliente")

HOST = str(input('Digite o endereço de IP: '))
PORT = 9876
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

opcaoMenu = 0
opcaoMusica = 0



print('''[1] Enviar Musica
[2] Tocar Musica''')
opcaoMenu = int(input('Qual sua opcao? '))
if opcaoMenu == 1:
    print('''[1] Mario
[2] Brega''')
    opcaoMusica = int(input('Qual sua opcao? '))
    if opcaoMusica == 1:
        bytes = open('mario.mp3', 'rb').read()
        s.send(bytes)
        s.close()
    elif opcaoMusica == 2:
        bytes = open('malemolencia.mp3', 'rb').read()
        s.send(bytes)
        s.close()
else:
    s.close()


