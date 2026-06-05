# Projeto BPC/LOAS — Apoio à Defensoria

Material de apoio para **Defensores Públicos** atuarem em casos de **Benefício de Prestação Continuada (BPC/LOAS)** — concessão, manutenção, revisão, suspensão, cessação e recursos — nas vias **judicial e extrajudicial**.

Reúne um **playbook por cenário** (tese + base legal + estratégia + modelo) e **modelos de peça anonimizados** (ofícios de defesa, petições, recurso ao CRPS e inicial judicial), construídos a partir do material da DPU/CCRPREV e da prática da DPU/MA.

> ⚠️ **Foco atual:** o endurecimento do acesso ao BPC pelo **Decreto nº 12.534/2025** — em especial o **cômputo do Bolsa Família** e de pensões indenizatórias na renda per capita, a biometria e a revisão automática.

---

## Como usar

1. Leia **[`playbook/PLAYBOOK-LOAS.md`](playbook/PLAYBOOK-LOAS.md)** — o coração do projeto.
2. Identifique o **cenário** do seu caso na tabela de roteamento (seção 3).
3. Use o **modelo** correspondente em **[`modelos/`](modelos/)** e adapte ao caso concreto.
4. Consulte o **[índice de material](playbook/INDICE-MATERIAL.md)** para localizar normas e precedentes.

### O projeto recebe o CASO, não o problema
O defensor traz a situação e os documentos; o diagnóstico (identificar problemas, teses cabíveis, documentos a pedir e peças a produzir) é tarefa do projeto. Fluxo completo na seção 0 do playbook.

---

## Estrutura

```
playbook/
  PLAYBOOK-LOAS.md      Playbook por cenário (C1–C13): tese, base legal, modelo, pedidos
  INDICE-MATERIAL.md    Índice de modelos, normas e precedentes
modelos/                Modelos de peça ANONIMIZADOS (placeholders [NOME], [CPF], [NB]…)
jurisprudencia/
  base-jurisprudencial-LOAS-BPC.md   Precedentes STF/STJ/TNU — texto oficial (BNP/CJF), sem alteração
skills/                 Pipeline de produção: anti-alucinação → formatação (DOCX+PDF) → checagem final
```

## Produção da peça (skills)
Depois de redigir a peça a partir de um modelo, o projeto entrega o documento final pronto via [`skills/`](skills/README.md):
1. **[anti-alucinação](skills/anti-alucinacao/SKILL.md)** — valida a origem de toda citação (processo, súmula, tema, relator, trecho); o que não tem fonte é removido ou generalizado.
2. **[formatação](skills/formatacao-docx/SKILL.md)** — gera **DOCX + PDF** com layout institucional (cabeçalho, barra lateral com pedido/sumário, rodapé, assinatura). Assinatura configurável por defensor.
3. **[checagem final](skills/checagem-final/CHECKLIST.md)** — checklist + `verificar_pdf.py` (páginas, acentos, assinatura).

```bash
pip install -r skills/formatacao-docx/requirements.txt
export FORMATAR_PECA_NOME="Seu Nome"   # cada defensor configura a sua assinatura
```

## Base jurisprudencial
[`jurisprudencia/base-jurisprudencial-LOAS-BPC.md`](jurisprudencia/base-jurisprudencial-LOAS-BPC.md) reúne precedentes vinculantes (STF/STJ) e acórdãos recentes da TNU, reproduzidos **ipsis litteris** dos bancos oficiais (BNP/CNJ e CJF), com explicações do redator claramente separadas. Cobre: miserabilidade (RG 27/STF, RR 185/STJ), exclusão de renda (Tema 640/STJ, **Tema 369/TNU**), grupo familiar (QO 20/TNU), conceito de deficiência (Tema 378/TNU + Súmulas 29/80), TEA e teto recursal (Tema 807/STF).

---

## ⚠️ Privacidade e LGPD

Este repositório **não contém dados pessoais**. Os modelos foram **anonimizados** (todo nome, CPF, NB e data viraram placeholders). As peças reais que originaram os modelos **não** estão aqui — permanecem locais.

**Ao adaptar um modelo, nunca versione/publique a versão preenchida com dados do assistido.** Mantenha os arquivos preenchidos fora de qualquer repositório público.

---

## Como contribuir

Colegas defensores podem contribuir com novos cenários, teses e modelos:

1. Faça um *fork* e crie um *branch*.
2. Adicione/edite modelos em `modelos/` **sempre anonimizados**.
3. Atualize o playbook e o índice se incluir um cenário novo.
4. Abra um *Pull Request* descrevendo o caso-tipo coberto.

**Regra inegociável:** nenhum PR pode conter nome, CPF, NB, endereço ou qualquer dado de pessoa real.

---

## Licença

[CC BY 4.0](LICENSE) — uso e adaptação livres, com atribuição. Material de apoio; não substitui a análise do caso concreto pelo defensor responsável.
