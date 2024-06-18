#exercicio 1
cores=("vermelho", "verde","azul")
#exercicio 2
print (cores)
selec= int(input("selecione uma posiçao:"))
elemento = cores[selec]
print(elemento)
#exercicio 3
perg = str(input("coloque a cor:"))
if perg == "verde" and "vermelho" and "azul":
    print("o {} está na lista".format(perg))
#exercicio 4
for i in range (len (cores)):
    if cores [i]== perg:
        print(i)
#exercicio 5
cont = cores.count("azul")
print ("azul aparece ",cont)
#exercicio 6
contt= cores.count(elemento)
print("a tupla tem",contt)
#exercicio 7
lista = [1, 2, 3]
tupla_convertida = tuple(lista)
lista_convertida = list(tupla_convertida)
#exercicio 8
sigcor = ("amarelo")
#exercicio 9
tupla1 = (1, 2)
tupla2 = (3, 4)
tupla_combinada = tupla1 + tupla2
print("Tupla combinada:", tupla_combinada)
#exercicio 10
coordenadas = (10, 20)
x, y = coordenadas
print("Valor de x:", x)
print("Valor de y:", y)
 
