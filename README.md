# Health Insurance Cost Predictor Model

Este projeto treina e avalia modelos de regressão para prever os encargos médicos individuais ("charges") de seguros de saúde, usando a base `data/raw/insurance.csv`. O fluxo principal acontece em um Jupyter Notebook com análise exploratória (EDA), pré-processamento e treinamento de modelos.

## Estrutura do Projeto
- `notebooks/FIAP_AI_para_DEVs_Fase_1_Desafio_Machine_Learning.ipynb`: Notebook principal com EDA, pré-processamento, treino e avaliação dos modelos.
- `data/raw/insurance.csv`: Base de dados bruta utilizada.
- `requirements.txt` e `requirements-dev.txt`: Dependências do projeto.
- `src/`, `tests/`, `models/`, `reports/`: Pastas para código, testes, modelos e relatórios.

## Pré-requisitos
- Python 3.10+ instalado
- Pip instalado
- VS Code (recomendado) com extensão Jupyter

### Configuração manual com venv
```bash
# Na raiz do projeto
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
```

Se desejar dependências extras de desenvolvimento:
```bash
pip install -r requirements-dev.txt
```

## Executando o Notebook
1. Abra o VS Code na pasta do projeto:
```bash
code .
```
2. Abra o notebook: `notebooks/FIAP_AI_para_DEVs_Fase_1_Desafio_Machine_Learning.ipynb`.
3. Selecione o kernel Python do seu ambiente (`.venv`).
4. Execute as células na ordem. As primeiras células:
   - Importam bibliotecas (pandas, numpy, matplotlib, seaborn).
   - Carregam a base: `df = pd.read_csv('../data/raw/insurance.csv')`.
   - Fazem EDA, pré-processamento (remoção de duplicatas, LabelEncoder para `sex` e `smoker`, OneHot para `region`), divisão treino/teste estratificada por `smoker` e treino dos modelos:
     - `LinearRegression`
     - `RandomForestRegressor`
     - `DecisionTreeRegressor`
     - `GradientBoostingRegressor`
   - Avaliam métricas (`R2`, `MAE`, `MSE`, `MAPE`) e geram gráficos comparativos.

## Saídas Esperadas
- Tabela comparativa de métricas por modelo.
- Gráficos de EDA (histogramas, heatmap de correlação, pairplots).
- Gráfico de dispersão Valor Real vs Predito (Gradient Boosting).

## Dicas e Solução de Problemas
- Erro ao carregar CSV: confirme o caminho relativo no notebook (`../data/raw/insurance.csv`) quando o notebook estiver em `notebooks/`.
- Kernel errado: troque para o Python do `.venv` no topo do notebook (selector de kernel).

## Reprodutibilidade
Para garantir resultados reprodutíveis, o notebook define `np.random.seed(42)` e usa `random_state=42` na divisão de treino.

## Licença
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Uso educacional. Ajuste conforme necessário para seu contexto.

