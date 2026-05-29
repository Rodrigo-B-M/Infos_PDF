from arquivos import selecionar_pasta, montar_arquivos, exportar_excel, definir_documento
from extrator import extrair_dados


documento = definir_documento()

print("Selecione o local dos arquivos:")

local = selecionar_pasta()
arquivos = montar_arquivos(local, documento)

resultado = extrair_dados(arquivos, documento)

print("Selecione o local para salvar os resultados:")

exportar_excel(resultado)

print("Encerrando.")


