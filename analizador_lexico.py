# leer archivo fuente
archivo = open('../proyecto_compilador/archivo_fuente.txt', 'r')

matriz_estado = [
    [1, 2, 204, 3, 4, 209, 210, 211, 212, 5, 7, 215, 9, 303, 303, 303, 303, 16, 18, 20, 32, 24, 0, 22, 30, 31, 303, 32, 0],
    [200, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201],
    [203, 202, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203],
    [206, 206, 206, 205, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206],
    [208, 208, 208, 208, 207, 208, 208, 208, 208, 208, 208, 208, 208, 208, 208, 208, 208, 208, 208, 208, 208, 208, 208, 208, 208, 208, 208, 208, 208],
    [300, 300, 300, 300, 300, 300, 300, 300, 300, 6, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300],
    [300, 300, 300, 300, 300, 300, 300, 300, 300, 213, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300],
    [301, 301, 301, 301, 301, 301, 301, 301, 301, 301, 8, 301, 301, 301, 301, 301, 301, 301, 301, 301, 301, 301, 301, 301, 301, 301, 301, 301, 301],
    [301, 301, 301, 301, 301, 301, 301, 301, 301, 301, 214, 301, 301, 301, 301, 301, 301, 301, 301, 301, 301, 301, 301, 301, 301, 301, 301, 301, 301],
    [302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 14, 220, 10, 11, 12, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302],
    [302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 216, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302],
    [302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 217, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302],
    [302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 218, 302, 302, 13, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302],
    [302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 219, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302],
    [302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 15, 302, 302, 302, 302, 302, 302, 302, 302],
    [221, 221, 221, 221, 221, 221, 221, 221, 221, 221, 221, 221, 221, 221, 221, 221, 221, 221, 221, 221, 15, 15, 15, 221, 221, 221, 221, 221, 221],
    [304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 17, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304],
    [304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 222, 304, 223, 304, 304, 304, 304, 304, 304, 304, 304, 304],
    [304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 19, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304],
    [304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 224, 225, 304, 304, 304, 304, 304, 304, 304, 304, 304],
    [228, 228, 228, 228, 228, 228, 228, 228, 228, 228, 228, 228, 228, 228, 228, 228, 21, 228, 228, 226, 228, 228, 228, 228, 228, 228, 228, 228, 228],
    [304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 304, 227, 304, 304, 304, 304, 304, 304, 304, 304, 304],
    [305, 305, 305, 305, 305, 305, 305, 305, 305, 305, 305, 305, 305, 305, 305, 305, 305, 305, 305, 305, 23, 305, 305, 305, 305, 305, 305, 305, 305],
    [229, 229, 229, 229, 229, 229, 229, 229, 229, 229, 229, 229, 229, 229, 229, 229, 229, 229, 229, 229, 23, 23, 229, 229, 229, 229, 229, 229, 229],
    [230, 230, 230, 230, 230, 230, 230, 230, 230, 230, 230, 230, 230, 230, 230, 230, 230, 230, 230, 230, 230, 24, 230, 230, 230, 230, 25, 27, 27],
    [306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 26, 306, 306, 306, 306, 306, 306, 306],
    [231, 231, 231, 231, 231, 231, 231, 231, 231, 231, 231, 231, 231, 231, 231, 231, 231, 231, 231, 231, 231, 26, 231, 231, 231, 231, 231, 27, 27],
    [306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 28, 28, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 28],
    [306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 29, 306, 306, 306, 306, 306, 306, 306],
    [232, 232, 232, 232, 232, 232, 232, 232, 232, 232, 232, 232, 232, 232, 232, 232, 232, 232, 232, 232, 232, 29, 232, 232, 232, 232, 232, 232, 232],
    [307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 30, 30, 30, 307, 233, 307, 307, 307, 307],
    [307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 31, 31, 31, 307, 307, 234, 307, 307, 307],
    [235, 235, 235, 235, 235, 235, 235, 235, 235, 235, 235, 235, 235, 235, 235, 235, 235, 235, 235, 235, 32, 235, 235, 235, 235, 235, 235, 235, 235]
]

lista_simbolos = ['{','}',':','(',')',';',',','[',']','|','&','~','/','\ ','+','-','*','<','>','=','letra','dígito','espacio','@',"'",'"','.','e','null']

palabras_reservadas = ['int', 'string', 'real', 'logical', 'list', 'funcion', 'principal', 'regresar', 'mientras', 'hacer', 'ciclo', 'repeat', 'si',
                        'para', 'dentro', 'imprimir', 'longitud', 'entero', 'decimal', 'entrada', 'asbsoluto', 'cadena', 'potencia', 'redondear', 'sumar',
                        'minimo', 'maximo', 'elseif', 'else', 'rango'
                    ]
                    
estados_finales = {
    '200': '{{',
    '201': '{',
    '202': '}}',
    '203': '}',
    '204': ':',
    '205': '((',
    '206': ')',
    '207': '))',
    '208': ')',
    '209': ';',
    '210': ',',
    '211': '[',
    '212': ']',
    '213': '|||',
    '214': '&&&',
    '215': '~',
    '216': '/+\ ',
    '217': '/-\ ',
    '218': '/*\ ',
    '219': 'comentario',
    '220': '/\ ',
    '221': 'comentario',
    '222': '<*<',
    '223': '<*=',
    '224': '>*>',
    '225': '>*=',
    '226': '==',
    '227': '=*=',
    '228': '=',
    '229': 'identificador',
    '230': 'número entero',
    '231': 'número decimal',
    '232': 'número enterio con notación científica',
    '233': 'texto',
    '234': 'texto',
    '235': 'palabra reservada'
}

# apuntador
estado = 0
columna = 0
apuntador = 0
token = ''

# def buscarEstadoFinal(estado, token_armado):
#     global estado
#     for estado_final in estados_finales:
#         # print(estado_final[0])
#         if(estado_final[0] == estado):
#             print(
#                 f'token: {token_armado} estado final: {estado_final[0]} reconoce: {estado_final[1]} ')
#             # se reinicia el apuntador estado a 0 y se limpia la variable de token armado
#             # print(f'aputadores estado{estado}, token_armado{token_armado}')
#             estado = 0
#             token_armado = ''
#             print(f'aputadores estado{estado}, token_armado{token_armado}')
#             return

#     print(f'error el token: {token_armado} no es válido estado: {estado}')
#     estado = 0
#     token_armado = ''

def obtener_columna(caracter):
    try:
        columna = lista_simbolos.index(caracter)
        return columna
    except ValueError:
        if(caracter.isalpha() == True):
            return 20
        elif(caracter.isdigit() == True):
            return 21
            # print('numero')
        elif(caracter.isspace() == True):
            return 22
        else:
            print('el caracter no existe en la lista')

def main():
    # leer linea de el archivo fuente
    for linea in archivo:
        # global estado
        # texto = linea.replace(' ', '')
        texto = linea
        print(texto)
        apuntador = 0
        # iterar texto e identificar tokens   
        for i in range(len(texto)):
            print('caracter',texto[i])
            apuntador += 1
            caracter = texto[i]
            token += caracter
            columna = obtener_columna(caracter)
            estado = buscarEstado(estado, columna)
            if (estado >= 200):
                pass
            else:
                pass

if __name__ == '__main__':
    main()