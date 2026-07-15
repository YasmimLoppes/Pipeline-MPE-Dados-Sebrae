# **Pipeline-MPE-Dados-Sebrae**
## **Pipeline Completo de Dados e Análise de Micro e Pequenas Empresas de São Paulo**
**Fonte de dados**: Sebrae-SP

---

##  Objetivo do Projeto
Este projeto estrutura, limpa, valida e analisa dados oficiais sobre Micro e Pequenas Empresas (MPE) do estado de São Paulo, disponibilizados pelo Sebrae. O objetivo principal é transformar dados brutos em informações confiáveis, acessíveis e visualizáveis, gerando insights que auxiliem no entendimento do cenário empreendedor paulista, na identificação de oportunidades, desafios e tendências por região, setor e porte empresarial.

Além disso, implementa um **pipeline de dados replicável e escalável**, seguindo boas práticas de engenharia de dados, garantindo qualidade, rastreabilidade e facilidade de atualização sempre que novas versões dos dados forem disponibilizadas.

---

##  Contexto e Importância
As Micro e Pequenas Empresas representam mais de 99% dos estabelecimentos formais em São Paulo, respondem por cerca de 50% dos empregos gerados e são fundamentais para a economia estadual e nacional. No entanto, os dados brutos disponibilizados frequentemente apresentam inconsistências, campos ausentes, formatos mistos e falta de padronização — o que dificulta análises rápidas e seguras.

Este projeto resolve esse problema ao criar uma estrutura sólida que:
- Preserva os dados originais sem nenhuma alteração
- Aplica regras rigorosas de validação e limpeza
- Consolida informações de diferentes fontes e abrangências geográficas ou temporais
- Disponibiliza os dados em formato pronto para análise e visualização
- Permite a construção de dashboards interativos e facilmente atualizáveis

---

##  Arquitetura e Fluxo do Pipeline
Segue o modelo **ETL (Extração → Transformação → Carga)**, com camadas de validação e auditoria em todas as etapas:

`Dados Brutos Sebrae → Extração → Validação de Qualidade → Transformação e Padronização → Consolidação → Carga e Exportação → Dashboard Power BI`

### 1️⃣ Extração
- Leitura automatizada de arquivos nos formatos CSV, XLSX e JSON, obtidos do portal de dados abertos do Sebrae-SP
- Suporte a importação direta por API ou carregamento manual de arquivos locais
- Registro completo de origem, data de coleta e metadados de cada fonte consultada
- Preservação integral dos arquivos originais na pasta `dados/raw/`

### 2️⃣ Validação de Dados
Antes de qualquer alteração, os dados passam por verificações rigorosas:
- Verificação de integridade e ausência de corrupção nos arquivos
- Validação de tipos de dados (números, datas, códigos de região e setor econômico)
- Identificação e classificação de valores ausentes, duplicados ou inválidos
- Conferência de consistência com bases de referência oficiais (IBGE, CNAE, códigos de municípios)
- Registro detalhado de todos os problemas encontrados em relatório de qualidade

### 3️⃣ Transformação e Padronização
- Uniformização de nomes de colunas e formatos de texto
- Conversão e normalização de datas, valores monetários e percentuais
- Tratamento direcionado para valores ausentes (sem exclusão indiscriminada de registros)
- Criação de campos calculados: taxa de formalização, tempo de atividade, participação setorial
- Agrupamento por região, município, porte da empresa e segmento econômico

### 4️⃣ Consolidação e Carga
- Integração de múltiplas bases de dados em um único conjunto estruturado e consistente
- Exportação em formatos abertos (.csv, .parquet) e compatíveis com ferramentas de BI
- Registro de versão e carimbo de data/hora de cada processamento realizado
- Organização final dos arquivos na pasta `dados/processed/`

---

##  Estrutura Completa do Projeto
Pipeline-MPE-Dados-Sebrae/
├── dados/ # Todos os arquivos de dados do projeto
│ ├── raw/ # Dados brutos originais (NÃO ALTERAR)
│ ├── interim/ # Dados em processo de tratamento
│ └── processed/ # Dados finais padronizados e consolidados
├── scripts/ # Códigos Python do pipeline
│ ├── 01_extracao.py # Módulo de coleta e leitura de dados
│ ├── 02_validacao.py # Módulo de verificação de qualidade
│ ├── 03_transformacao.py # Módulo de limpeza e padronização
│ └── 04_consolidacao.py # Módulo de integração de bases
├── dashboard/ # Arquivos do painel de visualização
│ └── modelo_dados.pbix # Dashboard completo no Power BI
├── docs/ # Documentação complementar
│ ├── dicionario_dados.md # Explicação detalhada de todos os campos
│ └── relatorio_qualidade.md # Relatório de validação de dados
├── requirements.txt # Lista de bibliotecas e versões utilizadas
├── .gitignore # Arquivos e pastas ignorados no versionamento
└── README.md # Documentação principal do projeto


---

##  Tecnologias e Ferramentas Utilizadas
| Ferramenta/Biblioteca | Versão recomendada | Finalidade |
|---|---|---|
| Python | 3.11 ou superior | Linguagem principal de desenvolvimento do pipeline |
| Pandas | 2.2 ou superior | Manipulação e análise de dados tabulares |
| NumPy | 1.26 ou superior | Cálculos matemáticos e tratamento de valores numéricos |
| Requests | 2.31 ou superior | Coleta automatizada de dados por API |
| Power BI Desktop | Última versão estável | Construção de dashboard interativo |
| Git / GitHub | — | Controle de versão e compartilhamento do projeto |

---

##  Principais Indicadores e Análises Disponíveis
- Quantidade de MPE por porte e por região do estado de São Paulo
- Distribuição por setor econômico (Comércio, Serviços, Indústria, Agropecuária)
- Taxa de formalização e sua evolução ao longo dos anos
- Perfil de empregabilidade gerada por município
- Comparativo entre regiões e identificação de polos de crescimento
- Tendências de abertura e fechamento de empresas por segmento

---

##  Como Reproduzir o Projeto
### Pré-requisitos
- Python 3.11 ou superior instalado
- Gerenciador de pacotes `pip`

### Passo a Passo
1. Clone o repositório:
```bash
git clone https://github.com/YasmimLoppes/Pipeline-MPE-Dados-Sebrae.git
cd Pipeline-MPE-Dados-Sebrae

pip install -r requirements.txt
python scripts/01_extracao.py
python scripts/02_validacao.py
python scripts/03_transformacao.py
python scripts/04_consolidacao.py

Abra o arquivo dashboard/modelo_dados.pbix no Power BI para visualização dos resultados.

Boas Práticas Aplicadas
Rastreabilidade completa: toda alteração nos dados é registrada com origem e data
Reexecução segura: novas execuções não geram duplicatas ou sobrescrevem arquivos
Modularidade: cada etapa funciona de forma independente, facilitando ajustes e manutenção
Segurança: dados originais na pasta raw/ nunca são sobrescritos ou modificados
Licença
Os dados utilizados são públicos, disponibilizados pelo Sebrae-SP, e podem ser utilizados para fins educacionais, de pesquisa e aplicação profissional, seguindo as regras de uso definidas pela instituição.

Desenvolvido por # **Yasmim Loppes**
Focada em transformar dados brutos do Sebrae em inteligência de negócio para o cenário de Micro e Pequenas Empresas de São Paulo.