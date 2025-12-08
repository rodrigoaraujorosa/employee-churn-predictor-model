"""
Módulo de configuração para o ML Boilerplate.
"""

from .settings import *

__all__ = [
    'PROJECT_ROOT', 'DATA_DIR', 'MODELS_DIR', 'REPORTS_DIR',
    'RANDOM_STATE', 'TEST_SIZE', 'CV_FOLDS',
    'CLASSIFICATION_MODELS', 'REGRESSION_MODELS',
    'VISUALIZATION_CONFIG', 'PLOTLY_CONFIG',
    'setup_project_environment', 'create_directories',
    'get_model_config', 'get_metrics_config'
]