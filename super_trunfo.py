print(">>> JOGO SUPER TRUNFO <<<")

print("\nCADASTRO DE CARTAS:\n")

estado = str(input("Estado (A a H): ")).strip().upper()
cidade = int(input("Código da carta (1 - 4): "))
area = float(input("Área da cidade (Km²): "))
populacao = int(input("População: "))
pib = float(input("PIB: R$"))
pontos_turisticos = int(input("Pontos Turisticos: "))

densidade_populacional = populacao / area
pib_per_capita = pib / populacao

print("\nDADOS DA CARTA\n")
print(f"CÓDIGO DA CARTA: {estado}0{cidade}")
print(f"Área: {area}Km²")
print(f"POPULAÇÃO: {populacao}")
print(f"PIB: R${pib:,.2f} M")
print(f"PONTOS TURISTICOS: {pontos_turisticos}")
print(f"Densidade Populacional: {densidade_populacional:.2f} hab/Km²")
print(f"PIB per Capita: R${pib_per_capita:,.2f}")