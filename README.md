# Pipeline de Dados: Micro e Pequenas Empresas – DataSebrae + Power BI

Projeto completo de engenharia de dados usando a fonte oficial DataSebrae, com fluxo automatizado e dados prontos para análise no Power BI.

## Fonte dos dados
API DataSebrae: https://api.datasebrae.sebrae.com.br/v1
Dados de MEI, ME e EPP, com foco inicial em São Paulo.

## Como usar
1. Instale as dependências: `pip install -r requisitos.txt`
2. Configure seu token no arquivo `.env`
3. Execute os scripts na ordem:
   - `python extrair_dados.py`
   - `python validar_dados.py`
   - `python transformar_dados.py`
   - `python consolidar_base.py`
4. Use os arquivos da pasta `dados/powerbi/` no Power BI

## Pastas
- `dados/brutos`: dados diretos da API
- `dados/validados`: registros verificados
- `dados/tratados`: dados limpos
- `dados/powerbi`: bases prontas para análise