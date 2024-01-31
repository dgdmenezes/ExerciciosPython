from time import sleep

i =0

while 1 == 1:
    print("Verificando se há arquivos...")
    sleep(2)
    i += 1
    if i>10:
        break

contador =1 

while contador < 20:
    if contador%2 ==0:
        print(f"O numero {contador} é par")
    else:
        print(f"O numero {contador} é impar")
    
    contador+=1