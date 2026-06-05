# Teses DPU — instruções globais do projeto

Monorepo de apoio a Defensores Públicos: cada **área** do direito fica em `areas/<area>/`, e o que é reaproveitável fica em `comum/`. Repositório **público**: https://github.com/jppicanco/teses-dpu

## Arquitetura
```
comum/                      Reaproveitável por todas as áreas
  skills/                   anti-alucinacao · formatacao-docx · checagem-final
  modelos-base/             blocos genéricos (gratuidade, prerrogativas, tutela)
areas/
  bpc-loas/                 1ª área (BPC/LOAS) — playbook, modelos, jurisprudência, CLAUDE.md próprio
  <nova-area>/              mesma estrutura
```
Cada área tem seu próprio `CLAUDE.md` (regras específicas) que **complementa** estas regras globais.

## ⚠️ Regra inegociável — LGPD (repo público)
- **NUNCA** versionar dado pessoal (nome, CPF, NB, endereço de assistido) — nem em arquivo, nem em nome de arquivo, nem em texto.
- `**/Material/` (peças reais), `saida/` (peças geradas) e `*_extr.txt` são **gitignored** — ficam locais.
- Material novo do usuário: extrair → **anonimizar** (placeholders) → só então versionar.
- Antes de todo commit: `git status` + grep por CPF (`\d{3}\.\d{3}\.\d{3}-\d{2}`) e nomes próprios nos arquivos staged. Achou → abortar e limpar.

## ⚠️ Padrão de redação da peça (REGRA — não resumir)
Peça real é **completa, detalhada e minuciosa** — nunca enxuta. Sempre:
- **Fatos:** narrativa cronológica completa e específica (datas, nº de benefício/processo, despachos, valores, composição familiar nominal, condições de saúde/CID/laudos, gastos comprovados, canal de notificação). Contar o caso a caso.
- **Direito:** cada tese a fundo — lei + Constituição + **jurisprudência transcrita** (processo, relator, data) + **subsunção ao caso concreto** com cálculo demonstrado.
- **Esgotar teses** (principal + subsidiárias + complementares); pedidos detalhados e ordenados.
- Os modelos são **esqueleto** — devem ser expandidos com a minúcia do caso, não copiados enxutos.

## Pipeline de produção (vale para todas as áreas)
1. Redigir a partir dos modelos da área + blocos de `comum/modelos-base/`.
2. `comum/skills/anti-alucinacao` — validar origem de cada citação (na dúvida, remover).
3. `comum/skills/formatacao-docx/formatar_peca.py` — gerar DOCX+PDF. Assinatura via env `FORMATAR_PECA_NOME`/`_CARGO`/`_LOCAL` (default = placeholder).
4. `comum/skills/checagem-final/verificar_pdf.py` — checagem final.

## Como adicionar uma nova área
1. Criar `areas/<nova-area>/` com `playbook/`, `modelos/`, `jurisprudencia/` e um `CLAUDE.md` próprio.
2. Reusar `comum/skills/` e `comum/modelos-base/` (não duplicar).
3. Atualizar a tabela de áreas no `README.md` raiz.

## Jurisprudência sob demanda
MCPs de jurisprudência (BNP/CNJ, CJF) disponíveis para confirmar/atualizar teses. Toda citação específica precisa de origem rastreável (regra anti-alucinação).

## Commits
Branch `main`. Mensagens normais (não-caveman). Rodapé:
`Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>`
