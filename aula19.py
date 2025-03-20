nomes = ["ana", "Paula", "maria", "Sophia", "Fernanda", "Sophia"]

print(f"a primeira ocorrencia da sophia e no indice: {nomes.index("Sophia")}")

print(f"sophia aparece {nomes.count("sophia")} vezes na lista")

nomes.sort()
print(nomes)

nomes.reverse()
print(nomes)

copiaNomes = nomes.copy()
print(f"Nomes copiados: {copiaNomes}")