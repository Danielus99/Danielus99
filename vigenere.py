alph = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
mode = input("Cifrar (c) o descifrar (d):\n")
txt = input("Texto:\n")
psw = input("Contrasena:\n")
pswc = 0
out = ""
for i, c in enumerate(txt):
    select = alph.find(c) #Indice del caracter
    code = alph.find(psw[pswc]) #Indice del caracter en clave
    pswc = (pswc+1)%len(psw) #Incrementar posición en clave
    
    if(mode == 'c'): #cifrar
        out = out+alph[(code+select)%52]

    elif(mode == 'd'): #descifrar
        out = out+alph[(select-code)%52]
print(out)