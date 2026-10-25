# Export rukopisu

`python3 tools/export_manuscript.py '40 Books/Název knihy/Manuscript.md' -o /tmp/rukopis.md`

Skript čte pořadí z `Manuscript.md`, nahrazuje pouze transkluze `![[...#Text]]` obsahem sekce `## Text` jednotlivých scén a vypíše čistý Markdown. Cesty mohou být relativní k Manuscriptu nebo ke kořeni vaultu. Při chybě chybí export (exit code != 0). Žádné externí závislosti.
