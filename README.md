# Employee Churn Predictor Model 🤖

Projeto de Machine Learning para prever o abandono (churn) de colaboradores em uma empresa, utilizando a base de dados `HR_Abandono.csv`. O modelo final atingiu **96.50% de acurácia** usando algoritmo **KNN (K=7)**, capaz de identificar colaboradores com risco de saída e apoiar o RH em ações preventivas de retenção.

## 📊 Sobre o Projeto

Este projeto faz parte do **Desafio Machine Learning Avançado - FIAP AI para DEVs (Fase 1)** e implementa um pipeline completo de ciência de dados, desde a análise exploratória até a validação de modelos de classificação.

### Objetivo
Construir um modelo preditivo capaz de identificar colaboradores com alta probabilidade de deixar a empresa, permitindo que o RH tome ações preventivas de retenção.

### Dataset
- **Arquivo**: `data/raw/HR_Abandono.csv` (separador: ponto-e-vírgula)
- **Registros**: ~15.000 colaboradores
- **Variável Target**: `left` (0 = permaneceu, 1 = saiu)
- **Principais Features**:
  - `satisfaction_level`: Nível de satisfação (0 a 1)
  - `last_evaluation`: Última avaliação de desempenho (0 a 1)
  - `average_montly_hours`: Média de horas trabalhadas por mês
  - `time_spend_company`: Tempo de empresa (anos)
  - `num_project`: Número de projetos
  - `Work_accident`: Acidente de trabalho (0/1)
  - `promotion_last_5years`: Promoção nos últimos 5 anos (0/1)
  - `salary`: Nível salarial (low, medium, high)
  - `depto`: Departamento do colaborador

## 🗂️ Estrutura do Projeto

```
├── data/
│   ├── raw/                    # Dados brutos
│   │   └── HR_Abandono.csv
│   ├── processed/              # Dados processados
│   ├── interim/                # Dados intermediários
│   └── external/               # Dados externos
├── notebooks/
│   └── FIAP_AI_para_DEVs_Fase_1_Desafio_Machine_Learning_Avançado.ipynb
├── src/                        # Código fonte
├── models/                     # Modelos treinados
├── reports/                    # Relatórios e visualizações
│   └── figures/
├── tests/                      # Testes unitários
├── requirements.txt            # Dependências principais
├── requirements-dev.txt        # Dependências de desenvolvimento
└── README.md
```

## 🚀 Começando

### Pré-requisitos
- Python 3.10 ou superior
- pip (gerenciador de pacotes Python)
- Graphviz (para visualização de árvores de decisão). Baixe e instale o Graphviz através do [site oficial](https://graphviz.org/download/).
- VS Code com extensão Jupyter (recomendado)

### Instalação

1. **Clone ou copie o projeto**
```bash
cd employee-churn-predictor-model
```

2. **Crie e ative um ambiente virtual**
```bash
# Criar ambiente virtual
python -m venv .venv

# Ativar no Windows
.venv\Scripts\activate

# Ativar no Linux/Mac
source .venv/bin/activate
```

3. **Instale as dependências**
```bash
# Dependências principais
pip install -r requirements.txt

# Opcional: dependências de desenvolvimento
pip install -r requirements-dev.txt
```

4. **Instale pacotes adicionais para visualizações**
```bash
pip install dtreeviz yellowbrick
```

### Executando o Notebook

1. Abra o VS Code na pasta do projeto:
```bash
code .
```

2. Abra o notebook: `notebooks/FIAP_AI_para_DEVs_Fase_1_Desafio_Machine_Learning_Avançado.ipynb`

3. Selecione o kernel Python do ambiente virtual (`.venv`)

4. Execute as células sequencialmente

## 📈 Pipeline de Machine Learning

### 1. Análise Exploratória de Dados (EDA)
- ✅ Verificação de valores nulos e duplicados
- ✅ Identificação e tratamento de outliers (ex: registro com 810 horas/mês removido)
- ✅ Conversão de tipos de dados (satisfaction_level e last_evaluation de string para float)
- ✅ Estatística descritiva detalhada
- ✅ Análise de correlações e distribuições
- ✅ Visualizações: boxplots, histogramas, pairplots, heatmaps, gráficos de contagem

### 2. Pré-processamento
- **Limpeza**: Remoção de outliers e tratamento de inconsistências
- **Encoding**: One-Hot Encoding para variáveis categóricas (`salary`, `depto`)
- **Seleção de Features**: 8 variáveis finais selecionadas com base em análise de correlação
- **Escalonamento**: StandardScaler aplicado em modelos que requerem normalização
- **Divisão**: 80% treino / 20% teste com estratificação pela variável target

### 3. Modelos Treinados e Comparados
| Modelo | Acurácia | Precision (Sai) | Recall (Sai) | F1-Score | ROC-AUC |
|--------|----------|----------------|--------------|----------|---------|
| **KNN (K=7)** ⭐ | **96.50%** | **95%** | **91%** | **93%** | **98%** |
| KNN (K=6) | 96.93% | 96% | 93% | 94% | 98% |
| SVM | 96.33% | 95% | 90% | 92% | 97% |
| Floresta Aleatória | 90.80% | 91% | 68% | 78% | - |
| Árvore de Decisão | 82.13% | 100% | 25% | 40% | - |
| Regressão Logística | ~75% | - | - | - | - |

**Modelo Selecionado**: KNN (K=7)
- Melhor equilíbrio entre precisão e recall
- Apenas 59 falsos negativos (colaboradores que saíram mas foram classificados como permanentes)
- Evita problema de empate do K par (K=6)

### 4. Validação e Métricas
- ✅ Matriz de Confusão
- ✅ Relatórios de Classificação (Precision, Recall, F1-Score)
- ✅ Curvas ROC com AUC
- ✅ Análise de Coeficientes (Regressão Logística)
- ✅ Importância de Features (Árvores)
- ✅ Visualização de Árvores de Decisão com dtreeviz

## 🔍 Principais Descobertas

### Fatores que mais influenciam a evasão:
1. **Nível de Satisfação** 📉: Forte correlação negativa (-0.39) - quanto menor a satisfação, maior a chance de saída
2. **Salário Baixo** 💰: ~68% dos que saem têm salário baixo ou médio
3. **Tempo de Empresa** ⏱️: Correlação positiva (0.22) - colaboradores podem sair após cumprir determinado tempo
4. **Horas Trabalhadas** 🕐: Média mais alta entre quem sai

### Grupos de risco identificados:
- **Grupo 1**: Alta performance + baixa satisfação (burnout)
- **Grupo 2**: Baixa performance + satisfação média (~0.4)
- **Grupo 3**: Insatisfação extrema (nível ≤ 0.11) - 100% de evasão

## 📊 Saídas e Visualizações

O notebook gera:
- 📈 Histogramas e boxplots de todas as variáveis numéricas
- 🔥 Heatmap de correlação
- 📊 Gráficos de contagem por salário e departamento
- 🎯 Matrizes de confusão para todos os modelos
- 📉 Curvas ROC comparativas
- 🌳 Visualizações de árvores de decisão
- 📋 Relatórios de classificação com métricas detalhadas

## 🛠️ Tecnologias Utilizadas

- **Linguagem**: Python 3.10+
- **Análise e Manipulação**: pandas, numpy
- **Visualização**: matplotlib, seaborn, dtreeviz, yellowbrick
- **Machine Learning**: scikit-learn
- **Ambiente**: Jupyter Notebook / JupyterLab

## ⚠️ Dicas e Solução de Problemas

### Erro ao carregar o CSV
- Confirme que o arquivo está em `data/raw/HR_Abandono.csv`
- Verifique o separador (`;` no código)
- No notebook, o caminho relativo é `HR_Abandono.csv` pois o notebook está em `notebooks/`

### Kernel errado
- Selecione o kernel Python do ambiente virtual `.venv` no canto superior direito do notebook

### Avisos (Warnings)
- O notebook já inclui `warnings.filterwarnings("ignore")` para silenciar avisos não críticos

### Performance lenta
- O treinamento de alguns modelos pode levar alguns minutos
- KNN com grandes datasets pode ser mais lento na predição

## 🔄 Reprodutibilidade

Todos os processos aleatórios usam `random_state=42` para garantir resultados reprodutíveis:
- Divisão treino/teste
- Inicialização de modelos
- Seed do NumPy

## 📝 Próximos Passos

- [ ] Implementar Grid Search para otimização de hiperparâmetros
- [ ] Testar algoritmos de ensemble avançados (XGBoost, LightGBM)
- [ ] Criar pipeline automatizado de retreinamento
- [ ] Desenvolver API REST para predições em produção
- [ ] Implementar monitoramento de drift de dados

## 📄 Licença

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Uso educacional. Ajuste conforme necessário para seu contexto.

---

**Desenvolvido como parte do Desafio FIAP - AI para DEVs (Fase 1)**

