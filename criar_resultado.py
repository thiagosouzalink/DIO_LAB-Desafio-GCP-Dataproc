import os


diretorio_atual = os.getcwd() 

with open(f"{diretorio_atual}/resultado_part-00000", "r") as _file:
    linhas = [next(_file).strip() for _ in range(10)]
with open(f'{diretorio_atual}/resultado.txt', 'w') as r:
    for l in linhas:
        r.write(f"{l}\n")