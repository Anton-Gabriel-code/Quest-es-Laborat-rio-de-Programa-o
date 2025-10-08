import heapq

def top_tres_maiores(numeros: list[int]):
  return heapq.nlargest(3, numeros)

numeros = [5, 42, 12, 9, 73, 51, 22]
maiores = top_tres_maiores(numeros) 
print(maiores)
