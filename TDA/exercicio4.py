def media(media,contador):
    media = media / contador
    return  media

contadorM = 0
contadorF = 0
mediaM = 0
mediaF = 0
prosseguir = "s"

while(prosseguir=="s" or prosseguir=="sim" ):
    genero = input("Digite o seu sexo(m/f): ").lower()
    altura =float(input("Digite sua altura(em M): "))

    if(genero=="m" or genero=="masculino"):
        print("A altura masculina digitada é de: ", altura," m")
        contadorM = contadorM + 1
        mediaM = mediaM + altura

        print("Alturas masculinas digitadas até agora: ", contadorM)
        print("A media masculina é de: ", media(mediaM, contadorM ))

        print("Alturas femininas digitadas até agora: ", contadorF)
        print("A media feminina é de: ", mediaF)

    elif(genero=="f" or genero=="feminino"):
        print("A altura feminina digitada é de:" , altura," m")			
        contadorF = contadorF + 1			
        mediaF = mediaF + altura

        print("Alturas masculinas digitadas até agora: ", contadorM)
        print("A media masculina é de: ", mediaM)

        print("Alturas femininas digitadas até agora: ", contadorF)
        print("A media feminina é de: ", media(mediaF, contadorF))

    else:
        print("Sexo digitado inválido. tente novamente")

    prosseguir = input("Deseja prosseguir?(s/n): ").lower()
