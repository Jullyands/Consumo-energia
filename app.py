# Programa de cálculo de consumo de energia
# Autor: Anna Jullya

# Informações

Aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho em watts(W): "))
horasDia = float(input("Tempo médio de uso diário (em horas): "))

# Cálculo

consumoMensal = ((potencia)*(horasDia)*30)/1000

custo = (float(consumoMensal)*0.75)
resultado = print( "O consumo mensal de seu aparelho", (Aparelho), "foi de: ", (consumoMensal), "Khw/mês, com um custo estimado de R$", round(custo, 2) )
                  

