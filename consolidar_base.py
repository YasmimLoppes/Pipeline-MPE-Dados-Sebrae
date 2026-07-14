import pandas as pd
import os
from utils import criar_pasta, listar_arquivos

PASTA_TRATADOS = "dados/tratados"
PASTA_PBI = "dados/powerbi"
criar_pasta(PASTA_PBI)

def gerar_bases():
    arquivos = listar_arquivos(PASTA_TRATADOS, "_tratado.parquet")
    lista_dfs = [pd.read_parquet(os.path.join(PASTA_TRATADOS, arq)) for arq in arquivos]
    base_principal = pd.concat(lista_dfs, ignore_index=True).drop_duplicates(subset=["cnpj"])

    base_principal.to_csv(f"{PASTA_PBI}/base_mpe_sp.csv", sep=";", encoding="utf-8-sig", index=False)

    dim_porte = base_principal[["porte"]].drop_duplicates().reset_index(drop=True)
    dim_porte["id_porte"] = dim_porte.index + 1
    dim_porte.to_csv(f"{PASTA_PBI}/dim_porte.csv", sep=";", encoding="utf-8-sig", index=False)

    dim_situacao = base_principal[["situacao_cadastral"]].drop_duplicates().reset_index(drop=True)
    dim_situacao["id_situacao"] = dim_situacao.index + 1
    dim_situacao.to_csv(f"{PASTA_PBI}/dim_situacao.csv", sep=";", encoding="utf-8-sig", index=False)

    dim_regiao = base_principal[["uf", "municipio"]].drop_duplicates().reset_index(drop=True)
    dim_regiao["id_regiao"] = dim_regiao.index + 1
    dim_regiao.to_csv(f"{PASTA_PBI}/dim_regiao.csv", sep=";", encoding="utf-8-sig", index=False)

    print(f"Todas as bases prontas na pasta {PASTA_PBI}")

if __name__ == "__main__":
    gerar_bases()