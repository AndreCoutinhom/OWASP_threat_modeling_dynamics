# Esse script serve para estabelecer limites de tamanho de arquivo enviado ao sistema por usuários.
# É um exemplo muito bom para evitar DOS.

import urllib.request

url = "https://mysite.com/myimage.png"

tamanho_maximo = 5 * 1024 * 1024 # 5MB
url_remota = urllib.request.urlopen(url)
meta = url_remota.info()
tamanho_conhecido = int(meta['content-length'])

if tamanho_conhecido > tamanho_maximo:
    raise Exception("Arquivo muito grande.")

conteudo = url_remota.read(tamanho_maximo)
conteudo_excedente = url_remota.read(1)

if conteudo_excedente:
    raise Exception("Arquivo muito grande")
