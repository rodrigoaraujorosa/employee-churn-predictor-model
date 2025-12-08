#!/bin/bash
# Script de configuração para Linux/Mac

echo "🚀 Configurando ML Boilerplate para Linux/Mac..."

# Verificar se Python >= 3.12 está instalado
python_version=$(python3 --version 2>&1 | grep -o '[0-9]\+\.[0-9]\+' | head -1)
major_version=$(echo $python_version | cut -d. -f1)
minor_version=$(echo $python_version | cut -d. -f2)

if [[ $major_version -lt 3 ]] || [[ $major_version -eq 3 && $minor_version -lt 12 ]]; then
    echo "❌ Python 3.12+ é necessário. Versão atual: $python_version"
    exit 1
fi

echo "✅ Python $python_version encontrado"

# Criar ambiente virtual
echo "🔧 Criando ambiente virtual..."
python3 -m venv venv

# Ativar ambiente virtual
echo "🔌 Ativando ambiente virtual..."
source venv/Scripts/activate

# Atualizar pip
echo "⬆️ Atualizando pip..."
pip install --upgrade pip

# Instalar dependências
echo "📦 Instalando dependências..."
pip install -r requirements.txt

# Instalar dependências de desenvolvimento
echo "🛠️ Instalando dependências de desenvolvimento..."
pip install -r requirements-dev.txt

# Configurar projeto
echo "⚙️ Configurando projeto..."
python config/settings.py

echo ""
echo "🎉 Configuração concluída com sucesso!"
echo ""
echo "Para usar o projeto:"
echo "1. Ativar o ambiente virtual: source venv/bin/activate"
echo "2. Iniciar Jupyter: jupyter lab"
echo "3. Ou executar exemplo: python example_usage.py"
echo ""
echo "Comandos úteis:"
echo "- make help          # Ver todos os comandos"
echo "- make jupyter       # Iniciar Jupyter Lab"
echo "- make test          # Executar testes"
echo "- make format        # Formatar código"
echo "