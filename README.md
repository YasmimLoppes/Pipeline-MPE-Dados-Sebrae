#  Pipeline-MPE-Dados-Sebrae
## Pipeline Completo de Dados e Análise de Micro e Pequenas Empresas de São Paulo
**Fonte de dados**: Sebrae-SP

---

##  Objetivo do Projeto
Este projeto estrutura, limpa, valida e analisa dados oficiais sobre Micro e Pequenas Empresas (MPE) do estado de São Paulo, disponibilizados pelo Sebrae. O objetivo principal é transformar dados brutos em informações confiáveis, acessíveis e visualizáveis, gerando insights que auxiliem no entendimento do cenário empreendedor paulista, identificação de oportunidades, desafios e tendências por região, setor e porte empresarial.

Além disso, implementa um **pipeline de dados replicável e escalável**, seguindo boas práticas de engenharia de dados, garantindo qualidade, rastreabilidade e facilidade de atualização quando novas versões dos dados forem disponibilizadas.

---

##  Contexto e Importância
As Micro e Pequenas Empresas representam mais de 99% dos estabelecimentos formais em São Paulo, respondem por cerca de 50% dos empregos gerados e são fundamentais para a economia estadual e nacional. No entanto, os dados brutos disponibilizados frequentemente apresentam inconsistências, campos ausentes, formatos mistos e falta de padronização o que dificulta análises rápidas e seguras.

Este projeto resolve esse problema ao criar uma estrutura sólida que:
- Preserva os dados originais sem alterações
- Aplica regras rigorosas de validação e limpeza
- Consolida informações de diferentes fontes e abrangências
- Disponibiliza os dados em formato pronto para análise e visualização
- Permite a construção de dashboards interativos e atualizáveis

---

##  Arquitetura e Fluxo do Pipeline
Segue o modelo **ETL (Extração → Transformação → Carga)** com camadas de validação e auditoria em todas as etapas:

Dados Brutos Sebrae → Extração → Validação de Qualidade → Transformação e Padronização → Consolidação → Carga e Exportação → Dashboard Power BI


### 1️⃣ Extração
- Leitura automatizada de arquivos nos formatos CSV, XLSX e JSON do portal de dados abertos do Sebrae-SP
- Suporte a importação direta por API ou carregamento de arquivos locais
- Registro completo de origem, data de coleta e metadados de cada fonte
- Preservação integral dos arquivos originais na pasta `dados/raw/`

### 2️⃣ Validação de Dados
Antes de qualquer alteração, passam por verificações rigorosas:
- Verificação de integridade e ausência de corrupção
- Validação de tipos de dados (números, datas, códigos de região/setor)
- Identificação e classificação de valores ausentes, duplicados ou inválidos
- Conferência de consistência com bases de referência (IBGE, CNAE, códigos de municípios)
- Registro de todos os problemas em relatório de qualidade

### 3️⃣ Transformação e Padronização
- Uniformização de nomes de colunas e formatos de texto
- Conversão e normalização de datas, valores monetários e percentuais
- Tratamento direcionado para valores ausentes (sem exclusão indiscriminada)
- Criação de campos calculados: taxa de formalização, tempo de atividade, participação setorial
- Agrupamento por região, município, porte da empresa e segmento econômico

### 4️⃣ Consolidação e Carga
- Integração de múltiplas bases em um único conjunto de dados estruturado
- Exportação em formatos abertos (.csv, .parquet) e compatíveis com ferramentas de BI
- Registro de versão e carimbo de data/hora de cada processamento
- Organização final na pasta `dados/processed/`

---

##  Estrutura Completa do Projeto

Pipeline-MPE-Dados-Sebrae/
├── dados/ # Todos os arquivos de dados
│ ├── raw/ # Dados brutos originais (não alterar)
│ ├── interim/ # Dados em processo de tratamento
│ └── processed/ # Dados finais padronizados e consolidados
├── scripts/ # Códigos Python do pipeline
│ ├── 01_extracao.py # Módulo de coleta e leitura
│ ├── 02_validacao.py # Verificação de qualidade
│ ├── 03_transformacao.py # Limpeza e padronização
│ └── 04_consolidacao.py # Integração de bases
├── dashboard/ # Arquivos do Power BI
│ └── modelo_dados.pbix # Dashboard completo
├── docs/ # Documentação complementar
│ ├── dicionario_dados.md # Explicação de todos os campos
│ └── relatorio_qualidade.md # Relatório de validação
├── requirements.txt # Bibliotecas e versões utilizadas
├── .gitignore # Arquivos ignorados no versionamento
└── README.md # Este documento


---

##  Tecnologias e Ferramentas Utilizadas
| Ferramenta/Biblioteca | Versão | Finalidade 
| Python | 3.11+ | Linguagem principal do pipeline 
| Pandas | 2.2+ | Manipulação e análise de dados tabulares 
| NumPy | 1.26+ | Cálculos matemáticos e tratamento de valores 
| Requests | 2.31+ | Coleta de dados por API 
| Power BI Desktop | Última | Construção de dashboard interativo 
| Git/GitHub | Versionamento do projeto 

---

##  Principais Indicadores e Análises Disponíveis
- Quantidade de MPE por porte e por região do estado
- Distribuição por setor econômico (Comércio, Serviços, Indústria, Agropecuária)
- Taxa de formalização e evolução ao longo dos anos
- Perfil de empregabilidade por município
- Comparativo entre regiões e identificação de polos de crescimento
- Tendências de abertura e fechamento de empresas por segmento

---

##  Como Reproduzir o Projeto
### Pré-requisitos
- Python 3.11 ou superior
- Gerenciador de pacotes `pip`

### Passo a Passo
1. Clone o repositório:
```bash
git clone https://github.com/YasmimLoppes/Pipeline-MPE-Dados-Sebrae.git
cd Pipeline-MPE-Dados-Sebrae

Instale as dependências:

pip install -r requirements.txt

Execute as etapas na ordem:

python scripts/01_extracao.py
python scripts/02_validacao.py
python scripts/03_transformacao.py
python scripts/04_consolidacao.py

Abra dashboard/modelo_dados.pbix no Power BI para visualização

✅ Boas Práticas Aplicadas
Rastreabilidade completa: toda alteração é registrada
Reexecução segura: sem geração de duplicatas
Modularidade: cada etapa funciona de forma independente
Segurança: dados originais nunca são sobrescritos

📄 Licença
Dados públicos do Sebrae-SP, disponíveis para fins educacionais, de pesquisa e aplicação profissional, seguindo as regras de uso da instituição.

Desenvolvido por **Yamim Lopes** | Focado em transformar dados brutos do Sebrae em inteligência de negócio robusta para o cenário de MPE de São Paulo.

