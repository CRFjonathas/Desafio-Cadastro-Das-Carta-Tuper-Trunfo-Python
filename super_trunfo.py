print(">>> JOGO SUPER TRUNFO <<<")

print("\nCADASTRO DE CARTAS:\n")

estado = str(input("Estado (A a H): ")).strip().upper()
cidade = int(input("Código da carta (1 - 4): "))
populaçao = int(input("População: "))
pib = int(input("PIB: R$"))
pontos_turisticos = int(input("Pontos Turisticos: "))

print("\nDADOS DA CARTA\n")
print(f"CÓDIGO DA CARTA: {estado}0{cidade}")
print(f"POPULAÇÃO: {populaçao}")
print(f"PIB: R${pib:,.2f}")
print(f"PONTOS TURISTICOS: {pontos_turisticos}")