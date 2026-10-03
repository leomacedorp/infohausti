# 🏛️ Infohausti RP — Portal da Cidade Digital (Ribeirão Vivo)

Infraestrutura digital de informação cívica, mobilidade urbana, patrimônio histórico, serviços públicos e dados de **Ribeirão Preto - SP**.

---

## 🎯 Visão do Projeto
O portal conecta moradores, turistas, estudantes e empreendedores a informações 100% verificadas, com rotas completas de ônibus integradas, fichas culturais profundas e transparência de dados públicos.

- **URL de Produção:** [https://infohausti.com.br](https://infohausti.com.br)
- **Plano Mestre:** v4 (Manual de Execução em Blocos v1.2)
- **Canal de Correções e Contato:** `infohausti@gmail.com`

---

## 🏗️ Arquitetura do Sistema
O portal adota geração orientada a dados:
1. **Dados Verificados (`content/dados-fonte/`):** Nenhum fato é inferido ou inventado; todas as informações contam com fonte primária citada e data de verificação.
2. **Motor de Compilação (`scripts/build.py`):** Constrói as ~200 páginas HTML a partir de modelos Jinja2 sem dependência de frameworks pesados de frontend.
3. **Pipeline de Auditoria (`scripts/audit_all.py`):** Roda checagens automáticas de links, acessibilidade WCAG 2.1 AA, validade de Schema.org JSON-LD e similaridade máxima de 30% em texto narrativo antes de qualquer publicação.
4. **Acervo Legado (`legado/`):** Preserva versões anteriores e páginas auditadas no modelo inicial.

---

## 📁 Estrutura de Pastas

```text
infohausti-rp/
├── EXECUCAO.md             # Manual de execução em blocos
├── README.md               # Este arquivo
├── PENDENCIAS.md           # Fila de insumos e dados sob checagem
├── LOG.md                  # Registro de execuções
├── content/
│   ├── config.json         # Configurações de domínio e e-mails
│   ├── autor.json          # Bio e créditos E-E-A-T do autor
│   ├── lista-mestre.json   # Slugs e entidades oficiais
│   ├── status.json         # Status de compilação de cada página
│   ├── correcoes.json      # Erros e correções rastreadas
│   ├── dados-fonte/        # Dados JSON puros e verificados
│   └── paginas/            # Conteúdos editoriais estruturados
├── templates/              # Modelos Jinja2 (ponto, linha, bairro, serviço...)
├── partials/               # Componentes reutilizáveis (nav, footer, ads...)
├── assets/
│   ├── css/                # CSS puro otimizado
│   ├── js/                 # Scripts leves (menu, LGPD)
│   └── img/                # Imagens com licenciamento documentado
├── scripts/                # Gerador e ferramentas de auditoria
├── reports/                # Relatórios de checagem e revisões
├── legado/                 # Histórico das primeiras páginas publicadas
└── dist/                   # Saída compilada pronta para hospedagem
```

---

## 🛡️ Diretrizes Editoriais
- **E-E-A-T:** Identificação clara de autoria e metodologia de curadoria.
- **Microdados:** Schema.org (`TouristAttraction`, `BusTrip`, `CollectionPage`, `FAQPage`) em todas as páginas.
- **Monetização Separada:** Conteúdo público e histórico é estritamente editorial; estabelecimentos privados e anúncios são tratados exclusivamente via patrocínio e AdSense.