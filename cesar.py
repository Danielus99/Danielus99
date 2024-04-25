def cesar(txt,n):
    if n != 0:
        out = ""
        for c in txt:
            ant = ord(c)
            if 64 < ant < 91:
                act = ant+n
                if 64 < ant < 91:
                    if act >= 91:
                        act = 65 + ((act-91)%26)
                    elif act <= 64:
                        act = 90 - ((64-act)%26)
            else:
                act = ant
            out = out + chr(act)
    else:
        out = txt
    return out

def breaker():
    txt = input("Texto:\n")
    for i in range(-12,14):
        print("("+str(i)+") "+ cesar(txt,i))

print("---CODIFICADOR CESAR---")
while True:
    print()
    print("0: Salir")
    print("1: Desplazamiento manual")
    print("2: Desplazamiento bruto (perfecto para decodificar)")
    num = int(input("Opc:\n"))
    if num == 0: quit()
    elif num == 1:
        txt = input("Texto:\n")
        n = int(input("Desplz.:\n"))
        print(cesar(txt,n))
    elif num == 2: breaker()
    


