from tkinter import filedialog
import os
import pandas as pd

def selecionar_pasta():
    """
    Abre uma janela para o usuario selecionar uma pasta
    """
    local = filedialog.askdirectory()
    return local

def montar_arquivos(local):
    """
    Recebe o caminho de uma pasta, percorre todos os arquivos existentes e adiciona em uma lista os endereços dos arquivos que contenham
    a palavra "Confirmação" no nome. Retorna uma lista com os caminhos completos dos arquivos encontrados.
    """
    lista_contratos = []
    for arquivo in os.listdir(local):
        endereco = os.path.join(local, arquivo)
        endereco = os.path.normpath(endereco)
        if "confirmação".lower() in arquivo.lower():
            lista_contratos.append(endereco)
    return lista_contratos

def exportar_excel(dados):
    """
    Recebe uma lista de dicionários contendo os dados dos contratos.
    Converte os dados em um DataFrame, solicita ao usuário o local onde o arquivo será salvo e exporta o resultado em formato XLSX.
    """
    df = pd.DataFrame(dados)
    local_salvar = selecionar_pasta()
    caminho = str(local_salvar) + "/Resultado.xlsx"
    df.to_excel(caminho, index=False)
    
