# Este script tem a finalidade de estabelecer limites de tamanho para arquivos enviados ao sistema pelos usuários.
# É um exemplo útil para prevenir ataques de Negação de Serviço (DOS) por meio do envio de arquivos excessivamente grandes.

# Importa o módulo urllib.request, que fornece uma interface para trabalhar com URLs.
import urllib.request

# Define a URL do arquivo remoto que será verificado.
url = "https://mysite.com/myimage.png"

# Define o tamanho máximo permitido para o arquivo (5 MB neste caso).
tamanho_maximo = 5 * 1024 * 1024  # 5 MB

# Abre a URL remota.
url_remota = urllib.request.urlopen(url)

# Obtém informações sobre o arquivo remoto, como o tamanho.
meta = url_remota.info()

# Converte o tamanho conhecido do arquivo (obtido das informações) para um valor inteiro.
tamanho_conhecido = int(meta['content-length'])

# Verifica se o tamanho do arquivo conhecido é maior que o tamanho máximo permitido.
if tamanho_conhecido > tamanho_maximo:
    # Levanta uma exceção se o arquivo for muito grande.
    raise Exception("Arquivo muito grande.")

# Lê a quantidade máxima permitida de dados do arquivo remoto.
conteudo = url_remota.read(tamanho_maximo)

# Lê mais um byte do arquivo remoto para verificar se há conteúdo excedente.
conteudo_excedente = url_remota.read(1)

# Verifica se há conteúdo excedente após o limite máximo permitido.
if conteudo_excedente:
    # Levanta uma exceção se houver conteúdo excedente, indicando que o arquivo é muito grande.
    raise Exception("Arquivo muito grande")

