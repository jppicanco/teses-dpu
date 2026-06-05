# Projeto BPC/LOAS — instruções do projeto

Apoio a Defensores Públicos em casos de BPC/LOAS (judicial e extrajudicial). Repositório **público**: https://github.com/jppicanco/projeto-bpc-loas

## Modo de operação
O defensor traz o **caso** (não o problema). O projeto **diagnostica**, identifica teses cabíveis, pede a documentação necessária e produz a peça (ofício, petição, recurso, inicial). Fluxo na seção 0 de `playbook/PLAYBOOK-LOAS.md`.

## ⚠️ Padrão de redação da peça (REGRA — não resumir)
Peça real é **completa, detalhada e minuciosa** — nunca enxuta. O exemplo curto não é o padrão. Sempre:
- **Fatos:** narrativa cronológica completa e específica do caso — datas, NB, DER/DIB/DCB, nº de despachos/protocolos, valores, composição familiar nominal, condições de saúde (CID, laudos, acompanhamento), gastos comprovados, canal de notificação. **Contar o caso a caso, não resumir.**
- **Direito:** desenvolver cada tese a fundo — fundamento legal + constitucional + **jurisprudência transcrita** (ementa/trecho oficial verificado, com nº do processo, relator, data) + **subsunção ao caso concreto** (aplicar a tese aos fatos daquele assistido, com o cálculo demonstrado da renda per capita).
- **Esgotar as teses cabíveis:** principal + subsidiárias + complementares (ver cenários do playbook); cumular quando o caso permitir.
- **Pedidos:** detalhados, ordenados (principal/subsidiário), com base legal de cada um.
- **Extensão proporcional à complexidade** — minúcia, não economia de argumentação. Linguagem técnica.
- Em peça real, **pedir ao defensor todos os dados** necessários para essa minúcia antes de redigir (ver checklist da seção 5 do playbook).

## Estrutura
- `playbook/` — playbook por cenário (C1–C14) + índice de material.
- `modelos/` — modelos de peça **anonimizados** (placeholders).
- `jurisprudencia/` — base de precedentes (texto oficial BNP/CJF).
- `skills/` — pipeline: anti-alucinação → formatação (DOCX+PDF) → checagem final.

## ⚠️ Regra inegociável — LGPD (repo público)
- **NUNCA** versionar dado pessoal (nome, CPF, NB, endereço de assistido), nem em arquivo, nem em nome de arquivo, nem em texto.
- `Material/` (peças reais), `saida/` (peças geradas) e `*_extr.txt` são **gitignored** — ficam locais.
- Ao incorporar material novo do usuário: extrair, **anonimizar** (placeholders), só então versionar.
- Antes de todo commit: `git status` + grep por CPF (`\d{3}\.\d{3}\.\d{3}-\d{2}`) e nomes próprios nos arquivos staged. Se achar, abortar e limpar.
- O template `skills/formatacao-docx/assets/template_dpu.docx` é letterhead institucional **sem** dado pessoal (corpo zerado, verificado).

## Pipeline de peça
1. Redigir a partir de `modelos/`.
2. `skills/anti-alucinacao` — validar origem de cada citação (na dúvida, remover).
3. `skills/formatacao-docx/formatar_peca.py` — gerar DOCX+PDF. Assinatura via env `FORMATAR_PECA_NOME`/`_CARGO`/`_LOCAL` (default = placeholder).
4. `skills/checagem-final/verificar_pdf.py` — checagem final.

## Jurisprudência sob demanda
MCPs de jurisprudência (BNP/CNJ, CJF) disponíveis para confirmar/atualizar teses. Toda citação específica precisa de origem rastreável (regra anti-alucinação).

## Commits
Branch `main`. Mensagens normais (não-caveman). Rodapé:
`Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>`
