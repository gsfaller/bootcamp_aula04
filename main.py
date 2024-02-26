import json

idade: int = 30
altura: float = 1.757
nome: str = "Alice"
is_estudante: bool = True

carrinho: list = []

product_1 = {
    'nome':'televisão',
    'quantidade':10,
    'preco':70.38,
    'disponibilidade':False
}


product_2 = {
    'nome':'microondas',
    'quantidade':15,
    'preco':75.38,
    'disponibilidade':False
}

carrinho.append(product_1)
carrinho.append(product_2)

carrinho_json = json.dumps(carrinho)

print(carrinho_json)


from typing import Dict, Any

livro_1: Dict[str, Any] = {
    'Titulo':'Game of Thrones',
    'Autor':'Estagiario',
    'Ano':2005
}

livro_2: Dict[str, Any] = {
    'Titulo':'Game of Thrones',
    'Autor':'Estagiario',
    'Ano':2005
}

lista_de_livros = []

lista_de_livros.append(livro_1)
lista_de_livros.append(livro_2)

print(lista_de_livros)

lista_de_livros_usando_dict:dict = {
    "livro_dict_1": {
        'Titulo':'Game of Thrones',
        'Autor':'Estagiario',
        'Ano':2005
    },
 "livro_dict_2": {
        'Titulo':'Game of Thrones',
        'Autor':'Estagiario',
        'Ano':2005
 }
}

print(lista_de_livros_usando_dict["livro_dict_1"]["Titulo"])

