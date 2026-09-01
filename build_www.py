#!/usr/bin/env python3
"""Sync www/index.html (the Android app's web asset) from the single canonical
source file /home/claude/hidraumiller.html.

hidraumiller.html is written as a fragment (no doctype/html/head/body - that's
how the Claude Artifact tool wraps it for the browser/PWA version). For the
native app it just needs to become a real standalone document. jsPDF is now
embedded inline in hidraumiller.html itself (used by buildDocumentPdf()/
buildListaComprasPdf() for both the native app and the browser/PWA - see
doPrint()/offerPdf() in hidraumiller.html), so no separate vendor script tag
is needed here anymore.

Run this every time hidraumiller.html changes, before `npx cap sync android`.
"""
import os

SRC = "/home/claude/hidraumiller.html"
DEST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "www", "index.html")

with open(SRC, "r", encoding="utf-8") as f:
    content = f.read()

wrapped = (
    '<!DOCTYPE html>\n'
    '<html lang="pt-BR">\n'
    '<head>\n'
    '<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    '</head>\n'
    '<body>\n'
    + content +
    '\n</body>\n'
    '</html>\n'
)

with open(DEST, "w", encoding="utf-8") as f:
    f.write(wrapped)

print(f"wrote {DEST} ({len(wrapped)} bytes)")
