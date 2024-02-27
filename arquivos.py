import csv

#Caminho para o arquivo CSV
caminho_do_arquivo: str = "arquivo.csv"

# Inicializa uma lista vazia para armazenar os dados
arquivo_csv: list = []

# Usa o gerenciador de contexto 'with' para abrir e fechar o arquivo
with open(file=caminho_do_arquivo, mode ='r', encoding='utf-8') as arquivo:

    #cria um objeto leitor de CSV
    leitor_csv = csv.DictReader(arquivo)

    for linha in leitor_csv:
        arquivo_csv.append(linha)

print(arquivo_csv)