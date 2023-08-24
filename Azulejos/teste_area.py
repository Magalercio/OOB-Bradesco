from area import Retangulo
import math
print(0**0)
teste = True
while teste:
    piso_a = float(input("Digite um lado do piso: "))
    piso_b = float(input("Digite o outro lado do piso: "))

    piso = Retangulo(piso_a, piso_b)

    az_a = float(input("Digite o lado do azulejo: "))
    az_b = float(input("Digite o outro lado do azulejo: "))

    azulejo = Retangulo(az_a, az_b)

    area_piso = piso.area()
    area_azulejo = azulejo.area()

    qntd_az = area_piso / area_azulejo

    if area_piso % area_azulejo ==0:
        print(f'A quantidade exate de azulejos para preencher o piso é de {qntd_az}')

    else:
        print (f'A quantidade mínima de azulejos para preencher o piso é de {math.ceil(qntd_az)}')

    finalizar = input("Deseja calcular novamente continuar? (Y,N)")
    if finalizar == "Y" or finalizar == "y":
        print("Reiniciando o programa")
        teste = True
    elif  finalizar == "N" or finalizar == "n":
        print("programa encerrado!!!")
        teste = False
    else:
        print("Resposta inválida, mas vamos reiniciar o programa mesmo assim!")



