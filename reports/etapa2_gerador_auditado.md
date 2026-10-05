# ETAPA 2 — AUDITORIA DOS GERADORES (gera_lote1..7.py)

Gerado: 2026-10-04 03:09

## gera_lote1.py — linhas ['001', '002', '003', '004', '005', '006', '007', '008', '015', '023']
- Textos narrativos hardcoded (secoes: <p>...): **0 blocos**
- Lê dados-fonte/linhas.json? **SIM**
- Paradas 'Ponto NNNN' citadas no código: 27 únicas | presentes no GTFS oficial: 0
- Erros fatais REAIS (lista A) nas linhas deste lote: **5** (linhas afetadas: 001, 002, 004, 006, 007)

## gera_lote2.py — linhas ['025', '026', '027', '035', '041', '043', '045', '051', '053', '055']
- Textos narrativos hardcoded (secoes: <p>...): **0 blocos**
- Lê dados-fonte/linhas.json? **SIM**
- Paradas 'Ponto NNNN' citadas no código: 1 únicas | presentes no GTFS oficial: 0
- Erros fatais REAIS (lista A) nas linhas deste lote: **3** (linhas afetadas: 035, 041, 051)

## gera_lote3.py — linhas ['063', '065', '073', '075', '079', '085', '093', '095', '101', '102']
- Textos narrativos hardcoded (secoes: <p>...): **0 blocos**
- Lê dados-fonte/linhas.json? **SIM**
- Paradas 'Ponto NNNN' citadas no código: 8 únicas | presentes no GTFS oficial: 0
- Erros fatais REAIS (lista A) nas linhas deste lote: **2** (linhas afetadas: 085, 101)

## gera_lote4.py — linhas ['103', '104', '105', '106', '107', '108', '110', '130', '136', '147']
- Textos narrativos hardcoded (secoes: <p>...): **0 blocos**
- Lê dados-fonte/linhas.json? **SIM**
- Paradas 'Ponto NNNN' citadas no código: 19 únicas | presentes no GTFS oficial: 0
- Erros fatais REAIS (lista A) nas linhas deste lote: **6** (linhas afetadas: 103, 104, 105, 106, 107, 130)

## gera_lote5.py — linhas ['148', '156', '178', '187', '199', '201', '202', '203', '204']
- Textos narrativos hardcoded (secoes: <p>...): **0 blocos**
- Lê dados-fonte/linhas.json? **SIM**
- Paradas 'Ponto NNNN' citadas no código: 11 únicas | presentes no GTFS oficial: 0
- Erros fatais REAIS (lista A) nas linhas deste lote: **8** (linhas afetadas: 148, 156, 178, 187, 201, 202, 203, 204)

## gera_lote6.py — linhas ['205', '206', '207', '208', '210', '211', '217', '220', '236']
- Textos narrativos hardcoded (secoes: <p>...): **0 blocos**
- Lê dados-fonte/linhas.json? **SIM**
- Paradas 'Ponto NNNN' citadas no código: 2 únicas | presentes no GTFS oficial: 0
- Erros fatais REAIS (lista A) nas linhas deste lote: **7** (linhas afetadas: 205, 206, 208, 210, 211, 220, 236)

## gera_lote7.py — linhas ['256', '299', '301', '302', '305', '306', '308', '310', '311']
- Textos narrativos hardcoded (secoes: <p>...): **0 blocos**
- Lê dados-fonte/linhas.json? **SIM**
- Paradas 'Ponto NNNN' citadas no código: 0 únicas | presentes no GTFS oficial: 0
- Erros fatais REAIS (lista A) nas linhas deste lote: **8** (linhas afetadas: 256, 299, 301, 302, 305, 306, 310, 311)

## DIAGNÓSTICO DO PADRÃO
- Estrutura: **MISTA** (textos escritos à mão dentro de cada gera_loteN.py, sem extração de dados-fonte)
- Consequência: o texto cita vias/instituições por memória do gerador, não pelas paradas reais da linha → origem dos 76 erros reais (lista A) e das invenções (lista B)
- A correção (Ajuste 4 do Leo) proposta para a Etapa 3: narrar SOMENTE a partir de dados-fonte/linhas.json da própria linha (vias reais, bairros reais, grade real),
  com instituições permitidas apenas quando presentes em dados-fonte/pontos/.

*Sem proposta de correção codificada — aguardando aprovação (regra 1.20).*