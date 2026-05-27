from arquivos import selecionar_pasta, montar_arquivos, exportar_excel
from extrator import extrair_dados, ler_pdf, capturar_numero, capturar_tipo, capturar_cfop

local = selecionar_pasta()
contratos = montar_arquivos(local)
resultado = extrair_dados(contratos)

exportar_excel(resultado)

# for contrato in contratos:
#     resultado = ler_pdf(contrato)
#     resultado2 = capturar_numero(resultado)
#     resultado3 = capturar_tipo(resultado)
#     resultado4 = capturar_cfop(resultado)

#     print(resultado2)
#     print(resultado3)
#     print(resultado4)
