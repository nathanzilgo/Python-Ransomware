#!/usr/bin/python3.6
#coding:utf-8
# utilizando criptografia de bloco assimétrica
# Função de mudança de arquivo.
def cryptAndDecryptFiles(filename, cryptoFn, blockSize=16):

    # Abre o arquivo 'filename' a ser criptografado no modo de leitura 'r+b' binário
    # Salva o arquivo aberto em _file
    with open(filename, 'r+b') as _file:
        # raw_value guarda uma leitura por blocos de 16 bits de _file.
        raw_value = _file.read(blockSize)

        # Aplica a função de criptografar a cada bloco
        # de raw_value, cifrando o arquivo.
        # Cada loop corresponde a um bloco de 16 bits.
        while raw_value:

            cipher_value = cryptoFn(raw_value)
            # Compara o tamanho do bloco cifrado e o original
            if len(raw_value) != len(cipher_value):
                raise ValueError('Valor cifrado difere em tamanho {} do original {}'.format(len(cipher_value), len(raw_value)))

            # Aponta para o inicio do arquivo original e o sobescreve com 'cipher_value'
            _file.seek(- len(raw_value), 1)
            _file.write(cipher_value)
            raw_value = _file.read(blockSize)
