@echo off
REM Script de configuração para Windows

echo 🚀 Configurando ML Boilerplate para Windows...

REM Verificar se Python >= 3.12 está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python não encontrado. Instale Python 3.12+ primeiro.
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version') do set python_version=%%i
echo ✅ Python %python_version% encontrado

REM Criar ambiente virtual
echo 🔧 Criando ambiente virtual...
python -m venv venv

REM Ativar ambiente virtual
echo 🔌 Ativando ambiente virtual...
call venv\Scripts\activate

REM Atualizar pip
echo ⬆️ Atualizando pip...
python -m pip install --upgrade pip

REM Instalar dependências
echo 📦 Instalando dependências...
pip install -r requirements.txt

REM Instalar dependências de desenvolvimento
echo 🛠️ Instalando dependências de desenvolvimento...
pip install -r requirements-dev.txt

REM Configurar projeto
echo ⚙️ Configurando projeto...
python config/settings.py

echo.
echo 🎉 Configuração concluída com sucesso!
echo.
echo Para usar o projeto:
echo 1. Ativar o ambiente virtual: venv\Scripts\activate
echo 2. Iniciar Jupyter: jupyter lab
echo 3. Ou executar exemplo: python example_usage.py
echo.
echo Comandos úteis (se tiver make instalado):
echo - make help          # Ver todos os comandos
echo - make jupyter       # Iniciar Jupyter Lab
echo - make test          # Executar testes
echo - make format        # Formatar código
echo.

pause