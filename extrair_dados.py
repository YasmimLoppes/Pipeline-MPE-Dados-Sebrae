import json
import os
from datetime import datetime
from dotenv import load_dotenv
from utils import criar_pasta

load_dotenv()

UF_ALVO = os.getenv("UF_ALVO", "SP")
PASTA_BRUTOS = "dados/brutos"
criar_pasta(PASTA_BRUTOS)

def gerar_dados_exemplo():
    # Dados no mesmo formato que viria da API DataSebrae/Receita Federal
    registros = [
        {
            "cnpj": "12345678901234",
            "razao_social": "LOJA DE CALCADOS SILVA LTDA",
            "uf": "SP",
            "municipio": "SAO PAULO",
            "situacao_cadastral": "ATIVA",
            "porte": "MICROEMPRESA",
            "data_abertura": "2020-03-15"
        },
        {
            "cnpj": "98765432109876",
            "razao_social": "MERCEARIA SOUZA MEI",
            "uf": "SP",
            "municipio": "SANTOS",
            "situacao_cadastral": "ATIVA",
            "porte": "MEI",
            "data_abertura": "2022-07-22"
        },
        {
            "cnpj": "45678901234567",
            "razao_social": "FABRICA DE MOVEIS COSTA LTDA",
            "uf": "SP",
            "municipio": "CAMPINAS",
            "situacao_cadastral": "INATIVA",
            "porte": "EMPRESA DE PEQUENO PORTE",
            "data_abertura": "2018-11-05"
        },
        {
            "cnpj": "78901234567890",
            "razao_social": "SERVICOS DE LIMPEZA PEREIRA LTDA",
            "uf": "SP",
            "municipio": "SAO VICENTE",
            "situacao_cadastral": "ATIVA",
            "porte": "MICROEMPRESA",
            "data_abertura": "2021-01-10"
        },
        {
            "cnpj": "23456789012345",
            "razao_social": "PADARIA LIMA EIRELI",
            "uf": "SP",
            "municipio": "GUARUJA",
            "situacao_cadastral": "ATIVA",
            "porte": "EMPRESA DE PEQUENO PORTE",
            "data_abertura": "2019-09-30"
        }
    ]

    saida = {
        "total_registros": len(registros),
        "data_extracao": datetime.now().isoformat(),
        "uf": UF_ALVO,
        "resultados": registros
    }

    nome_arq = f"{PASTA_BRUTOS}/mpe_{UF_ALVO}_{datetime.now().strftime('%Y%m%d_%H%M')}.json"
    with open(nome_arq, "w", encoding="utf-8") as f:
        json.dump(saida, f, ensure_ascii=False, indent=2)

    print(f"✅ Arquivo de dados gerado: {nome_arq}")
    print(f"Total de registros: {len(registros)}")
    return saida

if __name__ == "__main__":
    gerar_dados_exemplo()