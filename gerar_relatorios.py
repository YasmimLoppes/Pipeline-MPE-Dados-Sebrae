import pandas as pd
import matplotlib.pyplot as plt
import os
from utils import criar_pasta

PASTA_PBI = "dados/powerbi"
PASTA_GRAFICOS = "relatorios/graficos"
criar_pasta(PASTA_GRAFICOS)

plt.rcParams["font.family"] = "Arial"

def fazer_graficos():
    df = pd.read_csv(f"{PASTA_PBI}/base_mpe_sp.csv", sep=";", encoding="utf-8-sig")

    # Quantidade por porte
    df["porte"].value_counts().plot(kind="bar", color="#2c3e50")
    plt.title("Quantidade de Empresas por Porte")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(f"{PASTA_GRAFICOS}/por_porte.png", dpi=150)
    plt.close()

    # Situação cadastral
    df["situacao_cadastral"].value_counts().plot(kind="pie", autopct="%1.1f%%")
    plt.title("Situação Cadastral")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(f"{PASTA_GRAFICOS}/por_situacao.png", dpi=150)
    plt.close()

    print("Gráficos salvos na pasta relatorios/graficos")

if __name__ == "__main__":
    fazer_graficos()