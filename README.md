# 🏛️ Infohaus TI — Tecnologia, Presença Digital & Suporte Descomplicado

Repositório oficial do site institucional e das páginas comerciais da **Infohaus TI**.

- **URL de Produção:** [https://infohausti.com.br](https://infohausti.com.br)
- **Fundador:** Leonardo Macedo (Ribeirão Preto / SP)
- **Contato / WhatsApp:** `+55 (16) 98146-9121`
- **E-mail:** `infohausti@gmail.com`

---

## 🎯 Sobre a Marca
A Infohaus TI é a marca guarda-chuva de tecnologia, desenvolvimento web e suporte corporativo de Leonardo Macedo, voltada para transformar tecnologia em faturamento e tranquilidade para clínicas médicas, consultórios odontológicos, escritórios e pequenas empresas.

---

## 📁 Estrutura do Repositório

```text
Infohausti/
├── index.html                 # Landing page oficial da marca Infohaus TI
├── 404.html                   # Página de erro 404 customizada
├── perfil-google/             # Landing page de vendas: Otimização de Perfil no Google (GMN)
│   ├── index.html
│   └── og.jpg                 # Banner 1200x630 para prévia no WhatsApp
├── content/
│   └── artigos/               # Artigos e guias comerciais
│       └── gmn-ribeirao-preto.md
├── scripts/
│   ├── gera_og_image.ps1      # Gerador do banner OpenGraph em alta resolução
│   └── salva_perfil_google.py # Script de utilidade
├── MEMORIA_INFOHAUS.md        # Documento mestre de estratégia comercial e modelo de negócio
├── STATUS.md                  # Status operacional
├── CNAME                      # Apontamento de domínio no GitHub Pages
├── sitemap.xml                # Mapa do site oficial
├── robots.txt                 # Diretrizes para indexadores
└── logo.jpg / og-image.jpg    # Identidade visual da marca
```

---

## 🌐 Hospedagem & Infraestrutura
- **Servidor Primário:** GitHub Pages servido via CDN Fastly (Edge SP) com SSL HTTPS automático Let's Encrypt (Custo: R$ 0,00).
- **Servidor Secundário:** Nginx na Oracle Cloud VM (`praevisus-pro`) para contingência.