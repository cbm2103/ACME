arquivo = open('usuarios.txt', 'w')

for i in range(1, 501):
    nome = ('usuario{}'.format(i))
    from random import randrange
    quantidade = str(randrange(524288000))
    arquivo.write(nome + " " + quantidade + "\n")

arquivo.close()