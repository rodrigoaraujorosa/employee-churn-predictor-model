# Configuração de Projeto - Machine Learning Boilerplate
# Este arquivo contém todas as configurações padrão para projetos de ML

import os
from pathlib import Path
from typing import Dict, List, Any

# =============================================================================
# CONFIGURAÇÕES DE DIRETÓRIO
# =============================================================================

PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXTERNAL_DATA_DIR = DATA_DIR / "external"
INTERIM_DATA_DIR = DATA_DIR / "interim"

MODELS_DIR = PROJECT_ROOT / "models"
REPORTS_DIR = PROJECT_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
SRC_DIR = PROJECT_ROOT / "src"
TESTS_DIR = PROJECT_ROOT / "tests"

# =============================================================================
# CONFIGURAÇÕES DE MACHINE LEARNING
# =============================================================================

# Configurações gerais
RANDOM_STATE = 42
TEST_SIZE = 0.2
VALIDATION_SIZE = 0.2
N_JOBS = -1  # Usar todos os cores disponíveis

# Configurações de validação cruzada
CV_FOLDS = 5
SCORING_CLASSIFICATION = 'accuracy'
SCORING_REGRESSION = 'r2'

# =============================================================================
# CONFIGURAÇÕES DE PREPROCESSING
# =============================================================================

# Tratamento de valores ausentes
MISSING_VALUE_THRESHOLD = 0.5  # Remover colunas com >50% de valores ausentes
MISSING_VALUE_STRATEGIES = {
    'numerical': 'median',  # 'mean', 'median', 'mode', 'constant'
    'categorical': 'mode'   # 'mode', 'constant'
}

# Detecção de outliers
OUTLIER_METHOD = 'iqr'  # 'iqr', 'zscore', 'isolation_forest'
OUTLIER_THRESHOLD = {
    'iqr': 1.5,
    'zscore': 3.0,
    'isolation_forest': 0.1
}

# Encoding de variáveis categóricas
ENCODING_METHODS = {
    'binary': 'label',      # 'label', 'target'
    'multiclass': 'onehot', # 'onehot', 'label', 'target'
    'high_cardinality': 'target'  # Para variáveis com muitas categorias
}
HIGH_CARDINALITY_THRESHOLD = 10

# Scaling/Normalização
SCALING_METHOD = 'standard'  # 'standard', 'minmax', 'robust', 'quantile'

# =============================================================================
# CONFIGURAÇÕES DE FEATURE ENGINEERING
# =============================================================================

# Seleção de features
FEATURE_SELECTION = {
    'variance_threshold': 0.01,     # Remover features com baixa variância
    'correlation_threshold': 0.95,  # Remover features altamente correlacionadas
    'univariate_k_best': 20,        # Selecionar K melhores features
    'recursive_elimination': True   # Usar RFE
}

# Feature engineering automático
AUTO_FEATURE_ENGINEERING = {
    'polynomial_features': False,   # Gerar features polinomiais
    'polynomial_degree': 2,
    'interaction_features': True,   # Gerar interações entre features
    'log_transform': True,          # Aplicar transformação log em features assimétricas
    'binning': True,                # Criar bins para variáveis numéricas
    'n_bins': 5
}

# =============================================================================
# CONFIGURAÇÕES DE MODELOS
# =============================================================================

# Modelos para classificação
CLASSIFICATION_MODELS = {
    'logistic_regression': {
        'class': 'LogisticRegression',
        'params': {
            'random_state': RANDOM_STATE,
            'max_iter': 1000,
            'n_jobs': N_JOBS
        },
        'param_grid': {
            'C': [0.1, 1.0, 10.0, 100.0],
            'penalty': ['l1', 'l2', 'elasticnet'],
            'solver': ['liblinear', 'saga']
        }
    },
    'random_forest': {
        'class': 'RandomForestClassifier',
        'params': {
            'random_state': RANDOM_STATE,
            'n_jobs': N_JOBS
        },
        'param_grid': {
            'n_estimators': [50, 100, 200, 300],
            'max_depth': [None, 10, 20, 30],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4],
            'bootstrap': [True, False]
        }
    },
    'gradient_boosting': {
        'class': 'GradientBoostingClassifier',
        'params': {
            'random_state': RANDOM_STATE
        },
        'param_grid': {
            'n_estimators': [50, 100, 200],
            'learning_rate': [0.01, 0.1, 0.2],
            'max_depth': [3, 5, 7],
            'subsample': [0.8, 1.0]
        }
    },
    'xgboost': {
        'class': 'XGBClassifier',
        'params': {
            'random_state': RANDOM_STATE,
            'n_jobs': N_JOBS,
            'eval_metric': 'logloss'
        },
        'param_grid': {
            'n_estimators': [50, 100, 200],
            'max_depth': [3, 5, 7],
            'learning_rate': [0.01, 0.1, 0.2],
            'subsample': [0.8, 1.0],
            'colsample_bytree': [0.8, 1.0]
        }
    }
}

# Modelos para regressão
REGRESSION_MODELS = {
    'linear_regression': {
        'class': 'LinearRegression',
        'params': {
            'n_jobs': N_JOBS
        },
        'param_grid': {}
    },
    'ridge': {
        'class': 'Ridge',
        'params': {
            'random_state': RANDOM_STATE
        },
        'param_grid': {
            'alpha': [0.1, 1.0, 10.0, 100.0, 1000.0]
        }
    },
    'lasso': {
        'class': 'Lasso',
        'params': {
            'random_state': RANDOM_STATE,
            'max_iter': 2000
        },
        'param_grid': {
            'alpha': [0.1, 1.0, 10.0, 100.0, 1000.0]
        }
    },
    'random_forest': {
        'class': 'RandomForestRegressor',
        'params': {
            'random_state': RANDOM_STATE,
            'n_jobs': N_JOBS
        },
        'param_grid': {
            'n_estimators': [50, 100, 200, 300],
            'max_depth': [None, 10, 20, 30],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4],
            'bootstrap': [True, False]
        }
    },
    'gradient_boosting': {
        'class': 'GradientBoostingRegressor',
        'params': {
            'random_state': RANDOM_STATE
        },
        'param_grid': {
            'n_estimators': [50, 100, 200],
            'learning_rate': [0.01, 0.1, 0.2],
            'max_depth': [3, 5, 7],
            'subsample': [0.8, 1.0]
        }
    }
}

# =============================================================================
# CONFIGURAÇÕES DE AVALIAÇÃO
# =============================================================================

# Métricas para classificação
CLASSIFICATION_METRICS = [
    'accuracy', 'precision', 'recall', 'f1_score', 
    'roc_auc', 'precision_recall_auc'
]

# Métricas para regressão
REGRESSION_METRICS = [
    'r2_score', 'mse', 'rmse', 'mae', 'mape'
]

# Configurações de validação
VALIDATION_CONFIG = {
    'train_test_split': {
        'test_size': TEST_SIZE,
        'random_state': RANDOM_STATE,
        'stratify': True  # Para classificação
    },
    'cross_validation': {
        'cv': CV_FOLDS,
        'scoring': 'accuracy',  # Será definido dinamicamente
        'n_jobs': N_JOBS
    },
    'grid_search': {
        'cv': CV_FOLDS,
        'n_jobs': N_JOBS,
        'scoring': 'accuracy',  # Será definido dinamicamente
        'verbose': 1
    },
    'randomized_search': {
        'n_iter': 50,
        'cv': CV_FOLDS,
        'n_jobs': N_JOBS,
        'scoring': 'accuracy',  # Será definido dinamicamente
        'random_state': RANDOM_STATE,
        'verbose': 1
    }
}

# =============================================================================
# CONFIGURAÇÕES DE VISUALIZAÇÃO
# =============================================================================

VISUALIZATION_CONFIG = {
    'style': 'whitegrid',
    'palette': 'husl',
    'figure_size': (12, 8),
    'dpi': 100,
    'save_format': 'png',
    'save_dpi': 300
}

PLOTLY_CONFIG = {
    'template': 'plotly_white',
    'width': 800,
    'height': 600
}

# =============================================================================
# CONFIGURAÇÕES DE LOGGING
# =============================================================================

LOGGING_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'handlers': {
        'file': {
            'filename': 'ml_project.log',
            'max_bytes': 10485760,  # 10MB
            'backup_count': 5
        },
        'console': {
            'stream': 'stdout'
        }
    }
}

# =============================================================================
# CONFIGURAÇÕES DE DADOS
# =============================================================================

# Configurações de carregamento de dados
DATA_LOADING_CONFIG = {
    'csv': {
        'encoding': 'utf-8',
        'sep': ',',
        'na_values': ['', 'NA', 'N/A', 'null', 'NULL', 'None', 'NaN'],
        'low_memory': False
    },
    'excel': {
        'engine': 'openpyxl'
    },
    'parquet': {
        'engine': 'pyarrow'
    }
}

# Configurações de validação de dados
DATA_VALIDATION_CONFIG = {
    'max_missing_percentage': 0.5,  # Máximo 50% de valores ausentes
    'min_samples': 100,             # Mínimo 100 amostras
    'max_features': 1000,           # Máximo 1000 features
    'check_data_drift': True,       # Verificar deriva de dados
    'check_target_leakage': True    # Verificar vazamento de target
}

# =============================================================================
# CONFIGURAÇÕES DE EXPERIMENTOS
# =============================================================================

EXPERIMENT_CONFIG = {
    'tracking': {
        'use_mlflow': False,
        'experiment_name': 'ml_boilerplate',
        'auto_log': True
    },
    'model_versioning': {
        'save_all_models': True,
        'save_best_only': False,
        'model_registry': True
    },
    'reproducibility': {
        'set_random_seeds': True,
        'save_environment': True,
        'save_code_version': True
    }
}

# =============================================================================
# FUNÇÕES AUXILIARES
# =============================================================================
#TODO: criar diretórios NOTEBOOKS_DIR, SRC_DIR e TESTS_DIR caso não existam
#TODO: gerar código nos noteooks e código fonte automaticamente a partir dessas configurações
#TODO: adicionar configuração de logging para salvar logs em arquivo e console
def create_directories():
    """Cria todos os diretórios necessários para o projeto."""
    directories = [
        DATA_DIR, RAW_DATA_DIR, PROCESSED_DATA_DIR, 
        EXTERNAL_DATA_DIR, INTERIM_DATA_DIR,
        MODELS_DIR, REPORTS_DIR, FIGURES_DIR
    ]
    
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
    
    print("✅ Diretórios criados com sucesso!")

def get_model_config(model_type: str) -> Dict[str, Any]:
    """
    Retorna configuração de modelos para um tipo específico.
    
    Args:
        model_type (str): 'classification' ou 'regression'
    
    Returns:
        Dict[str, Any]: Configuração dos modelos
    """
    if model_type == 'classification':
        return CLASSIFICATION_MODELS
    elif model_type == 'regression':
        return REGRESSION_MODELS
    else:
        raise ValueError(f"Tipo de modelo inválido: {model_type}")

def get_metrics_config(problem_type: str) -> List[str]:
    """
    Retorna lista de métricas para um tipo de problema.
    
    Args:
        problem_type (str): 'classification' ou 'regression'
    
    Returns:
        List[str]: Lista de métricas
    """
    if problem_type == 'classification':
        return CLASSIFICATION_METRICS
    elif problem_type == 'regression':
        return REGRESSION_METRICS
    else:
        raise ValueError(f"Tipo de problema inválido: {problem_type}")

def setup_project_environment():
    """Configura ambiente completo do projeto."""
    # Criar diretórios
    create_directories()
    
    # Configurar seeds para reprodutibilidade
    if EXPERIMENT_CONFIG['reproducibility']['set_random_seeds']:
        import random
        import numpy as np
        random.seed(RANDOM_STATE)
        np.random.seed(RANDOM_STATE)
        
        try:
            import torch
            torch.manual_seed(RANDOM_STATE)
        except ImportError:
            # PyTorch not installed, skipping torch seed setup
            pass
    
    # Configurar matplotlib
    try:
        import matplotlib.pyplot as plt
        plt.style.use('default')
        plt.rcParams['figure.figsize'] = VISUALIZATION_CONFIG['figure_size']
        plt.rcParams['figure.dpi'] = VISUALIZATION_CONFIG['dpi']
    except ImportError:
        pass
    
    # Configurar seaborn
    try:
        import seaborn as sns
        sns.set_style(VISUALIZATION_CONFIG['style'])
        sns.set_palette(VISUALIZATION_CONFIG['palette'])
    except ImportError:
        pass
    
    print("🚀 Ambiente do projeto configurado com sucesso!")

if __name__ == "__main__":
    setup_project_environment()
    print("📋 Configurações carregadas!")
    print(f"📁 Diretório raiz do projeto: {PROJECT_ROOT}")
    print(f"🎯 Random state: {RANDOM_STATE}")
    print(f"🔧 Número de jobs: {N_JOBS}")