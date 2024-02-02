# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanhoArquivo = float(input("Qual o tamanho do arquivo a ser baixado em MB: "))
velocidadeLink = float(input("Qual a velocidade do Link da sua internet em Mbps: "))

tempoDeDownload = (tamanhoArquivo/velocidadeLink)/60

print(f"Seu download será concluído em {tempoDeDownload} minutos")
