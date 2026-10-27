#!/usr/bin/env bash
# =====================================================================
# Script de Inicialização da API do Scanner - Infohaus TI (Oracle VM)
# =====================================================================

set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

echo "=== INFOHAUS TI: INICIANDO SCANNER API ==="

# Verifica se o ambiente virtual existe, se não cria
if [ ! -d "venv" ]; then
    echo "Criando ambiente virtual Python..."
    python3 -m venv venv
fi

# Ativa o venv e instala/atualiza dependências
source venv/bin/activate
echo "Instalando dependências..."
pip install --upgrade pip
pip install -r requirements.txt

# Para instâncias anteriores na porta 8000 se houver
PID=$(lsof -t -i:8000 || true)
if [ -n "$PID" ]; then
    echo "Encerrando processo anterior na porta 8000 (PID: $PID)..."
    kill -9 "$PID" || true
fi

# Inicia a API com nohup em segundo plano
echo "Subindo o servidor Uvicorn na porta 8000..."
nohup python3 scanner_api.py > scanner_api.log 2>&1 &

sleep 2

# Testa se respondeu
if curl -s http://localhost:8000/health | grep -q "healthy"; then
    echo "✅ SUCESSO! A Scanner API está online e respondendo em http://localhost:8000"
    echo "Logs disponíveis em: $DIR/scanner_api.log"
else
    echo "⚠️ Verifique os logs em scanner_api.log para detalhes."
fi
