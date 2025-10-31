import csv

path_arquivo="desafio/vendas.csv"


def ler_csv(nome_do_arquivo_csv:str)-> list[dict]:
    """
    Função que lê um arquivo csv e retorna uma lista de dicionarios
    """

    lista=[]

    with open(nome_do_arquivo_csv, mode='r', encoding='utf-8') as arquivo:
        leitor= csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)

    return lista
 
#_____________________________________________________________________________________________________________________

def filtrar_produtos_nao_entregues(lista:list[dict])-> list[dict]:

    """
    Função que filtra os produtos não entregues
    """
    lista_com_produtos_filtrados=[]

    for produto in lista:
        if produto.get("entregue")=="True":
            lista_com_produtos_filtrados.append(produto)
    return lista_com_produtos_filtrados

#_____________________________________________________________________________________________________________________

def somar_valores_produtos_nao_entregues(lista_com_produtos_filtrados:list[dict])-> int:
    """
    Função que soma os valores dos produtos não entregues
    """
    valor_total=0
    for produto in lista_com_produtos_filtrados:
           valor_total += float(produto.get("price", 0))
    return valor_total

#_____________________________________________________________________________________________________________________

lista_de_produtos=ler_csv(path_arquivo)
produtos_entregues=filtrar_produtos_nao_entregues(lista_de_produtos)
valor_dos_produtos_entregues=somar_valores_produtos_nao_entregues(produtos_entregues)
print(valor_dos_produtos_entregues)
