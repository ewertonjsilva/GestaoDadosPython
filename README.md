# Gestão de Dados com Python

Uma solução robusta e profissional para processamento, transformação e análise de dados de vendas utilizando Python. Este projeto demonstra boas práticas de engenharia de dados, incluindo pipelines de transformação, conexão com banco de dados e análise exploratória.

## 📋 Visão Geral

Gestão de Dados com Python é um projeto educacional que implementa um pipeline completo de dados, desde a coleta e processamento até a transformação e análise de dados de vendas. O projeto utiliza Jupyter Notebooks para exploração interativa e módulos Python reutilizáveis para operações de transformação e persistência de dados.

## ✨ Recursos Principais

- **Processamento de Dados**: Transformação e limpeza de dados de vendas em larga escala
- **Pipeline de Transformação**: Módulos especializados para diferentes tipos de transformações
  - Transformadores genéricos para operações comuns
  - Transformadores específicos para casos de uso particulares
- **Conexão com Banco de Dados**: Gerenciamento seguro e eficiente de conexões com banco de dados
- **Análise Exploratória**: Notebooks interativos para análise e visualização de dados
- **Arquitetura Modular**: Separação clara entre componentes para facilitar manutenção e extensão

## 📁 Estrutura do Projeto

```
GestaoDadosPython/
├── data/                      # Dados de entrada e processados
│   ├── vendas.csv            # Dados brutos de vendas
│   └── vendas_processadas.csv # Dados após processamento
├── notebooks/                 # Análise exploratória
│   ├── experimento_01.ipynb  # Análise inicial dos dados
│   ├── experimento_02.ipynb  # Exploração de padrões
│   └── experimento_03.ipynb  # Validação de transformações
├── src/                       # Código fonte principal
│   ├── components/           # Transformadores de dados
│   │   ├── transformers.py   # Transformadores genéricos
│   │   └── transformersCasoNome.py # Transformadores específicos
│   └── database/             # Gerenciamento de banco de dados
│       └── connection.py      # Conexão com BD
├── requirements.txt           # Dependências do projeto
├── LICENSE                    # Licença do projeto
└── README.md                  # Este arquivo
```

## 🚀 Como Começar

### Requisitos

- Python 3.8 ou superior
- pip ou conda para gerenciamento de pacotes
- Jupyter Notebook (para análise exploratória)

### Instalação

1. Clone o repositório:
```bash
git clone <seu-repositorio>
cd GestaoDadosPython
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 📊 Notebooks Disponíveis

O projeto inclui três notebooks Jupyter para análise exploratória:

- **experimento_01.ipynb**: Análise inicial dos dados de vendas
- **experimento_02.ipynb**: Exploração de padrões e tendências
- **experimento_03.ipynb**: Validação das transformações aplicadas

Para executar os notebooks:
```bash
jupyter notebook
```

## 🔧 Módulos Principais

### Transformadores (`src/components/`)

- **transformers.py**: Implementa transformadores genéricos para operações comuns de processamento de dados
- **transformersCasoNome.py**: Contém transformadores específicos para casos de uso particulares

### Banco de Dados (`src/database/`)

- **connection.py**: Gerencia a conexão e operações com banco de dados

## 📝 Fluxo de Dados

```
Dados Brutos (vendas.csv)
        ↓
Transformação
        ↓
Validação
        ↓
Persistência em BD
        ↓
Dados Processados (vendas_processadas.csv)
```

## 📄 Licença

Este projeto está licenciado sob a licença especificada no arquivo [LICENSE](LICENSE).

---

**Desenvolvido como projeto educacional para demonstrar boas práticas em gestão e análise de dados com Python.**
