# 🏛️ MEMÓRIA ESTRATÉGICA & HISTÓRICO COMPLETO — INFOHAUS TI

*Documento oficial de consolidação técnica, estratégica e comercial da marca.*  
*Localização: `C:\Users\lamacedo\Documents\Antigravity\Infohausti\MEMORIA_INFOHAUS.md`*  
*Data de Registro: 26/09/2026*  

---

## 📌 1. A MARCA & O FUNDADOR

* **Fundador:** Leonardo Macedo (Ribeirão Preto / SP).
* **Histórico da Marca:** Mais de 20 anos de estrada e vivência real em informática, redes, manutenção e infraestrutura.
* **Posicionamento:** A Infohaus TI é a marca guarda-chuva de tecnologia, presença digital de alta conversão e suporte prático descomplicado.
* **Propósito:** Transformar tecnologia em **faturamento e tranquilidade** para donos de clínicas médicas/odontológicas, escritórios e pequenas empresas, eliminando dores de cabeça operacionais.
* **Canais Oficiais:**
  * **Site Oficial:** [https://infohausti.com.br](https://infohausti.com.br)
  * **WhatsApp Business:** `+55 (16) 98146-9121`
  * **E-mail Corporativo:** `infohausti@gmail.com`
  * **GitHub:** [https://github.com/leomacedorp/infohausti](https://github.com/leomacedorp/infohausti)

---

## 🌐 2. ARQUITETURA DE INFRAESTRUTURA (CUSTO ZERO & ALTA ESCALA)

### Como o site está funcionando no ar hoje:
1. **Domínio:** Comprado no **Registro.br** (`infohausti.com.br`).
2. **DNS & Apontamento:** Configurado com registro tipo `A` apontando para o IP do GitHub Pages (`185.199.108.153`).
3. **Hospedagem Primária (Produção):** **GitHub Pages** (repositório público no branch `main` com arquivo `CNAME`).
   * **CDN Global:** Servido a partir dos servidores de borda (*Edge Pop*) de São Paulo (Fastly).
   * **Cadeado HTTPS / SSL:** Emitido e renovado automaticamente para sempre pela Let's Encrypt / GitHub.
   * **Custo Operacional:** **R$ 0,00**.
4. **Hospedagem Secundária (Backup Local na Oracle Cloud):**
   * Configurado na VM Always Free da Oracle (`praevisus-pro`, IP Tailscale `100.121.157.24`).
   * Servidor web **Nginx 1.24** ativo em `/var/www/infohausti` na porta 80 local com `certbot` instalado para contingência.

---

## 📚 3. GUIA TÉCNICO: GITHUB PAGES & CLOUDFLARE (POR QUE É UMA MINA DE OURO?)

### Hospedagem Tradicional vs. Hospedagem Moderna em Borda:
* **Tradicional (Hostgator, Locaweb, cPanel):** Uma máquina física ligada. Se o HD pifar, a memória esgotar ou sofrer ataque, o site cai. Você paga R$ 40 a R$ 100/mês por site.
* **GitHub Pages & Cloudflare Pages:**
  * **Sem servidor físico para você cuidar:** Arquivos estáticos (HTML, CSS, JS, imagens) são distribuídos em centenas de servidores pelo mundo.
  * **Velocidade Extrema:** O visitante baixa o site do data center mais próximo da casa dele (abertura em menos de 1 segundo).
  * **Segurança Absoluta:** Impossível de ser hackeado via invasão de servidor tradicional (não tem banco de dados local nem senhas de root expostas).
  * **Por que é gratuito?** Para a Microsoft (GitHub) e a Cloudflare, entregar HTML estático consome frações microscópicas de centavo. Eles fornecem isso de graça para atrair desenvolvedores.
* **A Estratégia de Negócios:**  
  * Você cobra do cliente **R$ 97 a R$ 197 / mês** de *"Gestão de Hospedagem, Segurança e Presença em Nuvem"*.
  * Você hospeda no GitHub Pages ou Cloudflare Pages.
  * O cliente tem a estabilidade do site de um grande banco (99.99% de uptime) e o seu custo de servidor é **R$ 0,00**.
  * **Margem de lucro: 100% líquida.**

---

## 🛡️ 4. O CATÁLOGO DE SERVIÇOS: "BAIXA DOR DE CABEÇA & ALTO LUCRO"

### A Decisão Estratégica Fundamental:
> **Decisão tomada pelo Leonardo:** Não assumir a responsabilidade por dados médicos críticos, hospedagem de prontuários ou recuperação de ataques complexos de ransomware. Isso gera estresse, risco desnecessário e chamados de madrugada. O foco é em **serviços previsíveis, de entrega rápida, alto valor percebido e zero insônia.**

### Os 4 Pilares Comerciais Oficiais:

#### 1. Criação de Sites & Landing Pages de Alta Conversão (Carro-Chefe)
* **Para quem é:** Médicos, dentistas, clínicas, advogados e empresas que não têm site ou têm páginas antigas que passam vergonha no celular.
* **O que entregamos:** Site moderno (layout dark tech ou clean premium), carregando em < 1s no celular, com botão de WhatsApp estratégico, domínio próprio `.com.br` e SSL.
* **Modelo de Cobrança:** R$ 1.000 a R$ 2.500 de taxa de criação (setup) + R$ 97 a R$ 197/mês de hospedagem e suporte básico.

#### 2. Presença no Google Maps & Busca Local (SEO Local)
* **Para quem é:** Empresas que querem aparecer para quem pesquisa no bairro ou na cidade (*"dentista ribeirão preto"*, *"clínica na zona sul"*).
* **O que entregamos:** Otimização completa do Google Perfil de Empresas (antigo Google Meu Negócio), integração de rotas no mapa, fotos de qualidade, horários corretos e botão de ligação rápida.
* **Dor de cabeça:** **Zero.** É serviço de configuração e posicionamento.

#### 3. Otimização de Computadores & Redes Wi-Fi (O Básico Bem Feito)
* **Para quem é:** Consultórios com máquinas da recepção travando, computadores lentos ou Wi-Fi instável.
* **O que entregamos:** Upgrades de SSD, formatação limpa do Windows (máquinas ligando em segundos), limpeza de programas pesados e vírus, e configuração de roteador Wi-Fi estável sem quedas.
* **Modelo de Cobrança:** Cobrança pontual por máquina/serviço ou contrato mensal de manutenção preventiva leve.

#### 4. Triagem Automática no WhatsApp (Motor Pulso Leve)
* **Para quem é:** Clínicas e escritórios que perdem clientes que mandam mensagem à noite ou aos fins de semana.
* **O que entregamos:** Rotina de mensagens automáticas no WhatsApp que responde horários, localização, serviços e faz a triagem inicial sem deixar ninguém no vácuo fora do expediente.

---

## 🎨 5. IDENTIDADE VISUAL & CONCEITO DE DESIGN

### A Marca e o Símbolo:
* **O Símbolo:** A **Casa de Circuitos Eletrônicos com o Chip `IH` central**.
  * *Haus* = Casa (em alemão).
  * O conceito representa: *"A casa que acolhe, protege e impulsiona a tecnologia do seu negócio"*.
  * O chip central representa o cérebro / processador de dados da empresa.
* **Paleta de Cores Oficial:**
  * **Dark Navy / Preto Profundo (`#02040a`, `#030712`):** Autoridade, sofisticação e posicionamento premium corporativo (estilo Vercel, Linear, Stripe).
  * **Ciano Elétrico & Sky Blue (`#00f0ff`, `#38bdf8`):** Energia, fibra óptica, nuvem, velocidade e inteligência moderna.
  * **Branco Puro (`#ffffff`):** Tipografia sólida, contraste absoluto e legibilidade impecável no mobile.
  * **Verde Esmeralda (`#10b981`):** Indicador de status *"Online / Sistemas operando sem falhas"*.
* **Tipografia:**
  * **`INFOHAUS`:** Caixa alta ultra-bold geométrica, sólida e encorpada.
  * **`TI`:** Em destaque ciano neon com brilho suave.
  * **Subtítulo:** *TECNOLOGIA & PRESENÇA DIGITAL*.
* **Efeitos Visuais Implementados:**
  * Fundo com animação dinâmica em **HTML5 Canvas** (trilhas de circuito impresso com nós de energia pulsando em tempo real).
  * Anéis orbitais tracejados em 3D girando suavemente ao redor do emblema.
  * Letreiro rolante contínuo (*ticker*) com os principais diferenciais da marca.

---

## 🏆 6. CASE OFICIAL DE PORTFÓLIO: OURO NAS ESTRELAS (ONE)

Para demonstrar capacidade técnica de engenharia web de alto nível sem expor assuntos internos de trabalho público, o portfólio oficial destaca o **Ouro nas Estrelas**:
* **O que é:** Plataforma web de alta escala com processamento de cálculos astronômicos e oraculares em tempo real.
* **Tecnologias desenvolvidas pela Infohaus TI:**
  * Frontend e backend modernos em **Next.js & TypeScript**.
  * Motor determinístico proprietário (Oráculo) de altíssima velocidade.
  * Integração de checkout de pagamentos digitais com **Stripe**.
  * Pontuação máxima de performance (100% no Google Core Web Vitals).
* **Função no Site:** Mostrar para qualquer cliente que a Infohaus TI não faz apenas "páginas simples", mas domina engenharia web de ponta.

---

## 💡 7. O MOTOR PULSO (A SEMENTE DO FUTURO)

* **O que é o Pulso:** Motor de atendimento conversacional determinístico criado no início do ecossistema ONE (localizado em `c:\Users\lamacedo\Documents\Antigravity\Pulso`).
* **Princípio Soberano:** **Custo zero de token por padrão.**
  * Detecção de intenção por palavras-chave com normalização de texto (`detectIntent.ts`).
  * Interpolação de templates dinâmicos (`renderTemplate.ts`).
  * Respostas em **5 milissegundos**, sem risco de alucinação e sem contas caras de OpenAI.
* **Potencial Comercial:** Pode ser empacotado como um **widget web flutuante** para sites de clientes ou conectado ao WhatsApp de empresas parceiras.

---

## 📈 8. A MATEMÁTICA DA LIBERDADE FINANCEIRA (METAS REAIS)

* **Realidade Atual:** Bicos noturnos de segurança extremamente desgastantes (plantões das 22h às 06h por R$ 110,00).
* **A Equivalência de Negócios:**
  * **1 Cliente de Hospedagem/Suporte da Infohaus (R$ 150/mês):** Paga mais do que uma noite inteira de bico no frio.
  * **10 Clientes Ativos:** **R$ 1.500,00 / mês** recorrentes no piloto automático (elimina mais de 13 noites de plantão).
  * **25 Clientes Ativos:** **R$ 3.750,00 / mês** recorrentes e limpos (elimina completamente a necessidade de bicos, devolvendo o sono, o descanso e a saúde).

---

*Registro consolidado por Leonardo Macedo & Antigravity.*  
*Infohaus TI — Tecnologia que vira faturamento, não dor de cabeça.*
