import json
import os
from pydantic import BaseModel, Field, ValidationError
from utils import criar_pasta, listar_arquivos

PASTA_BRUTOS = "dados/brutos"
PASTA_VALIDADOS = "dados/validados"
criar_pasta(PASTA_VALIDADOS)

class EmpresaMPE(BaseModel):
    cnpj: str = Field(min_length=14, max_length=14)
    razao_social: str = Field(min_length=2)
    uf: str = Field(pattern=r"^[A-Z]{2}$")
    municipio: str
    situacao_cadastral: str
    porte: str
    data_abertura: str

def validar():
    for arq in listar_arquivos(PASTA_BRUTOS, ".json"):
        caminho = os.path.join(PASTA_BRUTOS, arq)
        with open(caminho, "r", encoding="utf-8") as f:
            dados = json.load(f)

        registros = dados.get("resultados", [])
        validos = []
        cont_invalidos = 0

        for item in registros:
            try:
                validos.append(EmpresaMPE(**item).model_dump())
            except ValidationError:
                cont_invalidos += 1

        resumo = {
            "origem": arq,
            "total": len(registros),
            "validos": len(validos),
            "invalidos": cont_invalidos,
            "dados": validos
        }

        nome_saida = arq.replace(".json", "_validado.json")
        with open(os.path.join(PASTA_VALIDADOS, nome_saida), "w", encoding="utf-8") as f:
            json.dump(resumo, f, ensure_ascii=False, indent=2)

        print(f"Validação pronta: {len(validos)} ok, {cont_invalidos} com erro")

if __name__ == "__main__":
    validar()