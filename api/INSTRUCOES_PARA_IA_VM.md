# 🤖 INSTRUÇÕES DE EXECUÇÃO PARA A IA / OPERADOR NA VM ORACLE (`praevisus-pro`)

Este documento contém os passos diretos para colocar a **API do Scanner de Perfil no Google (GBP)** rodando na porta `8000`.

---

## 🚀 PASSO 1: Sincronizar o Repositório Git

No terminal da VM (ou via console/Hermes), execute:

```bash
cd /var/www/infohausti
git pull origin main
```

*(Se o repositório estiver em outra pasta na home, ajuste o `cd` para a pasta onde o `infohausti` está clonado).*

---

## ⚡ PASSO 2: Iniciar a API com 1 Comando

Entre na pasta `api` e execute o script automático:

```bash
cd /var/www/infohausti/api
chmod +x start.sh
./start.sh
```

O script vai:
1. Criar o `venv` Python isolado automaticamente;
2. Instalar `fastapi` e `uvicorn`;
3. Iniciar o serviço em segundo plano na porta `8000`;
4. Fazer o teste de saúde (`health check`).

---

## 🧪 PASSO 3: Testar Localmente na VM

Para confirmar que a API está calculando e respondendo em tempo real:

```bash
curl "http://localhost:8000/scan?q=Oficina+Mecanica+do+Ze+Ribeirao+Preto"
```

A saída esperada deve ser um JSON com `score`, `status`, `categoria`, `pilares` e o `whatsapp_url`.

---

## 🌐 PASSO 4: Roteamento Cloudflare (Opcional se Cloudflared estiver ativo)

Se o `cloudflared` já estiver rodando na VM para expor a rota pública `api.infohausti.com.br`:
- Basta mapear o serviço `api.infohausti.com.br` para `http://localhost:8000` no painel Cloudflare Zero Trust > Tunnels.
- Ou, se estiver usando Nginx como proxy reverso local, adicionar o bloco:
  ```nginx
  location /api/ {
      proxy_pass http://127.0.0.1:8000/;
      proxy_set_header Host $host;
      proxy_set_header X-Real-IP $remote_addr;
  }
  ```

---

## 📋 Comandos de Manutenção:
- **Ver os logs em tempo real:**
  ```bash
  tail -f /var/www/infohausti/api/scanner_api.log
  ```
- **Verificar se está rodando:**
  ```bash
  ps aux | grep scanner_api
  ```
- **Parar o serviço:**
  ```bash
  pkill -f scanner_api.py
  ```
