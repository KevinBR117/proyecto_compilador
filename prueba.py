import sys
lista_inicial = ['eof','PROGRAMA' ,';']
lista_tokens = [';']
simbolo = lista_inicial[-1]
token = lista_tokens[0]
print(simbolo)
print(token)
print(lista_inicial)
print(lista_tokens)
lista_inicial.remove(simbolo)
lista_tokens.remove(token)
print(lista_inicial)
print(lista_tokens)
dicccionario = {
    1: 'DECLARACIONVARIABLES MAIN FUNCIONES ;',
    2: '{{ VARIABLES }}',
    3: 'TIPO : LISTAVARIABLES ; VARIABLES',
}
lista = dicccionario.get(1).split(' ')
print (lista)
caracter = ';'
lista.remove(caracter)
print(lista)
# lista.reverse()
# print(lista)
# print(lista_inicial)
# lista_inicial.remove('PROGRAMA')
# lista_inicial.extend(lista)
# print(lista_inicial)
# print(lista_inicial[-1])

# sys.exit('se finaliza la ejecucion')
# lista_vacia = []
# print(len(lista_vacia))

# numero = '45.5'
# if (numero.isdigit() == True):
#     print('digito')

# print(dicccionario.get(1))