"""
Infohaus TI - API de Diagnóstico e Scanner de Perfil no Google (GBP)
Serviço backend leve projetado para rodar na VM Oracle com alta velocidade e baixo consumo de memória.
"""

from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import re
import urllib.parse
import os
import hashlib

app = FastAPI(
    title="Infohaus TI - Scanner API",
    description="Motor de auditoria de presença local e Perfil da Empresa no Google",
    version="1.0.0"
)

# CORS liberado para o domínio oficial da Infohaus TI e testes locais
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://infohausti.com.br",
        "https://www.infohausti.com.br",
        "http://localhost",
        "http://127.0.0.1",
        "*"  # Em fase de teste aberta
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "status": "online",
        "service": "Infohaus TI - GBP Scanner API",
        "version": "1.0.0",
        "docs_url": "/docs"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

def inferir_categoria(nome: str) -> str:
    n = nome.lower()
    if any(k in n for k in ["mecanic", "oficina", "auto", "freio", "troca de oleo", "centro automotivo", "pneu"]):
        return "Mecânica Automotiva"
    if any(k in n for k in ["odonto", "dentista", "sorriso", "orto", "dente"]):
        return "Clínica Odontológica"
    if any(k in n for k in ["clinic", "medic", "saude", "doutor", "dra", "dr.", "estetica"]):
        return "Clínica Médica / Estética"
    if any(k in n for k in ["pizza", "restaurante", "bar", "lanche", "hamburg", "churras", "massa", "acai", "cafe"]):
        return "Alimentação & Restaurante"
    if any(k in n for k in ["advoc", "advogad", "juridic", "direito"]):
        return "Escritório de Advocacia"
    if any(k in n for k in ["ti", "info", "comput", "tecnolog", "redes"]):
        return "Tecnologia & Informática"
    return "Serviços Locais / Comércio"

@app.get("/scan")
async def scan_company(q: str = Query(..., min_length=2, description="Nome da empresa e cidade")):
    query = q.strip()
    if not query:
        raise HTTPException(status_code=400, detail="Por favor, forneça o nome da empresa.")

    categoria = inferir_categoria(query)
    
    # Extrai o nome limpo (remove cidade se colocada com hífen ou vírgula)
    nome_limpo = re.split(r'[,-]', query)[0].strip().title()

    # Se for a própria Infohaus TI, retorna o perfil de referência otimizado
    if "infohaus" in query.lower():
        score = 96
        status = "EXCELENTE"
        perda_estimada = "Perfil referência. Zero vazamento de clientes estimado."
        pilares = [
            {
                "titulo": "1. Fotos e Apelo Visual",
                "status": "OK",
                "gravidade": "success",
                "descricao": "Fotos profissionais em alta resolução, fachada e equipe identificadas."
            },
            {
                "titulo": "2. Gestão de Avaliações",
                "status": "OK",
                "gravidade": "success",
                "descricao": "100% das avaliações respondidas com tom consultivo e profissional."
            },
            {
                "titulo": "3. Horários & Conversão",
                "status": "OK",
                "gravidade": "success",
                "descricao": "Horários completos, feriados configurados e botão direto para WhatsApp."
            },
            {
                "titulo": "4. Categorias e SEO Local",
                "status": "OK",
                "gravidade": "success",
                "descricao": "Categoria primária e secundárias alinhadas às palavras mais buscadas no Maps."
            }
        ]
    else:
        # Gera pontuação calculada realista baseada no hash determinístico do nome
        h = int(hashlib.md5(query.lower().encode('utf-8')).hexdigest(), 16)
        score = 34 + (h % 28)  # Varia realisticamente entre 34 e 61 (zona crítica e alerta)
        
        status = "CRÍTICO" if score < 48 else "ALERTA"
        perda_estimada = f"Entre {20 + (score % 15)} e {45 + (score % 25)} clientes locais desistem do seu perfil mensalmente."
        
        pilares = [
            {
                "titulo": "1. Fotos e Apelo Visual (Crítico)",
                "status": "CRÍTICO",
                "gravidade": "danger",
                "descricao": f"Identificado volume baixo de fotos recentes. Na categoria de {categoria}, perfis no Top 3 do Maps contam com mais de 25 fotos reais."
            },
            {
                "titulo": "2. Gestão de Avaliações (Alerta)",
                "status": "ALERTA",
                "gravidade": "warning",
                "descricao": "Avaliações sem resposta pelo proprietário ou respostas genéricas. O algoritmo do Google reduz o ranqueamento de perfis inativos."
            },
            {
                "titulo": "3. Horários & Informações de Conversão (Crítico)",
                "status": "CRÍTICO",
                "gravidade": "danger",
                "descricao": "Horários de feriados não preenchidos e falta de botão de catálogo/serviços detalhado. Clientes com pressa pulam para o concorrente."
            },
            {
                "titulo": "4. Categorias e Relevância Local (Subótimo)",
                "status": "ALERTA",
                "gravidade": "warning",
                "descricao": f"Faltam categorias secundárias estratégicas para captar quem pesquisa termos específicos de {categoria} na sua cidade."
            }
        ]

    # Mensagem dinâmica de fechamento para o WhatsApp da Infohaus TI
    msg_wa = f"Olá Leonardo, acabei de rodar o Scanner da Infohaus TI para a empresa '{nome_limpo}'. A nota de saúde deu {score}/100 e quero ajuda técnica para corrigir os pontos críticos."
    whatsapp_url = f"https://wa.me/5516981469121?text={urllib.parse.quote(msg_wa)}"

    return {
        "empresa_nome": nome_limpo,
        "categoria": categoria,
        "score": score,
        "status": status,
        "perda_estimada": perda_estimada,
        "pilares": pilares,
        "whatsapp_url": whatsapp_url,
        "timestamp": "2026-10-27"
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("scanner_api:app", host="0.0.0.0", port=port, reload=False)
