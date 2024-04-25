
#Diccionario de base64 binario a letra
base64_dict = {"110000": "w", "110001": "x", "110101": "1", "110100": "0", "010100": "U", "010101": "V", "001100": "M", "001101": "N", "011110": "e", "011111": "f", "001001": "J", "001000": "I", "011011": "b", "011010": "a", "000110": "G", "000111": "H", "000011": "D", "000010": "C", "100100": "k", "100101": "l", "111100": "8", "111101": "9", "100010": "i", "100011": "j", "101110": "u", "101111": "v", "111001": "5", "111000": "4", "101011": "r", "101010": "q", "110011": "z", "110010": "y", "010010": "S", "010011": "T", "010111": "X", "010110": "W", "110110": "2", "110111": "3", "011000": "Y", "011001": "Z", "001111": "P", "001110": "O", "011101": "d", "011100": "c", "001010": "K", "001011": "L", "101101": "t", "000000": "A", "000001": "B", "100111": "n", "100110": "m", "000101": "F", "000100": "E", "111111": "/", "111110": "+", "100001": "h", "100000": "g", "010001": "R", "010000": "Q", "101100": "s", "111010": "6", "111011": "7", "101000": "o", "101001": "p"}

def encode(txt): #codificar

    by = ""
    #codigos ascii a string binario
    for c in txt:
        by += format(ord(c), '#010b')[2:]

    by = [by[i:i+6] for i in range(0, len(by), 6)] #parsear en array de 6 bits cada valor

    while len(by[-1]) != 6: #añadir 0s al final de último valor hasta que sea de tamaño 6
        by[-1] = by[-1] + '0'

    str = ""

    for i in by:
        str += base64_dict[i] #por cada valor de 6 bits, generamos la letra correspondiente a la biblioteca de base64

    str = [str[i:i+4] for i in range(0, len(str), 4)] #parsear en grupos de 4 letras

    while len(str[-1]) != 4: #Si el último grupo de letras no llega a 4, rellenar con '='
        str[-1] = str[-1] + '='
    
    txt = ""

    for i in str: #Imprimir caracteres en string
        txt += i

    return txt


def decode(txt): #decodificar
    
    by = ""

    for i in txt: 
        if i != '=': 
            by += list(base64_dict.keys())[list(base64_dict.values()).index(i)] #Utilizamos la libreria de base64 para convertir todo a string binario

    by = [by[i:i+8] for i in range(0, len(by), 8)] #parsear en grupos de 8 bits

    txt = ""

    for i in by:
        if int(i, 2) != 0:
            txt += chr(int(i, 2))   #transformamos los bytes en  caracteres

    return txt

n = '1'
while n != '3':
    n = input("1. Codificar\n2. Decodificar\n3. Salir\n")
    if(n == '1'):
        txt = input("Texto:\n")
        print(encode(txt))
    if(n == '2'):
        txt = input("Texto:\n")
        print(decode(txt))
