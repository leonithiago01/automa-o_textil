# =========================
# ENTRADAS
# =========================

artigo = input("Digite o artigo: ")

rolos_produzidos = int(input("Digite quantos rolos foram produzidos: "))

meta_rolos = int(input("Digite a meta em rolos: "))


# =========================
# BUSCAR DADOS DO ARTIGO
# =========================

metros_por_rolo = float(input("digite a metragem do rolo: "))


# =========================
# CÁLCULOS
# =========================

metragem_total = rolos_produzidos * metros_por_rolo

meta_metros = meta_rolos * metros_por_rolo

faltante_rolos = meta_rolos - rolos_produzidos

faltante_metros = meta_metros - metragem_total

porcentagem = (metragem_total / meta_metros) * 100


# =========================
# SAÍDA
# =========================

print()
print("===== PRODUÇÃO =====")

print("Artigo:", artigo)

print()

print("Produção Atual:")
print(rolos_produzidos, "rolos")
print(metragem_total, "metros")

print()

print("Meta:")
print(meta_rolos, "rolos")
print(meta_metros, "metros")

print()

print("Faltam:")
print(faltante_rolos, "rolos")
print(faltante_metros, "metros")

print()

print(f"Produção concluída: {porcentagem:.2f}%")


# =========================
# STATUS
# =========================

print()

if rolos_produzidos >= meta_rolos:

    print("STATUS: META ATINGIDA")

else:

    print("STATUS: PRODUÇÃO EM ANDAMENTO")