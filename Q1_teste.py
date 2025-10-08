def criar_pessoa(nome: str, idade: int, id: int):
  pessoa = {"id": id, "nome": nome, "idade": idade}
  return pessoa
p1 = criar_pessoa("Marcos", 28, 1)
p2 = criar_pessoa("Ana", 24, 2)
p3 = criar_pessoa("Carlos", 30, 3)
p4 = criar_pessoa("Antonio", 20, 4)

pessoas = [p1, p2, p3, p4]
print(p4)
