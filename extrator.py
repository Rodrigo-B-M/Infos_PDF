import pdfplumber
import re

def extrair_dados(lista, tipo_documento):
    """
    Recebe uma lista com endereços de arquivos.
    Para cada arquivo, realiza a leitura do conteúdo e extrai
    informações específicas. Em seguida, monta um dicionário com 
    os dados extraídos e adiciona esse dicionário em uma nova lista.
    """
    resumo_arquivos = []
    for arquivo in lista:
        print(f"Lendo arquivo:{arquivo}")
        texto = ler_pdf(arquivo)
        if tipo_documento == 1:            
            resumo = {"numero": capturar_numero(texto, tipo_documento), "tipo": capturar_tipo(texto), "cfop": capturar_cfop(texto)}
            resumo_arquivos.append(resumo)
        elif tipo_documento == 2:
            resumo = {"numero": capturar_numero(texto, tipo_documento), "produto": capturar_produtos(texto)}
            resumo_arquivos.append(resumo)
    return resumo_arquivos

def ler_pdf(endereço):
    """
    Recebe o endereço de um arquivo PDF e, se o conteúdo for lido corretamente, extrai o texto para uma variável
    """
    texto_completo =""
    with pdfplumber.open(endereço) as pdf:
        for pagina in pdf.pages:
            texto = pagina.extract_text()
            if texto:
                texto_completo += texto + "\n"
    return texto_completo

def capturar_numero(texto, tipo_documento):
    """
    Recebe um texto e procura pelo numero do contrato com dois formatos pré-definidos, ou pelo numero da nota.
    """
    if tipo_documento == 1:
        padrao_1 = r"Nº do Contrato\s+(.+)"
        numero = re.search(padrao_1, texto)
        if numero:
            return numero.group(1)
        padrao_2 = r"CONFIRMAÇÃO DE NEGÓCIO - NÚMERO\s+(.+)"
        numero = re.search(padrao_2, texto)
        if numero:
            return numero.group(1)
    elif tipo_documento == 2:
        padrao_1 = r"Nº\s+(.+)"
        numero = re.search(padrao_1, texto)
        if numero:
            return numero.group(1)
        else:
            return "Fora do padrão!"
  
def capturar_tipo(texto):
    """
    Recebe um texto e procura o tipo do contrato, dois formatos pré-definidos.
    """
    padrao_tipo = r"2\.10\s+TIPO DO CONTRATO:\s+(.+)"
    tipo = re.search(padrao_tipo, texto)
    if tipo:
        return tipo.group(1)
    padrao_tipo2 = r"Tipo do Contrato:\s+(.+)"
    tipo = re.search(padrao_tipo2, texto)
    if tipo:
        return tipo.group(1)

def capturar_cfop(texto):
    """
    Recebe um texto e procura por um padrão pré-definido, caso não encontre retorna "Não disponível".
    """
    padrao_cfop = r"2\.11\s+CFOP:\s+(.+)"
    cfop = re.search(padrao_cfop, texto)
    if cfop:
        return cfop.group(1)
    else:
        return "Não disponível"

def capturar_produtos(texto):
    """
    Recebe um texto e procura pela descrição do produto, retorna todas as ocorrências que sigam o padrão pré-definido
    """
    padrao_produto = r"\d{4}-[A-Za-z]+(.+)"
    produto = re.search(padrao_produto, texto)
    if produto:
        return produto.group()
    else:
        return "Fora do padrão!"



