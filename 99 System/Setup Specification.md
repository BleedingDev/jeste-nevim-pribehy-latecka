# Specifikace autorského systému

> Implementační specifikace podle schválených Wayfinder rozhodnutí #2–#10. Nejde o kánon příběhu.

## Zdroje pravdy

- Obsidian Markdown: aktuální svět, postavy, vztahy, děj, scény a rukopis.
- GitHub Issues / Wayfinder: otázky, alternativy, rozhodnutí, praktické úkoly.
- Git: historie změn. Bez paralelních archivů a duplicit.

## Struktura

Jeden vault/repo = jeden svět nebo série. Sdílené entity jsou pouze jednou v `20 World` / `30 Characters`; jednotlivé knihy v `40 Books/<název>/` mají vlastní Book Bible, Plot & Arcs, Scenes a Manuscript.

- `00 Inbox`: rychlý capture, implicitně idea.
- `10 Series`: přehled série.
- `20 World`: místa, frakce, pravidla světa.
- `30 Characters`: jedna master note na postavu.
- `40 Books`: specifický děj a rukopis jednotlivých knih.
- `90 Research`: evidence, nikoli kánon.
- `99 System`: pravidla, šablony, nástroje.

Nevytvářet preventivně samostatné notes. Vlastní note vzniká pro samostatnou identitu, vývoj, opakované odkazy nebo filtrování.

## Metadata a odkazy

YAML properties jsou pouze index (např. `type`, `status`, `books`, `characters`, `location`); význam vztahů patří do Markdownu a `[[wikilinků]]`.

- `status`: `idea | working | canon | deprecated` = kanoničnost.
- `stage`: `outline | draft | revision | ready` = stav psané jednotky.
- Obsah se nestává `canon` přesunem, odkazem ani commitem; pouze explicitním rozhodnutím autora/pověřeného člověka. AI nekanonizuje.
- Před `ready` proběhne consistency pass vůči master notes.

## Od nápadu k rukopisu

Inbox zpracovávat `promote or consume`: jednu entitu přesunout; víc entit promítnout jejich vlastníkům a capture odstranit; výzkum přesunout do Research. Neudržovat `Processed` archiv. Každý fakt má jedno autoritativní místo, ostatní notes odkazují.

Přímo v Obsidianu: capture, běžné psaní a revize. Wayfinder: skutečné rozhodnutí s variantami, dopadem napříč entitami nebo potřeba research/lidského souhlasu. GitHub task: již rozhodnutá implementace.

Scene note obsahuje plán i jediný aktuální text pod přesným `## Text`. `Manuscript.md` určuje pořadí pomocí `![[Scenes/001 - Název#Text]]`; prózu nekopíruje. `tools/export_manuscript.py` vytvoří přenosný čistý Markdown bez YAML a plánovacích sekcí. PDF/DOCX/EPUB až jako volitelný downstream.

## Git a AI

- Autor: běžné psaní i explicitní změny kánonu přímo do `main`.
- AI: změny souborů vždy vlastní větev + PR; review a merge provede autor/pověřený člověk.
- Budoucí spoluautor: pravidla až při zapojení.
- Před prací synchronizovat, minimalizovat souběžné úpravy stejných notes.
- Necommitovat PAT, `.env`, workspace state, plugin `data.json` ani cache.

## Wayfinder

GitHub issue s `wayfinder:map` = mapa. Decision ticket má právě jeden `wayfinder:<type>`; pokud není native sub-issue, první řádek `Part of #N`. Resolution comment na ticket, krátký odkaz v mapě. Wayfinder Maps je read-only vizualizace. Frontier používá native dependencies, nevyrábět textové falešné blockery.

## Hranice obsahu

Původní handoff v Inboxu je pracovní vstup, nikoli kánon. Barnabáš a další příběhové volby nejsou tímto setupem schváleny. Samostatné mapy pro svět, postavy a příběh vzniknou až po dokončení setupu.

## Implementační kontrola

- [x] Zdokumentovaná struktura a pravidla
- [x] Minimální složky a šablony
- [x] Přenosný exportní skript
- [ ] Autorův review a merge PR #5
- [ ] Uzavření setup mapy #1 po mergi
