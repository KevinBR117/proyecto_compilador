from pathlib import Path
import pprint

matriz_estado = [
    [1, 2, 204, 3, 4, 209, 210, 211, 212, 5, 7, 215, 9, 303, 303, 303, 303, 16, 18, 20, 32, 24, 0, 22, 30, 31, 303, 303, 0],
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
    [302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 302, 218, 302, 302, 302, 302, 302, 302, 13, 13, 13, 302, 302, 302, 302, 302, 302],
    [308, 308, 308, 308, 308, 308, 308, 308, 308, 308, 308, 308, 308, 308, 308, 308, 33, 308, 308, 308, 13, 13, 13, 308, 308, 308, 308, 308, 308],
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
    [230, 230, 230, 230, 230, 230, 230, 230, 230, 230, 230, 230, 230, 230, 230, 230, 230, 230, 230, 230, 230, 24, 230, 230, 230, 230, 25, 27, 230],
    [306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 26, 306, 306, 306, 306, 306, 306, 306],
    [231, 231, 231, 231, 231, 231, 231, 231, 231, 231, 231, 231, 231, 231, 231, 231, 231, 231, 231, 231, 231, 26, 231, 231, 231, 231, 231, 27, 231],
    [306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 28, 28, 306, 306, 306, 306, 306, 29, 306, 306, 306, 306, 306, 306, 28],
    [306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 306, 29, 306, 306, 306, 306, 306, 306, 306],
    [232, 232, 232, 232, 232, 232, 232, 232, 232, 232, 232, 232, 232, 232, 232, 232, 232, 232, 232, 232, 232, 29, 232, 232, 232, 232, 232, 232, 232],
    [307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 30, 30, 30, 307, 233, 307, 307, 307, 307],
    [307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 31, 31, 31, 307, 307, 234, 307, 307, 307],
    [235, 235, 235, 235, 235, 235, 235, 235, 235, 235, 235, 235, 235, 235, 235, 235, 235, 235, 235, 235, 32, 235, 235, 235, 235, 235, 235, 235, 235],
    [308, 308, 308, 308, 308, 308, 308, 308, 308, 308, 308, 308, 219, 308, 308, 308, 33, 308, 308, 308, 13, 13, 13, 308, 308, 308, 308, 308, 219]
]

lista_simbolos = ['{','}',':','(',')',';',',','[',']','|','&','~','/','\\','+','-','*','<','>','=','letra','dígito','espacio','@',"'",'"','.','E','eof']

palabras_reservadas = ['int', 'string', 'real', 'logical', 'list', 'funcion', 'principal', 'regresar', 'mientras', 'hacer', 'ciclo', 'repeat', 'si',
                        'para', 'dentro', 'imprimir', 'longitud', 'entero', 'decimal', 'entrada', 'asbsoluto', 'cadena', 'potencia', 'redondear', 'sumar',
                        'minimo', 'maximo', 'elseif', 'else', 'rango'
                    ]
                    
estados_finales = {
    '200': ['{{', 'símbolo'],
    '201': ['{', 'símbolo'],
    '202': ['}}', 'símbolo'],
    '203': ['}', 'símbolo'],
    '204': [':', 'símbolo'],
    '205': ['((', 'símbolo'],
    '206': [')', 'símbolo'],
    '207': ['))', 'símbolo'],
    '208': [')', 'símbolo'],
    '209': [';', 'símbolo'],
    '210': [',', 'símbolo'],
    '211': ['[', 'símbolo'],
    '212': [']', 'símbolo'],
    '213': ['|||', 'símbolo'],
    '214': ['&&&', 'símbolo'],
    '215': ['~', 'simbolo'],
    '216': ['/+\ ', 'símbolo'],
    '217': ['/-\ ', 'símbolo'],
    '218': ['/*\ ', 'símbolo'],
    '219': 'comentario',
    '220': ['/\ ', 'símbolo'],
    '221': 'comentario',
    '222': ['<*<', 'símbolo'],
    '223': ['<*=', 'símbolo'],
    '224': ['>*>', 'símbolo'],
    '225': ['>*=', 'símbolo'],
    '226': ['==', 'símbolo'],
    '227': ['=*=', 'símbolo'],
    '228': ['=', 'símbolo'],
    '229': 'identificador',
    '230': 'número entero',
    '231': 'número decimal',
    '232': 'número entero con notación científica',
    '233': 'texto',
    '234': 'texto',
    '235': 'palabra reservada'
}

estados_error = {
    '300': 'error en operador lógico',
    '301': 'error en operador lógico',
    '302': 'error en operador aritmético',
    '303': 'error caracter inválido',
    '304': 'error en operador relacional',
    '305': 'error en identificador',
    '306': 'error en números',
    '307': 'error en textos',
    '308': 'error en comentario'
}

def obtener_columna(caracter):
    try:
        columna = lista_simbolos.index(caracter)
        return columna
    except ValueError:
        if(caracter.isalpha() == True):
            return 20
        elif(caracter.isdigit() == True):
            return 21
        elif(caracter.isspace() == True):
            return 22
        else:
            print('el caracter no existe en la lista')

tokens = {}
identificadores = []
constantes = []
lista_tokens = []

def guardar_token(token, tipo):
    tokens.setdefault(token.strip(), tipo)
    lista_tokens.append(token.strip())

def guardar_identificador(identificador):
    if (identificador in identificadores):
        pass
    else:
        identificadores.append(identificador.strip())

def guardar_constante(constante):
    if (constante in constantes):
        pass
    else:
        constantes.append(constante.strip())


def main():
    estado = 0
    columna = 0
    token = ''
    apuntador = 0
    eof= False

    texto = Path("../proyecto_compilador/archivo_fuente.txt").read_text().replace('\n', ' ')
    print(f'archivo fuente: {texto}\n')
    # print(len(texto))
    # iterar texto e identificar tokens   
    while (apuntador < (len(texto))):
        # print(f'apuntador: {apuntador}')
        caracter = texto[apuntador]
        token += caracter
        columna = obtener_columna(caracter)
        # si es eof
        if(apuntador == len(texto)-1):
            # print('apuntador', apuntador)
            # print('len(texto)', len(texto))
            # print('caracter', caracter)
            # print('token', token)
            columna = obtener_columna('eof')
            eof = True
        estado = matriz_estado[estado][columna]
        # print('estado: ', estado)
        apuntador += 1

        if (estado >= 200 and estado < 300):
            tipo = estados_finales[str(estado)]
            if(estado == 200):
                print(f'estado: {estado} token: {token} tipo: {tipo[1]}')
                guardar_token(token, tipo[1])
            elif(estado == 201):
                if(eof == False):
                    token = token[:-1]
                    apuntador -= 1
                print(f'estado: {estado} token: {token} tipo: {tipo[1]}')
                guardar_token(token, tipo[1])
            elif(estado == 202):
                print(f'estado: {estado} token: {token} tipo: {tipo[1]}')
                guardar_token(token, tipo[1])
            elif(estado == 203):
                if(eof == False):
                    token = token[:-1]
                    apuntador -= 1
                print(f'estado: {estado} token: {token} tipo: {tipo[1]}')
                guardar_token(token, tipo[1])
            elif(estado == 204):
                print(f'estado: {estado} token: {token} tipo: {tipo[1]}')
                guardar_token(token, tipo[1])
            elif(estado == 205):
                print(f'estado: {estado} token: {token} tipo: {tipo[1]}')
                guardar_token(token, tipo[1])
            elif(estado == 206):
                if(eof == False):
                    token = token[:-1]
                    apuntador -= 1
                print(f'estado: {estado} token: {token} tipo: {tipo[1]}')
                guardar_token(token, tipo[1])
            elif(estado == 207):
                print(f'estado: {estado} token: {token} tipo: {tipo[1]}')
                guardar_token(token, tipo[1])
            elif(estado == 208):
                if(eof == False):
                    token = token[:-1]
                    apuntador -= 1
                print(f'estado: {estado} token: {token} tipo: {tipo[1]}')
                guardar_token(token, tipo[1])
            elif(estado == 209):
                print(f'estado: {estado} token: {token} tipo: {tipo[1]}')
                guardar_token(token, tipo[1])
            elif(estado == 210):
                print(f'estado: {estado} token: {token} tipo: {tipo[1]}')
                guardar_token(token, tipo[1])
            elif(estado == 211):
                print(f'estado: {estado} token: {token} tipo: {tipo[1]}')
                guardar_token(token, tipo[1])
            elif(estado == 212):
                print(f'estado: {estado} token: {token} tipo: {tipo[1]}')
                guardar_token(token, tipo[1])
            elif(estado == 213):
                print(f'estado: {estado} token: {token} tipo: {tipo[1]}')
                guardar_token(token, tipo[1])
            elif(estado == 214):
                print(f'estado: {estado} token: {token} tipo: {tipo[1]}')
                guardar_token(token, tipo[1])
            elif(estado == 215):
                print(f'estado: {estado} token: {token} tipo: {tipo[1]}')
                guardar_token(token, tipo[1])
            elif(estado == 216):
                print(f'estado: {estado} token: {token} tipo: {tipo[1]}')
                guardar_token(token, tipo[1])
            elif(estado == 217):
                print(f'estado: {estado} token: {token} tipo: {tipo[1]}')
                guardar_token(token, tipo[1])
            elif(estado == 218):
                print(f'estado: {estado} token: {token} tipo: {tipo[1]}')
                guardar_token(token, tipo[1])
            elif(estado == 219):
                print(f'estado: {estado} token: {token} tipo: {tipo}')
            elif(estado == 220):
                print(f'estado: {estado} token: {token} tipo: {tipo[1]}')
                guardar_token(token, tipo[1])
            elif(estado == 221):
                if(eof == False):
                    token = token[:-1]
                    apuntador -= 1
                print(f'estado: {estado} token: {token} tipo: {tipo}')
            elif(estado == 222):
                print(f'estado: {estado} token: {token} tipo: {tipo[1]}')
                guardar_token(token, tipo[1])
            elif(estado == 223):
                print(f'estado: {estado} token: {token} tipo: {tipo[1]}')
                guardar_token(token, tipo[1])
            elif(estado == 224):
                print(f'estado: {estado} token: {token} tipo: {tipo[1]}')
                guardar_token(token, tipo[1])
            elif(estado == 225):
                print(f'estado: {estado} token: {token} tipo: {tipo[1]}')
                guardar_token(token, tipo[1])
            elif(estado == 226):
                print(f'estado: {estado} token: {token} tipo: {tipo[1]}')
                guardar_token(token, tipo[1])
            elif(estado == 227):
                print(f'estado: {estado} token: {token} tipo: {tipo[1]}')
                guardar_token(token, tipo[1])
            elif(estado == 228):
                if(eof == False):
                    token = token[:-1]
                    apuntador -= 1
                print(f'estado: {estado} token: {token} tipo: {tipo[1]}')
                guardar_token(token, tipo[1])
            elif(estado == 229):
                if(eof == False):
                    token = token[:-1]
                    apuntador -= 1
                print(f'estado: {estado} token: {token} tipo: {tipo}')
                guardar_token(token, tipo)
                guardar_identificador(token)
            elif(estado == 230):
                if(eof == False):
                    token = token[:-1]
                    apuntador -= 1
                print(f'estado: {estado} token: {token} tipo: {tipo}')
                guardar_token(token, tipo)
                guardar_constante(token)
            elif(estado == 231):
                if(eof == False):
                    token = token[:-1]
                    apuntador -= 1
                print(f'estado: {estado} token: {token} tipo: {tipo}')
                guardar_token(token, tipo)
                guardar_constante(token)
            elif(estado == 232):
                if(eof == False):
                    token = token[:-1]
                    apuntador -= 1
                print(f'estado: {estado} token: {token} tipo: {tipo}')
                guardar_token(token, tipo)
                guardar_constante(token)
            elif(estado == 233):
                print(f'estado: {estado} token: {token} tipo: {tipo}')
                guardar_token(token, tipo)
                guardar_constante(token)
            elif(estado == 234):
                print(f'estado: {estado} token: {token} tipo: {tipo}')
                guardar_token(token, tipo)
                guardar_constante(token)
            elif(estado == 235):
                if(eof == False):
                    token = token[:-1]
                    apuntador -= 1
                if(token.strip() in palabras_reservadas):
                    print(f'estado: {estado} token: {token} tipo: {tipo}')
                    guardar_token(token, tipo)
                else:
                    print(f'estado: 308 token: {token} no es palabra reservada')
                            
            estado = 0
            token = ''            
        
        elif(estado >= 300):
            tipo = estados_error[str(estado)]
            if(estado == 300):
                print(f'Error estado: {estado} token: {token} tipo: {tipo}')
            elif(estado == 301):
                print(f'Error estado: {estado} token: {token} tipo: {tipo}')
            elif(estado == 302):
                print(f'Error estado: {estado} token: {token} tipo: {tipo}')
            elif(estado == 303):
                print(f'Error estado: {estado} token: {token} tipo: {tipo}')
            elif(estado == 304):
                print(f'Error estado: {estado} token: {token} tipo: {tipo}')
            elif(estado == 305):
                print(f'Error estado: {estado} token: {token} tipo: {tipo}')
            elif(estado == 306):
                print(f'Error estado: {estado} token: {token} tipo: {tipo}')
            elif(estado == 307):
                print(f'Error estado: {estado} token: {token} tipo: {tipo}')

            estado = 0
            token = ''
            
                                                          
if __name__ == '__main__':
    main()
    print('tokens: ')
    pprint.pprint(tokens)
    print(f'identificadores: {identificadores}')
    print(f'constantes: {constantes}')
    print(f'lista de tokens: {lista_tokens}')