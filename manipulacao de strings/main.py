# url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
#
# if url.replace(" ","") == "":
#     raise ValueError(" URL Vazia")
#
# # Separa base e parâmetros
# indice_interrogacao = url.find('?')
# url_base = url[:indice_interrogacao]
# print("url_base: "+url_base)
# url_parametros = url[indice_interrogacao+1:]
# print("Parametros: "+url_parametros)
# num_parametros=url_parametros.count("&")+1
#
#
# indice=0
# paramentros_list=[]
# dicionario ={}
#
#
# for i in range(num_parametros):
#         if i<num_parametros-1:
#             paramentros_list.append(url_parametros[indice:url_parametros.find("&",indice)])
#         else:
#             paramentros_list.append(url_parametros[indice:])
#         indice=url_parametros.find("&",indice)+1 if url_parametros.find("&",indice)>0 else indice+1
#
#
# for i in paramentros_list:
#      dicionario[i[:i.find("=")]]=i[i.find("=")+1:]
#
#
# print(dicionario)


# Arquivo utilizado até a aula 3, quando então passamos a utilizar a classe
# ExtratorURL no arquivo extrator_url.py
url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"

# Sanitização da URL
url = url.strip()

# Validação da URL
if url == "":
    raise ValueError("A URL está vazia")

# Separa base e parâmetros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

# Busca o valor de um parâmetro
parametro_busca = 'quantidade'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print(valor)


