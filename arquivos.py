from tkinter import filedialog
import os
import pandas as pd

def definir_documento():
    while True:
        try:
            tipo = int(input("Qual o tipo de arquivo?\n1-Contratos\n2-Notas fiscais (mod.55)\n"))
            if tipo not in (1, 2):
                raise ValueError
            else:
                return tipo
        except ValueError:
            print("Entrada invalida!\n")  

def selecionar_pasta():
    """
    Abre uma janela para o usuario selecionar uma pasta
    """
    print("Selecione o local dos arquivos:")
    local = filedialog.askdirectory()
    return local

def montar_arquivos(local,tipo_documento):
    """
    Recebe o caminho de uma pasta, percorre todos os arquivos existentes e adiciona em uma lista os endereços dos arquivos, caso se trate 
    de contratos, icluira na lista somente os arquivos que contenham a palavra "Confirmação" no nome. 
    Retorna uma lista com os caminhos completos dos arquivos encontrados.
    """
    lista_arquivos = []
    for arquivo in os.listdir(local):
        print("Carregando arquivo.")
        endereco = os.path.normpath(os.path.join(local, arquivo))
        if tipo_documento == 1 and "confirmação".lower() in arquivo.lower():
            lista_arquivos.append(endereco)
        elif tipo_documento == 2:
            lista_arquivos.append(endereco)
    return lista_arquivos

def exportar_excel(dados):
    """
    Recebe uma lista de dicionários contendo os dados dos contratos.
    Converte os dados em um DataFrame, solicita ao usuário o local onde o arquivo será salvo e exporta o resultado em formato XLSX.
    """
    df = pd.DataFrame(dados)
    print("Selecione o local para salvar os resultados:")
    local_salvar = selecionar_pasta()
    caminho = str(local_salvar) + "/Resultado.xlsx"
    df.to_excel(caminho, index=False)
    print("Encerrando!")
    
