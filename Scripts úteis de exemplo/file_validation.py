# Este código é um exemplo de como podemos evitar que atacantes insiram tipos de arquivo não autorizados por meio de Null Byte

# A biblioteca 'os' é importada. Ela fornece uma maneira de usar funcionalidades dependentes do sistema operacional, como ler ou escrever em arquivos.

import os

# Aqui é definida uma função chamada 'validate_image'. Ela recebe um argumento: 'filename', que é o nome do arquivo de imagem que você deseja validar.

def validate_image(filename):
    # 'magic_numbers' é um dicionário que mapeia extensões de arquivo de imagem para seus respectivos números mágicos.
    # Números mágicos são valores que identificam unicamente um tipo de arquivo. Eles são os primeiros bytes de um arquivo.

    magic_numbers = {
        '.png' : bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x1A, 0x0A]),
        '.jpg' : bytes([0xFF, 0xD8, 0xFF, 0xE0]),
        '.jpeg' : bytes([0xFF, 0xD8, 0xFF, 0xE0])
    }

    # Aqui, a função 'splitext' da biblioteca 'os' é usada para obter a extensão do arquivo de imagem.
    extension = os.path.splitext(filename)[1]

    # A extensão do arquivo é impressa.
    print(f'extension: {extension}')

    # O arquivo de imagem é aberto no modo de leitura binária ('rb').
    with open(filename, 'rb') as f:
        # A assinatura (números mágicos) para a extensão do arquivo é obtida do dicionário 'magic_numbers'.
        signature = magic_numbers[extension]

        # O número de bytes a serem lidos é definido como o comprimento da assinatura.
        bytes_to_read = len(signature)

        # Os primeiros 'bytes_to_read' bytes do arquivo são lidos.
        file_head = f.read(bytes_to_read)

        # Se a cabeça do arquivo corresponder à assinatura, então é um tipo de arquivo válido e 'Valid file type' é impresso.
        if file_head == signature:
            print('Valid file type')
        # Se a cabeça do arquivo não corresponder à assinatura, então é um tipo de arquivo inválido e 'Invalid file type' é impresso.
        else:
            print('Invalid file type')

# A função 'validate_image' é chamada com 'myimage.jpeg' como argumento.
validate_image('myimage.jpeg')
