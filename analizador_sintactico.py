import analizador_lexico, pprint, sys
from analizador_lexico import tokens, lista_tokens

matriz_sintactica = [
    [1,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e'],
    [2,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e'],
    ['e',4,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e',3,3,3,3,3,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e'],
    ['e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e',5,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e'],
    ['e','e','e','e','e',7,6,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e'],
    ['e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e',8,9,10,11,12,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e'],
    ['e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e',13,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e',14],
    ['e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e',15,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e'],
    ['e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e',16,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e'],
    ['e','e','e',17,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e'],
    ['e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e',18,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e'],
    ['e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e',19,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e'],
    ['e','e','e','e','e',21,20,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e'],
    ['e','e','e','e','e','e','e',22,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e'],
    ['e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e',23,'e','e','e','e','e','e','e','e','e','e',23,23,'e',23,23,23,'e',23,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e'],
    ['e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e',24,'e','e','e','e','e','e','e','e','e','e',25,26,'e',27,28,29,'e',30,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e'],
    ['e','e','e','e','e','e','e','e','e','e','e',31,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e',32,32,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e',33,33,33,33,33,33,33,33,33,33,33,'e','e','e','e'],
    ['e','e','e','e','e','e','e','e','e','e','e','e',36,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e',35,36,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e'],
    ['e','e',38,'e','e','e','e','e','e','e','e','e',39,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e'],
    ['e','e','e','e','e','e','e','e','e','e','e','e',41,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e',40,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e'],
    ['e','e','e','e','e','e','e','e','e','e','e','e',43,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e',42,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e'],
    ['e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e',44,45,46,47,48,49,50,51,52,53,54,'e','e','e','e'],
    ['e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e',55,'e',56,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e'],
    ['e','e','e','e','e','e',57,'e','e','e',58,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e'],
    ['e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e',59,60,'e','e'],
    ['e','e','e','e','e',61,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e',62,'e','e'],
    ['e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e',63,'e'],
    ['e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e',64,64,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e'],
    ['e','e','e','e','e',66,'e','e','e','e',65,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e'],
    ['e','e','e','e','e',68,'e','e','e','e',67,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e'],
    ['e','e','e','e','e','e','e','e','e',69,'e','e','e','e','e',69,'e','e','e','e','e','e','e','e','e','e','e',69,69,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e'],
    ['e','e','e','e','e',71,'e',71,'e','e','e','e','e',70,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e'],
    ['e','e','e','e','e','e','e','e','e',72,'e','e','e','e','e',72,'e','e','e','e','e','e','e','e','e','e','e',72,72,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e'],
    ['e','e','e','e','e',74,'e',74,'e','e','e','e','e',74,73,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e'],
    ['e','e','e','e','e','e','e','e','e',76,'e','e','e','e','e',75,'e','e','e','e','e','e','e','e','e','e','e',77,77,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e'],
    ['e','e','e','e','e','e','e','e','e','e',79,'e','e','e',79,'e','e','e','e','e',78,78,78,78,78,'e',78,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e'],
    ['e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e',80,80,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e'],
    ['e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e',81,81,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e'],
    ['e','e','e','e','e',84,'e','e','e','e',84,'e','e','e',84,'e',82,83,'e','e',84,84,84,84,84,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e'],
    ['e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e',85,85,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e'],
    ['e','e','e','e','e',88,'e','e','e','e',88,'e','e','e',88,'e',88,88,86,87,88,88,88,88,88,'e',88,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e'],
    ['e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e',89,90,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e'],
    ['e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e',91,92,93,94,96,'e',95,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e']
]


simbolos_gramatica = ['{{','}}',':','((','))',';',',','{','}','(',')','[',']','|||','&&&','~','/+\\','/-\\','/*\\','/\\','<*<','>*>','<*=','>*=','=*=','=','==','identificador','numero','texto','int','string','real','logical','list','funcion','principal','regresar','mientras','hacer','ciclo','repeat','si','para',
                'dentro','imprimir','longitud','entero','decimal','entrada','absoluto','cadena','potencia','redondear','sumar','minimo','maximo','elseif','else','rango','eof']

no_terminales = ['PROGRAMA','DECLARACIONVARIABLES','VARIABLES','LISTAVARIABLES','LISTAVARIABLESPRIMA','TIPO','FUNCIONES','FUNCION','MAIN','PARAMETROS','RETURN','LISTARETURN','LISTARETURNPRIMA','BLOQUE','ESTATUTOS','ESTATUTO','LISTA','LISTAELEMENTOS','LISTAPRIMA','ELEMENTO_TEXTOSPRIMA','ELEMENTO_NUMEROSPRIMA',
'FUNCION_BUILT_IN','VARIABLESIMPRIMIR','VARIABLESPRIMA','ELSEIF','ELSE','RANGO','VALOR1','VALOR2','VALOR3','BOOLEXP','BOOLEXP_PRIMA','BOOLTERM','BOOLTERM_PRIMA','BOOLFACTOR','RELTERMP','RELTERM','EXPARITM','EXPPRIMA','TERMINO','TERMPRIMO','FACTOR','OPERADOR']

producciones = {
    1: 'DECLARACIONVARIABLES MAIN FUNCIONES',
    2: '{{ VARIABLES }}',
    3: 'TIPO : LISTAVARIABLES ; VARIABLES',
    4: 'nulo',
    5: 'identificador LISTAVARIABLESPRIMA',
    6: ', LISTAVARIABLES',
    7: 'nulo',
    8: 'int',
    9: 'string',
    10: 'real',
    11: 'logical',
    12: 'list',
    13: 'FUNCION FUNCIONES',
    14: 'nulo',
    15: 'funcion identificador PARAMETROS BLOQUE RETURN',
    16: 'principal BLOQUE',
    17: '(( VARIABLES ))',
    18: 'regresar LISTARETURN ;',
    19: 'identificador LISTARETURNPRIMA',
    20: ', LISTARETURN',
    21: 'nulo',
    22: '{ ESTATUTOS }',
    23: 'ESTATUTO ; ESTATUTOS',
    24: 'identificador = LISTA',
    25: 'mientras BOOLEXP BLOQUE',
    26: 'hacer BLOQUE ciclo BOOLEXP',
    27: 'repeat BLOQUE ciclo BOOLEXP',
    28: 'si BOOLEXP BLOQUE ELSEIF ELSE',
    29: 'para identificador dentro RANGO BLOQUE',
    30: 'imprimir ( VARIABLESIMPRIMIR )',
    31: '[ LISTAELEMENTOS ]',
    32: 'EXPARITM',
    33: 'FUNCION_BUILT_IN',
    34: 'identificador { LISTAPARAMETROS }',
    35: 'numero LISTAPRIMA',
    36: 'ELEMENTO_TEXTOSPRIMA',
    37: 'ELEMENTO_NUMEROSPRIMA',
    38: ': numero',
    39: 'nulo',
    40: 'texto ELEMENTO_TEXTOSPRIMA',
    41: 'nulo',
    42: 'texto ELEMENTO_NUMEROSPRIMA',
    43: 'nulo',
    44: 'longitud ( identificador )',
    45: 'entero ( identificador )',
    46: 'decimal ( identificador )',
    47: 'entrada ( )',
    48: 'absoluto ( EXPARITM )',
    49: 'cadena ( EXPARITM )',
    50: 'potencia ( EXPARITM )',
    51: 'redondear ( EXPARITM )',
    52: 'sumar ( identificador )',
    53: 'minimo ( identificador )',
    54: 'maximo ( identificador )',
    55: 'identificador VARIABLESPRIMA',
    56: 'texto VARIABLESPRIMA',
    57: ', VARIABLESIMPRIMIR',
    58: 'nulo',
    59: 'elseif BOOLEXP BLOQUE ELSEIF',
    60: 'nulo',
    61: 'nulo',
    62: 'else BLOQUE',
    63: 'rango ( VALOR1 )',
    64: 'EXPARITM VALOR2',
    65: 'nulo',
    66: '; EXPARITM VALOR3',
    67: 'nulo',
    68: '; EXPARTIM',
    69: 'BOOLTERM BOOLEXP_PRIMA',
    70: '||| BOOLTERM BOOLEXP_PRIMA',
    71: 'nulo',
    72: 'BOOLFACTOR BOOLTERM_PRIMA',
    73: '&&& BOOLFACTOR BOOLTERM_PRIMA',
    74: 'nulo',
    75: '~ BOOLFACTOR',
    76: '( RELTERM RELTERMP )',
    77: 'RELTERM RELTERMP',
    78: 'OPERADOR RELTERM',
    79: 'nulo',
    80: 'EXPARITM',
    81: 'TERMINO EXPPRIMA',
    82: '/+\ TERMINO EXPPRIMA',
    83: '/-\ TERMINO EXPPRIMA',
    84: 'nulo',
    85: 'FACTOR TERMPRIMO',
    86: '/*\ FACTOR TERMPRIMO',
    87: '/\ FACTOR TERMPRIMO',
    88: 'nulo',
    89: 'identificador',
    90: 'numero',
    91: '<*<',
    92: '>*>',
    93: '<*=',
    94: '>*=',
    95: '==',
    96: '=*=',
}

lista_inicial = ['eof','PROGRAMA']
# lista tokens esta imporada del modulo de analizador_lexico


def obtener_renglon(simbolo):
    try:
        renglon = no_terminales.index(simbolo)
        return renglon
    except ValueError:
        print(f'El simbolo no terminal no existe en la lista de no_terminales: {simbolo}')
        return -2


def obtener_columna(token):
    try:
        columna = simbolos_gramatica.index(token)
        return columna
    except ValueError:
        if(token.startswith('@') == True): #identificador
            return 27
        elif(token.isdigit() == True): #numero 
            return 28
        elif((token.startswith('"') == True) or (token.startswith("'"))): #texto
            return 29
        else:
            print(f'El token no existe en la lista de simbolos_gramatica: {token}')
            return -1


def main():
    renglon = 0 
    while(len(lista_tokens) != 0):
        print(f'lista_inicial: {lista_inicial}\n')
        print(f'lista_tokens: {lista_tokens}\n')
        token = lista_tokens[0]
        simbolo = lista_inicial[-1]

        print(f'token en revision: {token}')
        print(f'simbolo en revision: {simbolo}\n')

        if (token == simbolo):
            # if(token == ';'):
            #     print(token)
            # if(simbolo == ';'):
            #     print(simbolo)
            print('el token y el simbolo son iguales\n')

            print(f'lista_inicial: {lista_inicial}\n')
            print(f'lista_tokens: {lista_tokens}\n')    

            # eliminan de ambas listas el simbolo y el token
            # if ((simbolo == ';') and (token == ';')):
            #     print('eliminacion de token ;')
            #     lista_inicial.remove(';')
            #     lista_tokens.remove(';')
            # else:
            # lista_inicial.remove(simbolo)
            # lista_tokens.remove(token)

            del lista_inicial[-1]
            del lista_tokens[0]

            print(f'lista_inicial despues de eliminar: {lista_inicial}\n')
            print(f'lista_tokens despues de eliminar: {lista_tokens}\n')

        elif((token.startswith('@') == True) and (simbolo == 'identificador')):
            print('el token y el simbolo son iguales\n')
            print(f'lista_inicial: {lista_inicial}\n')
            print(f'lista_tokens: {lista_tokens}\n') 
            # lista_tokens.remove(token)
            # lista_inicial.remove(simbolo)
            del lista_inicial[-1]
            del lista_tokens[0]
            print(f'lista_inicial despues de eliminar: {lista_inicial}\n')
            print(f'lista_tokens despues de eliminar: {lista_tokens}\n')
        
        elif((token.isdigit() == True) and (simbolo == 'numero')):
            print('el token y el simbolo son iguales\n')
            print(f'lista_inicial: {lista_inicial}\n')
            print(f'lista_tokens: {lista_tokens}\n')
            # lista_tokens.remove(token)
            # lista_inicial.remove(simbolo)
            del lista_inicial[-1]
            del lista_tokens[0]
            print(f'lista_inicial despues de eliminar: {lista_inicial}\n')
            print(f'lista_tokens despues de eliminar: {lista_tokens}\n')
        
        elif((token.startswith('"') == True) or (token.startswith("'") == True)):
            if(simbolo == 'texto'):
                print('el token y el simbolo son iguales\n')
                print(f'lista_inicial: {lista_inicial}\n')
                print(f'lista_tokens: {lista_tokens}\n')
                # lista_tokens.remove(token)
                # lista_inicial.remove(simbolo)
                del lista_inicial[-1]
                del lista_tokens[0]
                print(f'lista_inicial despues de eliminar: {lista_inicial}\n')
                print(f'lista_tokens despues de eliminar: {lista_tokens}\n') 

        else:
            # se obtiene el indice de la lista de simbolos no terminales y de la lista de simbolos de la gramatica
            renglon = obtener_renglon(simbolo)
            columna = obtener_columna(token)
            # buscar en la matriz sintactica la produccion a sustituir
            numero_produccion = matriz_sintactica[renglon][columna]
            
            if (numero_produccion == 'e'):
                print('Error en la gramatica, se esperaba:\n')
                lista_esperaban = []
                for i in range(len(simbolos_gramatica)):
                    if (str(matriz_sintactica[renglon][i]).isdigit() == True):
                        lista_esperaban.append(simbolos_gramatica[i])
                print(lista_esperaban)
                sys.exit('Se finaliza la ejecucion')

            # obtener produccion y sustituir por simbolo no terminal
            produccion = producciones.get(numero_produccion).split(' ')
            produccion.reverse()
            # lista_inicial.remove(simbolo)
            del lista_inicial[-1]
            if(produccion[0] != 'nulo'):
                # print(produccion)
                lista_inicial.extend(produccion)
    print('analisis sintactico completado')


if __name__ == "__main__":
    analizador_lexico.main()
    print('tokens')
    pprint.pprint(tokens)
    lista_tokens.append('eof')
    print('\nlista de tokens: ', lista_tokens)
    main()