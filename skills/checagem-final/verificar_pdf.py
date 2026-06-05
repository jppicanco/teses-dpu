#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Checagem final do PDF gerado pela skill de formatação.

Verifica automaticamente os itens do CHECKLIST.md:
- nº de páginas (> 1)
- ausência de caracteres de encoding quebrado (ï¿½ / �)
- presença da assinatura (nome configurado ou placeholder)
- tamanho mínimo razoável

Uso:
    python skills/checagem-final/verificar_pdf.py saida/PECA_FINAL.pdf
    python skills/checagem-final/verificar_pdf.py saida/PECA_FINAL.pdf --nome "Fulano de Tal"

Saída: relatório no terminal + exit code 0 (tudo OK) ou 1 (há alertas).
"""
import sys
import os
import argparse

try:
    from pypdf import PdfReader
except ImportError:  # fallback para PyPDF2
    try:
        from PyPDF2 import PdfReader
    except ImportError:
        print("[ERRO] Instale pypdf: pip install pypdf")
        sys.exit(2)


def verificar(caminho_pdf, nome_assinatura=None, min_kb=80):
    if not os.path.exists(caminho_pdf):
        print(f"[ERRO] Arquivo não encontrado: {caminho_pdf}")
        return False

    alertas = []
    ok = []

    tamanho_kb = os.path.getsize(caminho_pdf) / 1024
    (ok if tamanho_kb >= min_kb else alertas).append(
        f"Tamanho do PDF: {tamanho_kb:.0f} KB" + ("" if tamanho_kb >= min_kb else f" (< {min_kb} KB — suspeito)")
    )

    reader = PdfReader(caminho_pdf)
    n_pag = len(reader.pages)
    (ok if n_pag > 1 else alertas).append(
        f"Páginas: {n_pag}" + ("" if n_pag > 1 else " (só 1 página — provável falta de marcadores ##)")
    )

    texto = "\n".join((p.extract_text() or "") for p in reader.pages)

    # encoding quebrado
    if "�" in texto or "ï¿½" in texto:
        alertas.append("Caracteres de encoding quebrado detectados (�) — verifique UTF-8")
    else:
        ok.append("Acentuação/encoding OK")

    # assinatura
    marcadores = []
    if nome_assinatura:
        marcadores.append(nome_assinatura.upper())
    marcadores += ["[NOME DO(A) DEFENSOR(A)]", "DEFENSOR"]
    achou = any(m.upper() in texto.upper() for m in marcadores)
    if achou:
        if "[NOME DO(A) DEFENSOR(A)]" in texto:
            alertas.append("Assinatura ainda é PLACEHOLDER — configure FORMATAR_PECA_NOME antes do uso real")
        else:
            ok.append("Bloco de assinatura presente")
    else:
        alertas.append("Bloco de assinatura NÃO encontrado")

    # relatório
    print("=" * 56)
    print(f"CHECAGEM FINAL — {os.path.basename(caminho_pdf)}")
    print("=" * 56)
    for o in ok:
        print(f"  [OK]    {o}")
    for a in alertas:
        print(f"  [ALERTA] {a}")
    print("-" * 56)
    print("RESULTADO:", "TUDO OK" if not alertas else f"{len(alertas)} ALERTA(S) — revisar")
    return not alertas


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Checagem final do PDF de peça")
    ap.add_argument("pdf", help="Caminho do PDF a verificar")
    ap.add_argument("--nome", help="Nome esperado na assinatura", default=None)
    ap.add_argument("--min-kb", type=int, default=80, help="Tamanho mínimo aceitável em KB")
    args = ap.parse_args()
    sys.exit(0 if verificar(args.pdf, args.nome, args.min_kb) else 1)
