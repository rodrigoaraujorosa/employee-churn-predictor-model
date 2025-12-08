# Makefile para ML Boilerplate
# Facilita comandos comuns de desenvolvimento

# Variáveis
PYTHON = python
PIP = pip
VENV = venv
JUPYTER = jupyter

# Cores para output
GREEN = \033[0;32m
YELLOW = \033[1;33m
RED = \033[0;31m
NC = \033[0m # No Color

.PHONY: help install install-dev setup test clean lint format jupyter example

# Help
help:
	@echo "$(GREEN)ML Boilerplate - Comandos Disponíveis:$(NC)"
	@echo ""
	@echo "  $(YELLOW)setup$(NC)         - Configuração completa do projeto (venv + dependências)"
	@echo "  $(YELLOW)install$(NC)       - Instalar dependências de produção"
	@echo "  $(YELLOW)install-dev$(NC)   - Instalar dependências de desenvolvimento"
	@echo "  $(YELLOW)test$(NC)          - Executar testes"
	@echo "  $(YELLOW)lint$(NC)          - Verificar qualidade do código"
	@echo "  $(YELLOW)format$(NC)        - Formatar código automaticamente"
	@echo "  $(YELLOW)jupyter$(NC)       - Iniciar Jupyter Lab"
	@echo "  $(YELLOW)example$(NC)       - Executar exemplo de uso"
	@echo "  $(YELLOW)clean$(NC)         - Limpar arquivos temporários"
	@echo ""

# Configuração completa
setup: create-venv install install-dev setup-project
	@echo "$(GREEN)✅ Projeto configurado com sucesso!$(NC)"
	@echo "$(YELLOW)💡 Para ativar o ambiente virtual:$(NC)"
ifeq ($(OS),Windows_NT)
	@echo "    $(VENV)\\Scripts\\activate"
else
	@echo "    source $(VENV)/bin/activate"
endif
	@echo "$(YELLOW)🚀 Para iniciar Jupyter:$(NC) make jupyter"

# Criar ambiente virtual
create-venv:
	@echo "$(GREEN)🔧 Criando ambiente virtual...$(NC)"
	$(PYTHON) -m venv $(VENV)
	@echo "$(GREEN)✅ Ambiente virtual criado!$(NC)"

# Instalar dependências de produção
install:
	@echo "$(GREEN)📦 Instalando dependências...$(NC)"
ifeq ($(OS),Windows_NT)
	$(VENV)\\Scripts\\pip install -r requirements.txt
else
	./$(VENV)/bin/pip install -r requirements.txt
endif
	@echo "$(GREEN)✅ Dependências instaladas!$(NC)"

# Instalar dependências de desenvolvimento
install-dev:
	@echo "$(GREEN)🛠️ Instalando dependências de desenvolvimento...$(NC)"
ifeq ($(OS),Windows_NT)
	$(VENV)\\Scripts\\pip install -r requirements-dev.txt
else
	./$(VENV)/bin/pip install -r requirements-dev.txt
endif
	@echo "$(GREEN)✅ Dependências de desenvolvimento instaladas!$(NC)"

# Configurar projeto
setup-project:
	@echo "$(GREEN)⚙️ Configurando projeto...$(NC)"
ifeq ($(OS),Windows_NT)
	$(VENV)\\Scripts\\python config/settings.py
else
	./$(VENV)/bin/python config/settings.py
endif

# Executar testes
test:
	@echo "$(GREEN)🧪 Executando testes...$(NC)"
ifeq ($(OS),Windows_NT)
	$(VENV)\\Scripts\\pytest tests/ -v
else
	./$(VENV)/bin/pytest tests/ -v
endif

# Verificar qualidade do código
lint:
	@echo "$(GREEN)🔍 Verificando qualidade do código...$(NC)"
ifeq ($(OS),Windows_NT)
	$(VENV)\\Scripts\\flake8 src/
	$(VENV)\\Scripts\\mypy src/
else
	./$(VENV)/bin/flake8 src/
	./$(VENV)/bin/mypy src/
endif

# Formatar código
format:
	@echo "$(GREEN)🎨 Formatando código...$(NC)"
ifeq ($(OS),Windows_NT)
	$(VENV)\\Scripts\\black src/ tests/
	$(VENV)\\Scripts\\isort src/ tests/
else
	./$(VENV)/bin/black src/ tests/
	./$(VENV)/bin/isort src/ tests/
endif
	@echo "$(GREEN)✅ Código formatado!$(NC)"

# Iniciar Jupyter Lab
jupyter:
	@echo "$(GREEN)🚀 Iniciando Jupyter Lab...$(NC)"
ifeq ($(OS),Windows_NT)
	$(VENV)\\Scripts\\jupyter lab
else
	./$(VENV)/bin/jupyter lab
endif

# Executar exemplo
example:
	@echo "$(GREEN)🎯 Executando exemplo de uso...$(NC)"
ifeq ($(OS),Windows_NT)
	$(VENV)\\Scripts\\python example_usage.py
else
	./$(VENV)/bin/python example_usage.py
endif

# Limpar arquivos temporários
clean:
	@echo "$(GREEN)🧹 Limpando arquivos temporários...$(NC)"
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type d -name "__pycache__" -delete 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name ".coverage" -delete 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	@echo "$(GREEN)✅ Limpeza concluída!$(NC)"

# Instalar em modo desenvolvimento
install-editable:
	@echo "$(GREEN)🔧 Instalando em modo desenvolvimento...$(NC)"
ifeq ($(OS),Windows_NT)
	$(VENV)\\Scripts\\pip install -e .
else
	./$(VENV)/bin/pip install -e .
endif

# Criar distribuição
build:
	@echo "$(GREEN)📦 Criando distribuição...$(NC)"
ifeq ($(OS),Windows_NT)
	$(VENV)\\Scripts\\python setup.py sdist bdist_wheel
else
	./$(VENV)/bin/python setup.py sdist bdist_wheel
endif

# Verificar dependências
check-deps:
	@echo "$(GREEN)🔍 Verificando dependências...$(NC)"
ifeq ($(OS),Windows_NT)
	$(VENV)\\Scripts\\pip list --outdated
else
	./$(VENV)/bin/pip list --outdated
endif

# Atualizar dependências
update-deps:
	@echo "$(GREEN)⬆️ Atualizando dependências...$(NC)"
ifeq ($(OS),Windows_NT)
	$(VENV)\\Scripts\\pip install --upgrade pip
	$(VENV)\\Scripts\\pip install --upgrade -r requirements.txt
else
	./$(VENV)/bin/pip install --upgrade pip
	./$(VENV)/bin/pip install --upgrade -r requirements.txt
endif