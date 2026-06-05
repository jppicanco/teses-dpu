# Modelos de Peça (anonimizados)

Modelos reutilizáveis para os cenários do [`playbook`](../playbook/PLAYBOOK-LOAS.md). Todos com placeholders — **preencha com os dados do caso e nunca versione a versão preenchida**.

Convenção de placeholders: `[NOME]`, `[CPF]`, `[NB]`, `[DER]`, `[DATA]`, `[PROTOCOLO]`, `[PAJ]`, `[UNIDADE]`, `[VALOR]`, `[CIDADE/UF]`, `[ÓRGÃO/OFÍCIO DPU]`, `[E-MAIL DPU]`.

| Arquivo | Cenário | Quando usar |
|---|---|---|
| [`00-blocos-reutilizaveis.md`](00-blocos-reutilizaveis.md) | transversal | Blocos prontos (desbloqueio art. 47-E, composição familiar, rendas excluídas, dedução médica) para encaixar em qualquer peça |
| [`01-defesa-adm-excompanheira-grupo-familiar.md`](01-defesa-adm-excompanheira-grupo-familiar.md) | C2 | Revisão por renda — ex-cônjuge/companheiro indevido no grupo |
| [`02-defesa-adm-apuracao-renda-competencia.md`](02-defesa-adm-apuracao-renda-competencia.md) | C4 | Erro de apuração (competência isolada) / filho separado de fato |
| [`03-defesa-adm-renda-1sm-idoso-pcd.md`](03-defesa-adm-renda-1sm-idoso-pcd.md) | C3 | Renda de 1 SM de idoso/PCD de outro membro |
| [`04-defesa-adm-deducao-gastos-medicos.md`](04-defesa-adm-deducao-gastos-medicos.md) | C5 | PCD — dedução de gastos de saúde da renda bruta |
| [`05-defesa-adm-bpc-menor-tea.md`](05-defesa-adm-bpc-menor-tea.md) | C6 | BPC criança/menor (TEA) — atraso do INSS + renda |
| [`06-peticao-reativacao-cessacao-act.md`](06-peticao-reativacao-cessacao-act.md) | C9/C10 | Reativação de BPC cessado (via ACT DPU-INSS) |
| [`07-recurso-crps-flexibilizacao.md`](07-recurso-crps-flexibilizacao.md) | C11 | Recurso ao CRPS com flexibilização de tempestividade |
| [`08-inicial-judicial-computo-bolsa-familia.md`](08-inicial-judicial-computo-bolsa-familia.md) | C1 | Ação judicial (JEF) — BPC indeferido por cômputo do Bolsa Família |
| [`09-inicial-judicial-restabelecimento-rural-65.md`](09-inicial-judicial-restabelecimento-rural-65.md) | C14 | Ação judicial — restabelecimento de BPC/PcD cessado por cômputo de aposentadoria por idade **rural** de membro **< 65 anos** (relativização etária + gênero) |
| [`10-emenda-nulidade-notificacao-digital-pcd.md`](10-emenda-nulidade-notificacao-digital-pcd.md) | T-F / C8-C9 | Emenda/preliminar — nulidade por **notificação só digital** a beneficiário **PcD** sem acesso digital |
