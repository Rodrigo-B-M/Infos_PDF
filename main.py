from arquivos import selecionar_pasta, montar_arquivos, exportar_excel, definir_documento
from extrator import extrair_dados

documento = definir_documento()
local = selecionar_pasta()
arquivos = montar_arquivos(local, documento)
resultado = extrair_dados(arquivos, documento)

exportar_excel(resultado)
