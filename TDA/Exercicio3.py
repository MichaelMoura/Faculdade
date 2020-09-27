anterior = 0
quantPositiva = 0
quantNegativa = 0
deseja = "s"

while(deseja =="s" or deseja =="sim" or deseja=="S"):
    valor = float(input("Digite algum valor: "))

    if(valor<0):
        print("O valor digitado é negativo")
        quantNegativa += 1
    elif(valor>0):
        print("O valor digitado é positivo")
        quantPositiva +=1
    else:
        print("O valor é neutro. Tente novamente")
        deseja = input("Você deseja continuar?(s/n)")

    print("Valores positivos digitados até agora: " , quantPositiva)
    print("Valoress negativos  digitados até agora: ",  quantNegativa)

    if(anterior>valor):
        print(f"{anterior} é maior que {valor}")
    elif(anterior<valor):
        print(f"{anterior} é menor que {valor}")
    elif(anterior==0):
      print("Não há valor anterior")  
    else:
        print(f"{anterior} é igual a {valor}")

    anterior = valor
    deseja = input("Você deseja continuar?(s/n)")
    
