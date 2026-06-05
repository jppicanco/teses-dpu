# Teses DPU

Coleção de projetos de apoio a **Defensores Públicos**, organizada por **área do direito**. Cada área reúne playbook por cenário, modelos de peça anonimizados e base jurisprudencial; a infraestrutura comum (skills de validação e formatação, blocos genéricos) é compartilhada por todas.

> Material de apoio técnico-jurídico. Não substitui a análise do caso concreto pelo(a) Defensor(a) responsável.

## Áreas disponíveis

| Área | Pasta | Cobertura |
|---|---|---|
| **BPC/LOAS** | [`areas/bpc-loas/`](areas/bpc-loas/) | Benefício de Prestação Continuada — concessão, revisão, suspensão, cessação e recursos (judicial e extrajudicial). 14 cenários, 10 modelos, base STF/STJ/TNU. Foco no Decreto 12.534/2025. |
| _(próximas)_ | `areas/<area>/` | aposentadoria rural, auxílio por incapacidade, etc. |

## Infraestrutura comum

| Pasta | O que é |
|---|---|
| [`comum/skills/`](comum/skills/) | Pipeline: **anti-alucinação** (valida origem de citações) → **formatação** (gera DOCX+PDF institucional) → **checagem final** (verifica o PDF). Usado por todas as áreas. |
| [`comum/modelos-base/`](comum/modelos-base/) | Blocos genéricos de peça (gratuidade, prerrogativas DPU, prioridade, tutela de urgência). |

## Como usar
1. Entre na área do seu caso (ex.: [`areas/bpc-loas/`](areas/bpc-loas/)) e leia o playbook.
2. Identifique o cenário, pegue o modelo e expanda com os dados do caso (peça **completa e minuciosa**).
3. Rode o pipeline de `comum/skills/` para validar e gerar DOCX+PDF.

```bash
pip install -r comum/skills/formatacao-docx/requirements.txt
export FORMATAR_PECA_NOME="Seu Nome"   # cada defensor configura a sua assinatura
```

## Como adicionar uma nova área
1. Crie `areas/<nova-area>/` com `playbook/`, `modelos/`, `jurisprudencia/` e um `CLAUDE.md` próprio.
2. Reuse `comum/skills/` e `comum/modelos-base/` — não duplique.
3. Adicione a área à tabela acima.

## Privacidade (LGPD)
Repositório público, **sem dados pessoais**. Peças reais ficam locais (`**/Material/`, gitignored); modelos são anonimizados (placeholders). Saída gerada (`saida/`) é gitignored. Detalhes e regras em [`CLAUDE.md`](CLAUDE.md).

## Licença
[CC BY 4.0](LICENSE) — uso e adaptação livres, com atribuição.
