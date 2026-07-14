import os

def criar_pasta(caminho):
    os.makedirs(caminho, exist_ok=True)

def listar_arquivos(pasta, filtro=""):
    return sorted([arq for arq in os.listdir(pasta) if os.path.isfile(os.path.join(pasta, arq)) and filtro in arq])