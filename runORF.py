# -*- coding: utf-8 -*-

import re

# Função para selecionar as partes das sequências que começam com "M" e param no primeiro "-"
def select_orfs(sequence):
    orfs = []
    pattern = r'M[^-]*-'
    matches = re.findall(pattern, sequence)
    for match in matches:
        orfs.append(match.strip('-'))
    return orfs

# Função para ler e processar várias sequências de proteína em um arquivo
def process_sequences(input_file, output_file):
    with open(input_file, 'r') as file:
        sequences = file.read().split('>')  # Divide o conteúdo em sequências individuais
        with open(output_file, 'w') as output:
            for seq in sequences:
                if seq.strip():  # Ignora linhas em branco
                    lines = seq.strip().split('\n')
                    header = lines[0]  # Extrai o cabeçalho da sequência
                    sequence = ''.join(lines[1:])  # Junta as linhas da sequência
                    orfs = select_orfs(sequence)  # Seleciona as ORFs na sequência
                    output.write(header + '\n')
                    output.write('\n'.join(orfs) + '\n')

# Nome do arquivo de entrada com várias sequências de proteína
input_file = 'input.fasta'
# Nome do arquivo de saída para as partes selecionadas das sequências
output_file = 'output.fasta'

# Processa as sequências no arquivo de entrada e salva a saída no arquivo de saída
process_sequences(input_file, output_file)

print("Processo conclu\u00EDdo. Sa\u00EDda salva em", output_file)
