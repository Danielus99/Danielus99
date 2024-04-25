opc = 0
print("---XOR---")

while opc!="0":
    
    
    print("Para salir pulse 0.")
    ms = input("Introduzca el mensaje: ")
    clave = "XOR"

    #ENCRIPTAR
        
    mse = []
    mseAscii = []
    claveAscii = [ord(letra) for letra in clave]
    msAscii = [ord(letra) for letra in ms]
        
    while len(claveAscii) < len(msAscii): 
        claveAscii += claveAscii

    for i in range(len(msAscii)):
        mseAscii.append(chr(claveAscii[i] ^ msAscii[i]))
        
    print("El mensaje se ha traducido como: ", end="")
    for i in mseAscii:
        print(str(i), end="")
        
        
    print("")
    print("")
    





