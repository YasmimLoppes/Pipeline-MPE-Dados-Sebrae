import json
import pandas as pd
import os
from utils import criar_pasta, listar_arquivos

PASTA_VALIDADOS = "dados/validados"
PASTA_TRATADOS = "dados/tratados"
criar_pasta(PASTA_TRATADOS)

def limpar(texto):
    if pd.isna(texto):
        return ""
    return str(texto).strip().upper()

def formatar_cnpj(cnpj):
    if len(cnpj) == 14:
        return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"
    return cnpj

def tratar():
    for arq in listar_arquivos(PASTA_VALIDADOS, "_validado.json"):
        caminho = os.path.join(PASTA_VALIDADOS, arq)
        with open(caminho, "r", encoding="utf-8") as f:
            dados = json.load(f)

        df = pd.DataFrame(dados["dados"])

        df["razao_social"] = df["razao_social"].apply(limpar)
        df["municipio"] = df["municipio"].apply(limpar)
        df["situacao_cadastral"] = df["situacao_cadastral"].apply(limpar)
        df["porte"] = df["porte"].apply(limpar)
        df["cnpj_formatado"] = df["cnpj"].apply(formatar_cnpj)
        df["ano_abertura"] = pd.to_datetime(df["data_abertura"], errors="coerce").dt.year

        nome_saida = arq.replace("_validado.json", "_tratado.parquet")
        df.to_parquet(os.path.join(PASTA_TRATADOS, nome_saida), index=False)
        print(f"Tratamento concluído: {nome_saida}")

if __name__ == "__main__":
    tratar()