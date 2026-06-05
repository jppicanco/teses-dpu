# Skills — pipeline de produção de peças

Conjunto de skills que pega a peça redigida (a partir do [playbook](../playbook/PLAYBOOK-LOAS.md) e dos [modelos](../modelos/)) e a entrega **validada e formatada em DOCX + PDF**.

## Pipeline

```
Redação da peça (markdown, a partir de modelos/)
        ↓
1. anti-alucinacao/       → valida origem de TODA citação; remove/generaliza o que não tem fonte
        ↓
2. formatacao-docx/       → gera DOCX + PDF com layout institucional (formatar_peca.py)
        ↓
3. checagem-final/        → checklist + verificador de PDF (páginas, acentos, assinatura)
```

| Skill | Pasta | O que faz |
|---|---|---|
| Anti-alucinação | [`anti-alucinacao/`](anti-alucinacao/SKILL.md) | Verifica se cada citação (processo, súmula, tema, relator, trecho) veio de fonte confiável (PDF do processo, MCP BNP/CJF, base verificada, legislação). Sem origem → remove ou generaliza. **Na dúvida, remove.** |
| Formatação | [`formatacao-docx/`](formatacao-docx/SKILL.md) | Converte texto estruturado (`##`, `###`, `>`) em DOCX + PDF com cabeçalho, barra lateral (pedido + sumário), rodapé e assinatura. |
| Checagem final | [`checagem-final/`](checagem-final/CHECKLIST.md) | Checklist de qualidade + script `verificar_pdf.py` (nº de páginas, acentos, assinatura). |

## Pré-requisitos

```bash
pip install -r skills/formatacao-docx/requirements.txt
```
PDF: Windows com MS Word (via `docx2pdf`) **ou** LibreOffice no PATH (Linux/Mac/Windows).

## Configurar a assinatura (cada defensor a sua)

O engine usa placeholders por padrão. Configure por variável de ambiente:

```bash
export FORMATAR_PECA_NOME="Fulano de Tal"
export FORMATAR_PECA_CARGO="Defensor(a) Público(a) Federal"
export FORMATAR_PECA_LOCAL="São Luís/MA"
```
…ou passe `assinatura_nome=`, `assinatura_cargo=`, `assinatura_local=` direto em `criar_documento(...)`.

> ⚠️ **LGPD:** a saída (`saida/`) pode conter dados do assistido e é **gitignored**. Nunca versione peças preenchidas. O template (`assets/template_dpu.docx`) é o letterhead institucional, sem dado pessoal.
