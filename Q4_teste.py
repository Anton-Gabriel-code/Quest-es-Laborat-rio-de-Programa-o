def ordenar_lista(numeros_str: str) -> list[int]:
  if not numeros_str:
    return []
  else:
    numeros_str_lista = [num.strip() for num in numeros_str.split(',')]
    numeros_int_lista = [int(num) for num in numeros_str_lista]
    numeros_int_lista.sort()
    return numeros_int_lista

n1 = input("Insira os números para uma lista, separados por vírgula: ")

lista_ordenada = ordenar_lista(n1)


print("Lista ordenada:", lista_ordenada)
