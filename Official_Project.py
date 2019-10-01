arquivoentra = open("usuarios.txt", "r")

linhas = arquivoentra.readlines()
total = 0
totdisp = 1023
relat = open("Relatório.txt", "w")
nmr = 1
relat.write("ACME Inc.                         Uso do espaço em disco pelos usuários\n")
relat.write("-----------------------------------------------------------------------\n")
relat.write("Nr\t Usuário\t Espaço Utilizado\t % do uso\n")
for linha in linhas:
    nome = linha.split()[0]
    tam = float((linha.split()[1]))/1024/1024
    total = total + float(tam)
    percent = totdisp/float(tam)

    relat.write(" {}\t {}\t {:.2f}MB\t\t\t {:.2f}%\n".format(nmr, nome, tam, percent))
    nmr = nmr + 1



