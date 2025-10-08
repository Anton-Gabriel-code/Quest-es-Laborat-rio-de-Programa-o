def adicionar_gostos(pessoas: list, gostos: list) -> list:
    gostos_dict = {item["id"]: item["gostos"] for item in gostos}
    pessoas_gostos = []
    for pessoa in pessoas:
        pessoa_gosto = pessoa.copy()
        pessoa_gosto["gostos"] = gostos_dict.get(pessoa["id"], [])
        pessoas_gostos.append(pessoa_gosto)

    return pessoas_gostos[:5]

def criar_pessoa(nome: str, idade: int, id: int) -> dict:
    return {"id": id, "nome": nome, "idade": idade}


pessoas = [
    criar_pessoa("Marcos", 28, 1),
    criar_pessoa("Ana", 24, 2),
    criar_pessoa("Carlos", 30, 3),
    criar_pessoa("Julia", 22, 4),
    criar_pessoa("Pedro", 27, 5),
    criar_pessoa("Laura", 26, 6)
]

gostos = [
    {"id": 1, "gostos": ["Música", "Futebol"]},
    {"id": 2, "gostos": ["Leitura", "Cinema"]},
    {"id": 3, "gostos": ["Viagem"]},
    {"id": 4, "gostos": ["Dança", "Esportes"]},
    {"id": 5, "gostos": ["Tecnologia", "Culinária"]},
    {"id": 6, "gostos": ["Moda"]}
]

resultado = adicionar_gostos(pessoas, gostos)
print(resultado)
